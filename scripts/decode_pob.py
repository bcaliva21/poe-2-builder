#!/usr/bin/env python3
"""Decode a Path of Building export code to XML/text."""

from __future__ import annotations

import argparse
import base64
import re
import sys
import zlib


def normalize_code(raw: str) -> str:
    code = raw.strip()
    # Allow accidental wrapping / URL paste noise
    code = code.replace("\n", "").replace("\r", "").replace(" ", "")
    if "http" in code and "eN" in code:
        match = re.search(r"(eN[A-Za-z0-9_\-+/=]+)", code)
        if match:
            code = match.group(1)
    return code


def decode_pob(code: str) -> str:
    code = normalize_code(code)
    padded = code + ("=" * (-len(code) % 4))
    # PoB uses URL-safe base64 variants in the wild
    for variant in (
        padded,
        padded.replace("-", "+").replace("_", "/"),
    ):
        try:
            raw = base64.b64decode(variant)
        except Exception:
            continue
        for wbits in (zlib.MAX_WBITS, -zlib.MAX_WBITS, zlib.MAX_WBITS | 16):
            try:
                return zlib.decompress(raw, wbits).decode("utf-8", errors="replace")
            except Exception:
                pass
        # Some exports prefix a single version/method byte
        if len(raw) > 1:
            for wbits in (zlib.MAX_WBITS, -zlib.MAX_WBITS, zlib.MAX_WBITS | 16):
                try:
                    return zlib.decompress(raw[1:], wbits).decode("utf-8", errors="replace")
                except Exception:
                    pass
    raise ValueError("Could not decode PoB code (bad base64/zlib payload)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="PoB code string, or omit to read stdin")
    parser.add_argument("-o", "--output", help="Write decoded build to this path")
    args = parser.parse_args()

    raw = args.input if args.input else sys.stdin.read()
    if not raw.strip():
        print("No PoB code provided", file=sys.stderr)
        return 1

    try:
        decoded = decode_pob(raw)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(decoded)
        print(args.output)
    else:
        sys.stdout.write(decoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
