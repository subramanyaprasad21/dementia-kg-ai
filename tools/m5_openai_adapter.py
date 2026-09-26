"""Narrow Responses REST adapter. Live use requires separately approved budget."""
import argparse
from datetime import datetime, timezone
from decimal import Decimal
import json
import os
from pathlib import Path
import urllib.request
import urllib.error
import socket
import uuid
import m5_evidence_answers as ai

LIMITS = dict(model=ai.MODEL, generationCalls=14, httpRequests=28,
              inputTokensPerCall=100000, outputTokensPerCall=4096,
              reservedUSD='5.00', inputUSDPerMillion='2.00', outputUSDPerMillion='10.00')


def now():
    return datetime.now(timezone.utc).isoformat()


def save(path, value):
    temp = path.with_suffix(path.suffix+'.tmp')
    temp.write_bytes(ai.corpus.encode(value))
    temp.replace(path)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class DiagnosticError(RuntimeError):
    """Only closed-vocabulary diagnostics; never provider text or headers."""
    def __init__(self, category, phase, **metadata):
        self.diagnostic = dict(category=category, phase=phase, **metadata)
        super().__init__('OpenAI request failed; no retry performed. See safe diagnostic.')


def validate_request(route, payload):
    """Validate this approved pilot contract, not universal API/model support."""
    def fail(category):
        raise DiagnosticError(category, 'local_validation', transmission='not_started')
    if route not in {'responses', 'responses/input_tokens'}:
        fail('endpoint_invalid')
    if not isinstance(payload, dict):
        fail('payload_invalid')
    try:
        body = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode('utf-8')
        json.loads(body)
    except (TypeError, ValueError, UnicodeError):
        fail('serialization_invalid')
    fields = {'model', 'input', 'instructions', 'tools', 'text'}
    if route == 'responses':
        fields |= {'store', 'reasoning', 'max_output_tokens'}
    if set(payload) != fields:
        fail('request_fields_invalid')
    if payload['model'] != ai.MODEL:
        fail('model_not_approved')
    if not all(isinstance(payload[k], str) and payload[k] for k in ('input', 'instructions')):
        fail('payload_invalid')
    if payload['tools'] != []:
        fail('tools_not_approved')
    expected = dict(format=dict(type='json_schema', name='dementia_evidence_answer', strict=True, schema=ai.SCHEMA))
    if payload['text'] != expected:
        fail('structured_output_invalid')
    if route == 'responses':
        if payload['reasoning'] != {'effort': 'low'}:
            fail('reasoning_not_approved')
        if type(payload['max_output_tokens']) is not int or payload['max_output_tokens'] != 4096 or payload['store'] is not False:
            fail('configuration_not_approved')
    return ai.corpus.encode(payload)


# Deliberately exclude free-text provider messages, arbitrary parameter strings,
# request IDs and all headers. Unknown values become 'unclassified'.
ERROR_CODES = {'invalid_api_key', 'insufficient_quota', 'rate_limit_exceeded',
               'model_not_found', 'unsupported_parameter', 'unsupported_value',
               'invalid_json_schema', 'invalid_value', 'context_length_exceeded'}
ERROR_TYPES = {'invalid_request_error', 'authentication_error', 'permission_error',
               'rate_limit_error', 'server_error', 'insufficient_quota'}
ERROR_PARAMS = {'model', 'reasoning', 'reasoning.effort', 'text.format',
                'text.format.schema', 'max_output_tokens', 'tools', 'input', 'store'}


