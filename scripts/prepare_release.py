"""Prepare reviewed v5 release metadata locally. No network or credentials."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote

EXPECTED_SHA256 = "0b3a77dddde319ad7a7435102493b72de2646fd3b09cb49bd7356db0b98eee31"
CERT_SHA256 = "79533c8ad5e18c34a8958513b14aba52fa7783af1641a9cff1c8be8b0e8e7bd6"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--apk", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+", args.repo):
        parser.error("Expected GitHub OWNER/REPO")
    if not args.apk.is_file():
        parser.error("APK file is missing")
    digest = hashlib.sha256()
    with args.apk.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    if digest.hexdigest() != EXPECTED_SHA256:
        parser.error("This is not the reviewed final v5 APK; refusing incorrect metadata")
    base = f"https://github.com/{args.repo}/releases"
    manifest = {
        "schemaVersion": 1,
        "channel": "stable",
        "packageName": "com.qidi.glass.superapp",
        "versionCode": 150,
        "versionName": "1.2.0-offline-v5",
        "minSdk": 28,
        "downloadUrl": f"{base}/download/v5/{quote(args.apk.name, safe='')}",
        "sha256": EXPECTED_SHA256,
        "sizeBytes": args.apk.stat().st_size,
        "signerCertificateSha256": CERT_SHA256,
        "releaseNotesUrl": f"{base}/tag/v5",
    }
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "update.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (args.out / "SHA256SUMS.txt").write_text(f"{EXPECTED_SHA256}  {args.apk.name}\n", encoding="utf-8")
    print(f"Prepared local metadata for {args.repo}; remote publication is not performed.")


if __name__ == "__main__":
    main()
