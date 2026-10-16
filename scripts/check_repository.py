#!/usr/bin/env python3
"""Run portable, limited repository checks for HAIO-GATS."""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = (
    "canonical-event.schema.json",
    "authority-grant.schema.json",
    "approval-receipt.schema.json",
    "outcome-receipt.schema.json",
)


def check_schemas() -> bool:
    passed = True
    for name in SCHEMAS:
        path = ROOT / "schemas" / name
        try:
            with path.open(encoding="utf-8") as source:
                json.load(source)
            print(f"PASS JSON syntax: schemas/{name}")
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            print(f"FAIL JSON syntax: schemas/{name}: {error}", file=sys.stderr)
            passed = False
    return passed


def check_whitespace(base: Optional[str]) -> bool:
    ranges = [[f"{base}...HEAD"]] if base else [[], ["--cached"]]
    passed = True
    for revision in ranges:
        result = subprocess.run(
            ["git", "diff", "--check", *revision],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            print(result.stderr or result.stdout, file=sys.stderr, end="")
            passed = False
    print(f"{'PASS' if passed else 'FAIL'} Git whitespace check")
    return passed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="Base commit for checking a pull request")
    args = parser.parse_args()
    schemas_passed = check_schemas()
    whitespace_passed = check_whitespace(args.base)
    return 0 if schemas_passed and whitespace_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
