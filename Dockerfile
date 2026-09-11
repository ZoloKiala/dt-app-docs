# Serves the pre-built, versioned MkDocs site (public/) as static files.
# public/ is produced from the `gh-pages` branch (mike output): v1/, v2/,
# latest/ and versions.json, with a root index.html that redirects to latest/.
FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
COPY public /srv
