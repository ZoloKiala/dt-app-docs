---
title: Use Cases
---

# Use Cases

The [User Guide](../guide/index.md) explains what each control does. These
pages show how to **answer a real question** with the portal, end to end — which
datasets to open, in what order, and how to read what you see.

Every dataset named here exists in the portal's catalogue today. Names are
written exactly as they appear in **Explore data**, so you can find them with
**Search the catalogue**.

<div class="grid cards" markdown>

-   :material-sprinkler-variant: **[Irrigation water use monitoring](irrigation.md)**

    Where is irrigation expanding, and how much water does it consume?

-   :material-waves: **[Floods](floods.md)**

    Is a flood developing, where will it peak, and who is exposed?

-   :material-weather-sunny-alert: **[Droughts](droughts.md)**

    How stressed are vegetation, soils and rivers, and what is the outlook?

-   :material-fish: **[Environmental flows](eflows.md)**

    Are rivers receiving the flow their ecosystems need?

-   :material-water-check: **[Reservoir monitoring](reservoirs.md)**

    How full are the dams, and how are levels trending?

-   :material-scale-balance: **[Water accounting](water-accounting.md)**

    Where does the basin's water come from, and where does it go?

</div>

## How each use case is written

| Section | What it gives you |
| --- | --- |
| **The question** | Who is asking, the decision they need to make, and how often they look |
| **At a glance** | The headline numbers for the basin today, taken from the portal's own data API |
| **How the workflow fits together** | A flow diagram of the datasets and decision points |
| **Data you will use** | The exact catalogue datasets, where they live, and what each one tells you |
| **Walkthrough** | Numbered steps using the portal's own button labels |
| **Reading the charts** | Real charts built from the same series the portal shows when you click a station or dam, with what to look for |
| **Indicators and what to do** | Thresholds and the action they normally trigger |
| **Worked example** | The workflow applied to a real situation, with the numbers |
| **Checklist** | What a report from this analysis should contain |
| **Limits to keep in mind** | Latency, model assumptions and coverage caveats — so you don't over-read the data |

!!! info "About the charts"
    The charts on these pages are the portal's own: screenshots of the
    **Feature Information** card and of the **Charts** dock (the panel's
    **Expand** button) for real stations, dams and sites, captured from the
    production catalogue in September 2026. Where longer-term context helps, a
    collapsed block adds charts rendered from the same API series
    (`api.digitaltwins.iwmi.org`) — those are labelled as derived, not portal
    screens. Workflow diagrams and indicator tables are guidance, not official
    operating rules; check thresholds against your institution's procedures.

!!! tip "Save your analysis as a Story"
    Once you have a view that answers your question, use **Story → Capture
    Scene** to record the layers, time and camera, then **Share / Print** to hand
    colleagues a single link that reproduces it. See
    [Stories & Sharing](../guide/sharing.md).

!!! note "Some charts need a signed-in session"
    Station and site charts (discharge, rainfall, e-flow, reservoir forecasts)
    are served by the IWMI data API and require you to be signed in. Map layers
    work regardless.
