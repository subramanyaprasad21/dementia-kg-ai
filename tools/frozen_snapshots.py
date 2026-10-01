"""Helpers for verifying immutable historical snapshots without pinning living files."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive" / "frozen"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def snapshot_root(name: str) -> Path:
    root = ARCHIVE / name
    if not root.is_dir():
        raise ValueError(f"Missing frozen snapshot: {name}")
    return root


def load_json(path: Path):
    return json.loads(path.read_bytes())


def verify_mapping(mapping: dict[str, str], root: Path) -> dict[str, str]:
    """Verify every path in a historical digest mapping against one snapshot root."""
    verified = {}
    root = Path(root)
    for relative, expected in mapping.items():
        path = root / relative
        if not path.is_file():
            raise ValueError(f"Missing frozen authority: {relative}")
        actual = digest(path.read_bytes())
        if actual != expected:
            raise ValueError(f"Frozen authority mismatch: {relative}")
        verified[relative] = actual
    return verified


def verify_manifest_section(manifest: Path, section: str, snapshot: str) -> dict[str, str]:
    data = load_json(Path(manifest))
    mapping = data.get(section)
    if not isinstance(mapping, dict):
        raise ValueError(f"Manifest section is not a digest mapping: {section}")
    return verify_mapping(mapping, snapshot_root(snapshot))
