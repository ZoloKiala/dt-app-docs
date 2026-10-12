"""Publish the Limpopo production catalogue to S3, with a backup and rollback.

The portal reads its catalogue from a single S3 object. This replaces that
object with a prepared file, verifies the result over the public URL the portal
actually uses, and puts the old catalogue back if anything looks wrong.

    python tools/publish_prod_catalogue.py            # dry run, changes nothing
    python tools/publish_prod_catalogue.py --publish  # back up, upload, verify

Standard library only, so it runs under whichever Python is on your PATH. It
signs its own S3 requests rather than depending on boto3 being installed in
that particular environment.

Credentials come from the usual AWS environment variables if set, otherwise
from dt-app/dt_limpopo/serverconfig.json.

Note on the automation script: dt-app/automation/terria/main.py also uploads to
this key, but its output is stale (5 groups, 71 KB against the live 10 groups
and 609 KB). Do not run it against production without checking its output first.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUCKET = "iwmi-dt-odc-products-public"
KEY = "limpopo_dt_prod.json"
REGION = "af-south-1"
HOST = f"{BUCKET}.s3.{REGION}.amazonaws.com"
PUBLIC_URL = f"https://{HOST}/{KEY}"

SOURCE = ROOT / "dt-app/dt_limpopo/wwwroot/init/limpopo_dt_prod.updated.json"
BACKUP_DIR = ROOT / "dt-app/dt_limpopo/wwwroot/init"

# What the new catalogue must contain for the upload to count as a success.
REQUIRED = ("wapor_downscale_20m", "wapor_et_timeseries")
MIN_GROUPS = 10

EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()


# --------------------------------------------------------------------------- #
# credentials
# --------------------------------------------------------------------------- #

def credentials() -> tuple[str, str]:
    key_id = os.getenv("AWS_ACCESS_KEY_ID")
    secret = os.getenv("AWS_SECRET_ACCESS_KEY")
    if key_id and secret:
        print("credentials: AWS_ environment variables")
        return key_id, secret

    config_path = ROOT / "dt-app/dt_limpopo/serverconfig.json"
    share = json.loads(config_path.read_text(encoding="utf-8"))["shareUrlPrefixes"]["s"]
    print(f"credentials: {config_path.name}, key {share['accessKeyId'][:8]}...")
    return share["accessKeyId"], share["secretAccessKey"]


# --------------------------------------------------------------------------- #
# minimal AWS SigV4, enough for one GET and one PUT
# --------------------------------------------------------------------------- #

def _sign(key: bytes, message: str) -> bytes:
    return hmac.new(key, message.encode("utf-8"), hashlib.sha256).digest()


def signed_request(method: str, body: bytes | None = None,
                   content_type: str | None = None) -> urllib.request.Request:
    """Build a SigV4-signed request for this bucket and key."""
    key_id, secret = CREDENTIALS
    now = datetime.datetime.now(datetime.timezone.utc)
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = now.strftime("%Y%m%d")
    payload_hash = hashlib.sha256(body).hexdigest() if body is not None else EMPTY_SHA256

    headers = {
        "host": HOST,
        "x-amz-content-sha256": payload_hash,
        "x-amz-date": amz_date,
    }
    if content_type:
        headers["content-type"] = content_type

    signed_headers = ";".join(sorted(headers))
    canonical_headers = "".join(f"{name}:{headers[name]}\n" for name in sorted(headers))
    canonical_request = "\n".join([
        method, f"/{KEY}", "", canonical_headers, signed_headers, payload_hash,
    ])

    scope = f"{date_stamp}/{REGION}/s3/aws4_request"
    string_to_sign = "\n".join([
        "AWS4-HMAC-SHA256", amz_date, scope,
        hashlib.sha256(canonical_request.encode("utf-8")).hexdigest(),
    ])

    signing_key = _sign(f"AWS4{secret}".encode("utf-8"), date_stamp)
    for part in (REGION, "s3", "aws4_request"):
        signing_key = _sign(signing_key, part)
    signature = hmac.new(signing_key, string_to_sign.encode("utf-8"),
                         hashlib.sha256).hexdigest()

    headers["Authorization"] = (
        f"AWS4-HMAC-SHA256 Credential={key_id}/{scope}, "
        f"SignedHeaders={signed_headers}, Signature={signature}"
    )
    request = urllib.request.Request(f"https://{HOST}/{KEY}", data=body, method=method)
    for name, value in headers.items():
        request.add_header(name, value)
    return request


def s3_get() -> bytes:
    with urllib.request.urlopen(signed_request("GET"), timeout=120) as response:
        return response.read()


def s3_put(body: bytes, content_type: str = "application/json") -> int:
    request = signed_request("PUT", body=body, content_type=content_type)
    with urllib.request.urlopen(request, timeout=300) as response:
        return response.status


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #

def fetch_public() -> tuple[int, bytes]:
    with urllib.request.urlopen(PUBLIC_URL, timeout=90) as response:
        return response.status, response.read()


def check(body: bytes) -> tuple[bool, str]:
    """Is this a catalogue we are happy to serve?"""
    try:
        document = json.loads(body.decode("utf-8"))
    except Exception as exc:
        return False, f"not valid JSON: {exc}"
    groups = len(document.get("catalog") or [])
    if groups < MIN_GROUPS:
        return False, f"only {groups} top-level groups, expected at least {MIN_GROUPS}"
    missing = [name for name in REQUIRED if name.encode() not in body]
    if missing:
        return False, f"missing: {', '.join(missing)}"
    return True, f"{groups} groups, both tools present"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true",
                        help="actually upload; without it nothing is written")
    args = parser.parse_args()

    if not SOURCE.exists():
        print(f"source catalogue not found: {SOURCE}")
        return 1
    new_bytes = SOURCE.read_bytes()
    ok, detail = check(new_bytes)
    print(f"source: {SOURCE.name}, {len(new_bytes)} bytes, {detail}")
    if not ok:
        print("refusing to publish a catalogue that fails its own check")
        return 1

    try:
        live_bytes = s3_get()
    except urllib.error.HTTPError as exc:
        print(f"could not read the live object: HTTP {exc.code} {exc.reason}")
        print("check the credentials, then try again")
        return 1
    print(f"live object: {len(live_bytes)} bytes, "
          f"md5 {hashlib.md5(live_bytes).hexdigest()}")

    if not args.publish:
        print("\ndry run. Nothing was written. Re-run with --publish to upload.")
        return 0

    backup = BACKUP_DIR / f"limpopo_dt_prod.backup-{time.strftime('%Y%m%d-%H%M%S')}.json"
    backup.write_bytes(live_bytes)
    print(f"backup written: {backup}")

    try:
        status = s3_put(new_bytes)
    except urllib.error.HTTPError as exc:
        print(f"upload failed: HTTP {exc.code} {exc.reason}")
        print(f"nothing changed; the live catalogue is untouched, backup at {backup}")
        return 1
    print(f"uploaded (HTTP {status})")

    # Verify over the public URL, the way the portal fetches it.
    verified = False
    for attempt in range(6):
        time.sleep(4)
        try:
            code, body = fetch_public()
            ok, detail = check(body)
            print(f"public GET {code}: {len(body)} bytes, {detail}")
            if ok:
                verified = True
                break
        except Exception as exc:
            print(f"public GET attempt {attempt + 1} failed: {exc!r}")

    if verified:
        print("\nPublished. The portal will pick it up on a hard refresh.")
        return 0

    s3_put(live_bytes)
    print("\nVerification failed. Rolled back to the previous catalogue.")
    print(f"The copy that failed is still at {SOURCE}")
    return 1


CREDENTIALS = ("", "")

if __name__ == "__main__":
    CREDENTIALS = credentials()
    sys.exit(main())
