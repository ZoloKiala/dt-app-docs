"""Point the portal's WaterCopilot panel at a working URL.

The panel is an iframe whose address is baked in at build time. The value
currently shipped, https://digitaltwins.demos-only.iwmi.org/watercopilot_dev,
has no DNS record, so the browser shows a broken-document placeholder.

This updates the environment file for future builds and patches the already
built bundle, so the running server picks it up without a rebuild.

    python tools/fix_copilot_url.py            # dry run, changes nothing
    python tools/fix_copilot_url.py --apply    # write the change
    python tools/fix_copilot_url.py --apply --url https://water-copilot.digitaltwins.iwmi.org

Works the same in PowerShell, cmd or bash: no shell quoting involved.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / "dt-app" / "dt_limpopo"
ENV_FILE = APP / ".env"
BUNDLE_GLOB = "wwwroot/build/index_js-*.TerriaMap.js"

DEAD_URL = "https://digitaltwins.demos-only.iwmi.org/watercopilot_dev"
STAGING = "https://water-copilot.staging.digitaltwins.iwmi.org"
PRODUCTION = "https://water-copilot.digitaltwins.iwmi.org"


def patch(path: Path, old: str, new: str, apply: bool) -> int:
    """Replace every occurrence, returning how many there were."""
    with open(path, encoding="utf-8", errors="surrogateescape", newline="") as handle:
        text = handle.read()
    count = text.count(old)
    if count and apply:
        backup = path.with_suffix(path.suffix + ".bak")
        if not backup.exists():
            shutil.copy2(path, backup)
        with open(path, "w", encoding="utf-8", errors="surrogateescape",
                  newline="") as handle:
            handle.write(text.replace(old, new))
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true",
                        help="write the change; without it nothing is modified")
    parser.add_argument("--url", default=STAGING,
                        help=f"copilot URL to use (default {STAGING})")
    parser.add_argument("--old", default=DEAD_URL,
                        help="URL to replace")
    args = parser.parse_args()

    if not APP.exists():
        print(f"cannot find the app at {APP}")
        return 1

    print(f"replacing {args.old}")
    print(f"     with {args.url}")
    print(f"     mode {'APPLY' if args.apply else 'dry run'}\n")

    targets = []
    if ENV_FILE.exists():
        targets.append(ENV_FILE)
    targets.extend(sorted(APP.glob(BUNDLE_GLOB)))
    if not targets:
        print("nothing to patch: no .env and no built bundle found")
        return 1

    total = 0
    for path in targets:
        count = patch(path, args.old, args.url, args.apply)
        total += count
        state = "patched" if (count and args.apply) else ("would patch" if count else "no match")
        print(f"  {state:12} {count:>2}  {path.relative_to(ROOT)}")

    if not total:
        print("\nThe old URL was not found. It may already be fixed, "
              "or the build predates it. Check with --old <the URL you see>.")
        return 1

    if args.apply:
        print(f"\nDone, {total} occurrences. Hard-refresh the portal "
              "(Ctrl+F5) and reopen the WaterCopilot panel.")
        print("Backups were written next to each file as *.bak")
    else:
        print(f"\n{total} occurrences would change. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
