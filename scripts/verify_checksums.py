"""Check that the raw files match the SHA-256 values in CHECKSUMS.sha256.

Run from the repository root:
    python scripts/verify_checksums.py
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


ok = True
for line in (ROOT / "CHECKSUMS.sha256").read_text().splitlines():
    if not line.strip():
        continue
    expected, rel = line.split(maxsplit=1)
    path = ROOT / rel.strip()
    if not path.exists():
        print(f"MISSING  {rel}")
        ok = False
        continue
    match = sha256(path) == expected
    ok &= match
    print(f"{'OK     ' if match else 'MISMATCH'} {rel}")

sys.exit(0 if ok else 1)