def post(route, payload, key):
    body = validate_request(route, payload)
    if not key or key.encode() in body:
        raise DiagnosticError('unsafe_credential_content', 'local_validation', transmission='not_started')
    try:
        request = urllib.request.Request('https://api.openai.com/v1/'+route, data=body,
                                         headers={'Authorization': 'Bearer '+key, 'Content-Type': 'application/json'}, method='POST')
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    except Exception:
        raise DiagnosticError('client_construction_failed', 'request_construction', transmission='not_started') from None
    try:
        with opener.open(request, timeout=120) as response:
            raw = response.read(4*1024*1024+1)
        if len(raw) > 4*1024*1024 or key.encode() in raw:
            raise DiagnosticError('unsafe_or_oversized_response', 'response_read', transmission='attempted')
        return raw
    except urllib.error.HTTPError as error:
        # Read only a bounded error body in memory. Persist only allowlisted
        # classification values, never text, raw bytes, headers or the exception.
        safe = dict(httpStatus=error.code if type(error.code) is int and 100 <= error.code <= 599 else None)
        try:
            raw = error.read(65537)
            data = json.loads(raw).get('error', {}) if len(raw) <= 65536 and key.encode() not in raw else {}
            for field, allowed in [('code', ERROR_CODES), ('type', ERROR_TYPES), ('param', ERROR_PARAMS)]:
                value = data.get(field)
                safe['api_'+field] = value if isinstance(value, str) and value in allowed else 'unclassified'
        except Exception:
            safe['errorBodyClassification'] = 'unavailable'
        finally:
            error.close()
        raise DiagnosticError('http_rejection', 'http_response', transmission='response_received', **safe) from None
    except DiagnosticError:
        raise
    except (TimeoutError, socket.timeout):
        raise DiagnosticError('timeout', 'transport', transmission='unknown') from None
    except urllib.error.URLError:
        raise DiagnosticError('connection_error', 'transport', transmission='unknown') from None
    except Exception:
        raise DiagnosticError('unclassified_client_error', 'transport_or_read', transmission='unknown') from None


