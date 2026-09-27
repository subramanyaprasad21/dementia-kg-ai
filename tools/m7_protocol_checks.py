"""Offline M7 proposal arithmetic, eligibility declarations and scoring checks.

No model client, live runner, question generator or human-review substitute.
"""
from collections import Counter
from decimal import Decimal
import re

STATUSES={'completed','api-error','timeout','refusal','invalid-output','retrieval-failure','verification-failure'}
LABELS={'supported','unsupported','contradicted','unresolved'}

def budget(plan):
    b=plan['formalBudget']; n=plan['questionCount']
    assert n==12 and b['generations']==2*n and b['tokenCountRequests']==2*n
    assert b['maxHTTPRequests']==4*n
    assert b['inputTokens']==2*n*plan['maxInputTokensPerCall']
    assert b['outputTokens']==2*n*plan['maxOutputTokensPerCall']
    cost=(Decimal(b['inputTokens'])*Decimal(b['inputUSDPerMillion'])+Decimal(b['outputTokens'])*Decimal(b['outputUSDPerMillion']))/1000000
    assert cost==Decimal(b['tokenCostCeilingUSD'])
    retry=plan['developmentQ07Retry']
    retrycost=(Decimal(retry['maxInputTokens'])*Decimal(b['inputUSDPerMillion'])+Decimal(retry['maxOutputTokens'])*Decimal(b['outputUSDPerMillion']))/1000000
    assert retrycost==Decimal(retry['maximumReservationUSD'])
    assert cost+retrycost==Decimal(plan['combinedNewCeilingUSD'])<=Decimal(plan['proposedAdditionalSpendCapUSD'])
    assert cost+retrycost+Decimal(plan['priorReservationUSD'])==Decimal(plan['combinedCumulativeReservationCeilingUSD'])<=Decimal(plan['proposedCumulativeSpendCapUSD'])
    return {'formalUSD':str(cost),'newIncludingDevelopmentRetryUSD':str(cost+retrycost)}

def canonical_question(text):
    return ' '.join(re.findall(r'\w+',text.casefold()))

def validate_items(items, development_questions, allowed_roots, strata):
    """Mechanical checks only; attestations do not prove human independence/novelty."""
    if len(items)!=12:raise ValueError('Exactly 12 reviewed items required')
    banned={canonical_question(q) for q in development_questions};seen=set();identifiers=set();allocation=Counter()
    for item in items:
        text=item['question'];ident=item['id'];signature=canonical_question(text)
        if not isinstance(text,str) or not text.strip() or len(text.encode())>4096 or signature in banned|seen or ident in identifiers:
            raise ValueError('Invalid, repeated or exposed question')
        if item['category'] not in {'answerable','insufficient'} or item['stratum'] not in strata:raise ValueError('Wrong allocation')
        if not item['rootIds'] or len(item['rootIds'])>8 or len(set(item['rootIds']))!=len(item['rootIds']) or not set(item['rootIds'])<=set(allowed_roots):raise ValueError('Invalid fixed source scope')
        if not item['dependencyGroups'] or not item['requiredFactIds'] or len(set(item['requiredFactIds']))!=len(item['requiredFactIds']):raise ValueError('Missing gold/dependency scope')
        if not item['requiredQualifications']:raise ValueError('Missing qualification rubric')
        if item['category']=='insufficient' and not item['requiredAbstention']:raise ValueError('Missing abstention rubric')
        reviews=item['eligibilityReviews']
        if len(reviews)!=2 or len({r['reviewerId'] for r in reviews})!=2 or any(not r['reviewerId'] or r['decision']!='eligible' or not r['rationale'] for r in reviews):raise ValueError('Two explicit eligibility reviews required')
        if item['origin']!='human-authored' or item['developmentExposed'] or item['nearParaphraseOfDevelopment'] or item['syntheticControl']:raise ValueError('Not eligible for proposed question holdout')
        if not item['selfContained'] or not item['goldReviewed']:raise ValueError('Review incomplete')
        seen.add(signature);identifiers.add(ident);allocation[(item['stratum'],item['category'])]+=1
    if allocation!=Counter({(s,c):1 for s in strata for c in ('answerable','insufficient')}):raise ValueError('Unbalanced construction')
    return True

def readiness(plan, *, approved=False, reviewers=(), dataset_frozen=False, code_frozen=False, access_log=False, dispositions=False, pricing_verified=False, retrieval_passed=False):
    budget(plan)
    gates={'ownerApproval':approved,'twoDistinctReviewers':len(set(reviewers))==2 and all(reviewers),
           'datasetFrozen':dataset_frozen,'codeFrozen':code_frozen,'accessLog':access_log,
           'developmentDispositions':dispositions,'pricingVerified':pricing_verified,'retrievalDryRun':retrieval_passed}
    return {'ready':all(gates.values()),'unmet':[k for k,v in gates.items() if not v]}

