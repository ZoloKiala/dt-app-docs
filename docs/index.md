---
title: Home
---

# Limpopo Digital Twin Portal

Documentation for the **TerriaJS portal showcasing the Digital Twin (DT) of the
Limpopo River Basin**, developed for the International Water Management
Institute (IWMI).

!!! abstract "About this documentation"
    This site is the web edition of *DT_03 — User Guide: TerriaJS Digital Twin*
    (August 2024). It covers what the portal is, how it was built, and how to
    use every feature of its interface.

!!! tip "Open the portal"
    The live portal is at
    **[limpopo.digitaltwins.iwmi.org](https://limpopo.digitaltwins.iwmi.org/)**
    — TerriaMap `0.4.1` / TerriaJS `8.9.5`, built 2026-05-15. See
    [Release Notes](reference/release-notes.md) for what changed since the 2024
    release, or pick **v1** in the version selector for the older guide.

!!! warning "Screenshots are being re-captured"
    TerriaMap `0.4.0` redesigned the interface, changing the workbench and
    other panels. The screenshots in this guide still come from the 2024
    portal, so some panels will not look exactly as shown. The described
    workflows still apply; the images are being refreshed.

## What the portal does

The WebGIS Portal (Phase 2) is an advanced geospatial web portal that
visualises and lets you interact with spatial datasets relevant to the Limpopo
River basin. It features a Digital Twin of the basin, aggregating and
interpolating data from satellite imagery, in-situ sensors and numerical model
outputs.

Phase 2 builds on the foundation established in Phase 1, using the
[TerriaJS](https://terria.io/) framework — an open-source platform for
web-based geospatial catalogue exploration. The portal draws inspiration from
platforms such as Digital Earth Africa (DE Africa) and NationalMap.

<figure markdown="span">
  ![The homepage of the TerriaJS framework](assets/images/image1.png)
  <figcaption>Figure 1: The homepage of the TerriaJS framework.</figcaption>
</figure>

## Start here

<div class="grid cards" markdown>

-   :material-rocket-launch: **New to the portal?**

    Open the map, search for a location and add your first dataset.

    [:octicons-arrow-right-24: Getting Started](guide/getting-started.md)

-   :material-database-search: **Looking for data?**

    Browse the thematic catalogue and preview datasets before adding them.

    [:octicons-arrow-right-24: Data Catalogue](guide/data-catalogue.md)

-   :material-upload: **Have your own data?**

    Drag and drop local files, or connect a WMS/WFS web service.

    [:octicons-arrow-right-24: My Data](guide/my-data.md)

-   :material-cog: **Want the technical picture?**

    Architecture, data sources, development process and deployment.

    [:octicons-arrow-right-24: Project](project/index.md)

</div>

## Key capabilities at a glance

| Capability | What it gives you |
| --- | --- |
| Geospatial visualisation | Interactive 2D and 3D views of basin data |
| Thematic data catalogue | Curated datasets across five thematic categories |
| Time series analysis | Explore change over time with a timeline slider |
| Workbench | Toggle, restyle, reorder and compare active layers |
| My Data | Add local files or web services without uploading them |
| Stories | Capture scenes into a narrative you can share |
| Share & print | Shareable URLs, PNG export and printable views |
| AI-driven chatbot | Assistance with queries and navigation |

## Conclusion of the source report

The WebGIS Portal represents a significant advancement in geospatial data
visualisation for IWMI. Built on the robust TerriaJS framework, it integrates
diverse datasets and provides an intuitive interface for exploring the Limpopo
River basin — supporting informed decision-making in water resource management
across the basin.

## Contact

For help with the portal, or for questions about the datasets it publishes,
contact the IWMI geospatial team at
[iwmigeospatial@gmail.com](mailto:iwmigeospatial@gmail.com), or use the
[Feedback form](guide/help-support.md#feedback) built into the portal.