def run(prepared, condition, directory, approved=False, transport=None, reviewed_failure_ids=()):
    """One serial attempt. Same ledger must be reused; failures reserve cost.

    Injectable transport is for offline tests. No API request occurs without
    approved=True, including input-token counting.
    """
    if not approved:
        raise PermissionError('Explicit live-pilot budget approval is required')
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        raise RuntimeError('OPENAI_API_KEY is unavailable in this process environment')
    request = ai.request_for(prepared, condition)
    directory = Path(directory).resolve()
    if directory == ai.corpus.ROOT or ai.corpus.ROOT in directory.parents:
        raise ValueError('Run artifacts must be outside the Git repository')
    if key.encode() in ai.corpus.encode(prepared):
        raise ValueError('Credential unexpectedly present in prepared content')
    if condition != 'model_only' and not prepared['canCallModel']:
        return {'status': 'ABSTAINED-NO-RETRIEVABLE-SUPPORT', 'apiCalls': 0}
    directory.mkdir(parents=True, exist_ok=True)
    # Exclusive serial process lock. An interrupted lock needs explicit review.
    lock = directory/'run.lock'
    try:
        handle = lock.open('x')
    except FileExistsError:
        raise RuntimeError('Run already active or interrupted; review ledger before resuming') from None
    handle.close()
    try:
        path = directory/'ledger.json'
        if path.exists():
            ledger = ai.corpus.read(path)
        else:
            if any(p.name != 'run.lock' for p in directory.iterdir()):
                raise ValueError('Missing ledger in existing nonempty run directory')
            ledger = dict(profile='m5-openai-pilot-ledger-1', id=str(uuid.uuid4()), created=now(),
                          limits=LIMITS, httpRequests=0, generationCalls=0, reservedUSD='0', attempts=[])
        if ledger['limits'] != LIMITS:
            raise ValueError('Budget/configuration changed; no automatic reset')
        reviewed = set(reviewed_failure_ids)
        failed = {a['runId'] for a in ledger['attempts'] if a['status'] == 'failed-review-required'}
        if not reviewed <= failed or any(a['status'] != 'completed' and a['runId'] not in reviewed for a in ledger['attempts']):
            raise RuntimeError('Prior incomplete/failed attempt requires review; budget remains reserved')
        if ledger['httpRequests']+2 > LIMITS['httpRequests'] or ledger['generationCalls'] >= LIMITS['generationCalls']:
            raise RuntimeError('Pilot request/call ceiling reached')
        ident = f"{len(ledger['attempts'])+1:03d}"
        record = dict(runId=str(uuid.uuid4()), condition=condition, started=now(), status='counting',
                      promptVersion=ai.PROMPT_VERSION, modelRequested=request['model'],
                      requestSha256=ai.corpus.digest(ai.corpus.encode(request)),
                      parameters={k: request[k] for k in ('model', 'reasoning', 'max_output_tokens', 'store', 'tools')},
                      corpusManifestSha256=prepared['corpusManifestSha256'])
        if reviewed:
            record['ownerReviewedFailureIds'] = sorted(reviewed)
        ledger['attempts'].append(record)
        save(path, ledger)
        (directory/(ident+'.request.json')).write_bytes(ai.corpus.encode(request))
        (directory/(ident+'.prepared.json')).write_bytes(ai.corpus.encode(prepared))
        call = transport or post
        def invoke(route, payload):
            ledger['httpRequests'] += 1
            save(path, ledger)
            raw = call(route, payload, key)
            if not isinstance(raw, bytes) or len(raw) > 4*1024*1024 or key.encode() in raw:
                raise ValueError('Unsafe response; content not retained')
            return raw
        try:
            count_payload = {k: request[k] for k in ('model', 'input', 'instructions', 'tools', 'text')}
            counted = json.loads(invoke('responses/input_tokens', count_payload))
            tokens = counted.get('input_tokens')
            if type(tokens) is not int or not 0 <= tokens <= LIMITS['inputTokensPerCall']:
                raise ValueError('Input token count exceeds approved bound or is invalid')
            record['countedInputTokens'] = tokens
            reserve = (Decimal(tokens)*Decimal(LIMITS['inputUSDPerMillion'])+
                       Decimal(LIMITS['outputTokensPerCall'])*Decimal(LIMITS['outputUSDPerMillion']))/1000000
            if Decimal(ledger['reservedUSD'])+reserve > Decimal(LIMITS['reservedUSD']):
                raise ValueError('Pilot cost ceiling reached')
            ledger['reservedUSD'] = str(Decimal(ledger['reservedUSD'])+reserve)
            ledger['generationCalls'] += 1
            record['reservedUSD'] = str(reserve)
            record['status'] = 'generation-attempted'
            save(path, ledger)  # reserve before potentially billable generation
            raw = invoke('responses', request)
            response = json.loads(raw)
            (directory/(ident+'.response.json')).write_bytes(raw)
            record['responseSha256'] = ai.corpus.digest(raw)
            record['modelReturned'] = response.get('model')
            record['responseId'] = response.get('id')
            usage = response.get('usage')
            if not isinstance(usage, dict) or any(type(usage.get(k)) is not int or usage[k] < 0 for k in ('input_tokens', 'output_tokens')):
                raise ValueError('Missing/invalid usage accounting')
            record['usage'] = usage
            if usage['input_tokens'] > tokens or usage['output_tokens'] > LIMITS['outputTokensPerCall']:
                raise ValueError('Provider usage exceeds reservation; stop for review')
            candidate = ai.parse_response(prepared, response)
            if condition == 'model_only':
                result = dict(status='UNVERIFIED-MODEL-ONLY', candidate=candidate, acceptedAssertions=[])
            else:
                # Reuse the same generation for the retrieval/verified conditions.
                result = dict(retrieval=ai.verify(prepared, candidate, False), verified=ai.verify(prepared, candidate, True))
            (directory/(ident+'.result.json')).write_bytes(ai.corpus.encode(result))
            record['status'] = 'completed'
            record['finished'] = now()
            save(path, ledger)
            return dict(runId=record['runId'], status='completed', result=result)
        except Exception as error:
            record['diagnostic'] = error.diagnostic if isinstance(error, DiagnosticError) else dict(category='unclassified_processing_failure', phase='adapter_processing', transmission='unknown')
            record['status'] = 'failed-review-required'
            record['finished'] = now()
            save(path, ledger)
            raise RuntimeError('Run stopped; inspect sanitized ledger. No retry or budget refund.') from None
    finally:
        lock.unlink()


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('prepared')
    p.add_argument('--condition', choices=['model_only', 'retrieval', 'verified'], required=True)
    p.add_argument('--directory', required=True)
    p.add_argument('--approved-pilot', action='store_true', help='Use only after explicit owner approval of documented pilot')
    a = p.parse_args()
    try:
        outcome = run(ai.corpus.read(Path(a.prepared)), a.condition, a.directory, a.approved_pilot)
        print(outcome['status'])
    except (RuntimeError, ValueError, PermissionError) as error:
        print(str(error))
        raise SystemExit(1)
