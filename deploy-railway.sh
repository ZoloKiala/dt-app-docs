#!/usr/bin/env bash
# Rebuild the versioned site and deploy it to Railway.
#
# Serves the mike output (the `gh-pages` branch) as static files via Caddy.
# `public/` is generated here and must NOT be committed (it is ~90 MB) — but it
# also must NOT be in .gitignore, because `railway up` skips gitignored paths.
set -euo pipefail

# 1) (Re)build the versioned site onto gh-pages first, e.g.:
#      mike deploy --update-aliases v2 latest
#    then run this script.

# 2) Materialise gh-pages into public/ (Windows-safe: no symlinks).
#    tar fails to create the `latest` symlink on Windows; that's expected, so we
#    tolerate it here and recreate `latest` as a real copy below.
rm -rf public && mkdir -p public
git archive gh-pages | tar -x -C public || true
# `latest` is a mike symlink to the default version; copy it for static hosting.
rm -rf public/latest
default_ver=$(python -c "import json;d=json.load(open('public/versions.json'));print(next((v['version'] for v in d if 'latest' in v.get('aliases',[])), d[0]['version']))")
cp -r "public/$default_ver" public/latest

# 3) Deploy.
railway up --service dt-limpopo-docs --detach
echo "Deployed. URL: https://dt-limpopo-docs-production.up.railway.app"
