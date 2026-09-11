---
title: Release Notes
---

# Release Notes

What changed between the portal documented by the **v1** guide (TerriaMap
`0.1.2` / TerriaJS `8.7.1`, August 2024) and the portal now running at
[limpopo.digitaltwins.iwmi.org](https://limpopo.digitaltwins.iwmi.org/).

!!! info "Source"
    Compiled from `dt_limpopo/CHANGES.md` in
    [iwmihq/dt-app](https://github.com/iwmihq/dt-app) and from the live
    deployment's `version.json`. Entries are the upstream TerriaMap releases;
    each one pulls in a TerriaJS upgrade.

## Currently deployed

| Field | Value |
| --- | --- |
| Portal | <https://limpopo.digitaltwins.iwmi.org/> |
| Staging | <https://limpopo.staging.digitaltwins.iwmi.org/> |
| TerriaMap | `0.4.1` |
| TerriaJS | `8.9.5` |
| Build date | 2026-05-15 |

## What this means for users

The changes that are visible while using the portal:

- **The interface was redesigned.** TerriaMap `0.4.0` brought "a new look UI
  with changes to workbench and other panels". The
  [Workbench](../guide/workbench.md) and surrounding panels do not look the
  same as in v1.
- **Basemap choices changed.** The Carto basemaps — *positron*, *dark matter*
  and *black marble* — were removed from the defaults, because they now
  require a commercial Carto licence. **OpenStreetMap** was added as a default
  basemap in their place.
- **More data formats can be added.** The catalogue gained support for
  **I3S** (indexed 3D scene layers) and **COG** (cloud-optimised GeoTIFF), so
  more external services can be brought in via
  [Add Web Data](../guide/my-data.md#adding-web-data).
- **ArcGIS layers draw faster.** ArcGIS feature services now support tiling,
  enabled automatically where the server supports it.
- **Rendering fixes.** Several GeoJSON and region-mapping bugs that could
  leave features undrawn were fixed.

## Version history

### 0.4.1 — 2025-04-24

- TerriaJS `8.9.3`, containing a fix for region mapping and GeoJSON rendering.

### 0.4.0 — 2025-04-04

- TerriaJS `8.9.2`. **Breaking change.**
    - **New look UI**, with changes to the workbench and other panels.
    - Tiling support for ArcGIS feature services, enabled by default where the
      server supports it and unsupported marker/point styles are not used.
    - Fixed a regression in GeoJSON rendering that left some features
      undrawn.

### 0.3.0 — 2025-02-18

- TerriaJS `8.8.0`. **Breaking change**, but internal to the build:
  Webpack 5, Sass 1.80+, and a conversion from CommonJS to ESM modules. No
  user-facing change.

### 0.2.4 — 2024-12-19

- TerriaJS `8.7.11`. Added `clampToGround` and `dataSourceUri` to the KML
  catalogue item traits.

### 0.2.3 — 2024-11-29

- TerriaJS `8.7.10`. **OpenStreetMap added as a default basemap.**

### 0.2.2 — 2024-11-22

- TerriaJS `8.7.9`. **Breaking change:** the Carto basemaps *positron*,
  *dark matter* and *black marble* were removed from the default settings, as
  they now require a Carto Enterprise or Grantee licence.
- Added `I3SCatalogItem` and `CogCatalogItem`.

### 0.2.1 — 2024-08-07

- TerriaJS `8.7.5`.

### 0.1.2 — 2024-05-02

- TerriaJS `8.7.1`. **This is the release the [v1 documentation](index.md)
  describes.** The portal build documented there was dated 2024-08-26.

## Deployment

The portal is built and deployed from
[iwmihq/dt-app](https://github.com/iwmihq/dt-app) via GitHub Actions, which
push container images to **Amazon ECR** and deploy them to **Amazon ECS**.

- Branches with a `_prod` suffix deploy to production
  (`dt_limpopo_prod` → Limpopo production); unsuffixed branches are staging.
- Secrets for `dt_limpopo` are stored in GitHub and injected during the image
  build; other services read from AWS Secrets Manager.
- Authentication across the Digital Twin platform is handled by **Keycloak**
  at <https://auth.iwmi.org>.

See [Deployment & Maintenance](../project/deployment.md) for more.