def ratio(n,d):return None if not d else n/d

def aggregate(items, annotations):
    """Aggregate adjudicated source-relative labels; never infer them from text.

    One condition at a time. Retained labels belong to its assertion surface;
    prose labels cover the full unchanged answer prose. Failures remain in N.
    """
    expected={i['id']:i for i in items}
    if len(annotations)!=len(items) or {a['id'] for a in annotations}!=set(expected):raise ValueError('Missing/duplicate outcome')
    precision=[];relevance=[];provenance=[];recall=[];unsafe=[];unknown=[];failure=Counter();qpass=abstain=over=zero=emitted=0
    categories=Counter(i['category'] for i in items)
    for a in annotations:
        item=expected[a['id']];status=a['status']
        if status not in STATUSES:raise ValueError('Unknown status')
        required=set(item['requiredFactIds'])
        if not required:raise ValueError('No fixed gold denominator')
        if status!='completed':
            if a.get('retainedLabels') or a.get('proseLabels') or a.get('supportedFactIds') or a.get('qualificationPass') or a.get('abstentionPass') or a.get('excessiveAbstention'):raise ValueError('Failure is not a successful or abstaining answer')
            failure[status]+=1;recall.append(0);zero+=1
            continue
        if set(a['retainedLabels'])-LABELS or set(a['proseLabels'])-LABELS:raise ValueError('Unknown human label')
        if not set(a['supportedFactIds'])<=required or len(set(a['supportedFactIds']))!=len(a['supportedFactIds']):raise ValueError('Invalid/duplicate gold match')
        if type(a['qualificationPass']) is not bool:raise ValueError('Unscored qualification')
        if item['category']=='insufficient':
            if type(a['abstentionPass']) is not bool or a['excessiveAbstention'] is not None:raise ValueError('Wrong abstention category')
        elif type(a['excessiveAbstention']) is not bool or a['abstentionPass'] is not None:raise ValueError('Wrong abstention category')
        labels=a['retainedLabels'];emitted+=len(labels)
        for field in ['retainedRelevant','provenanceCorrect']:
            if len(a[field])!=len(labels) or any(type(v) is not bool for v in a[field]):raise ValueError('Unscored relevance/provenance')
        if labels:
            relevance.append(sum(a['retainedRelevant'])/len(labels))
            provenance.append(sum(a['provenanceCorrect'])/len(labels))
        if labels:precision.append(labels.count('supported')/len(labels))
        else:zero+=1
        prose=a['proseLabels']
        if prose:
            unsafe.append(sum(x in {'unsupported','contradicted'} for x in prose)/len(prose));unknown.append(prose.count('unresolved')/len(prose))
        recall.append(len(a['supportedFactIds'])/len(required));qpass+=a['qualificationPass']
        abstain+=a['abstentionPass'] is True;over+=a['excessiveAbstention'] is True
    return dict(n=len(items),completed=len(items)-sum(failure.values()),failures=dict(failure),
                retainedAssertionPrecision=ratio(sum(precision),len(precision)),precisionDefinedItems=len(precision),retainedAssertions=emitted,
                retainedRelevance=ratio(sum(relevance),len(relevance)),provenanceAccuracy=ratio(sum(provenance),len(provenance)),
                requiredFactRecall=ratio(sum(recall),len(items)),zeroRetainedRate=ratio(zero,len(items)),
                unsupportedProseRate=ratio(sum(unsafe),len(unsafe)),proseDefinedItems=len(unsafe),unresolvedProseRate=ratio(sum(unknown),len(unknown)),
                qualificationPassRate=ratio(qpass,len(items)),requiredAbstentionPassRate=ratio(abstain,categories['insufficient']),
                excessiveAbstentionRate=ratio(over,categories['answerable']))


def retrieval_coverage(required_support, supplied):
    """Exact required assertion-slot coverage, not completeness of biology."""
    if not required_support or any(not values for values in required_support.values()):
        raise ValueError('Explicit nonempty gold support slots required')
    return sum(set(values)<=set(supplied) for values in required_support.values())/len(required_support)

def paired_precision_difference(items, grounded, verified):
    """Descriptive verification-minus-grounded delta on defined pairs only."""
    aggregate(items,grounded);aggregate(items,verified)
    left={a['id']:a for a in grounded};right={a['id']:a for a in verified};deltas=[]
    for item in items:
        a,b=left[item['id']],right[item['id']]
        if a['status']==b['status']=='completed' and a['retainedLabels'] and b['retainedLabels']:
            deltas.append(b['retainedLabels'].count('supported')/len(b['retainedLabels'])-a['retainedLabels'].count('supported')/len(a['retainedLabels']))
    return {'difference':ratio(sum(deltas),len(deltas)),'definedPairs':len(deltas),'plannedItems':len(items)}
