"""
One-off: replace the "Reading the charts" sections of the use-case pages with the
portal's own feature-info charts (screenshots in docs/assets/charts/portal/),
keeping the derived API charts in a collapsed block.
"""
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs" / "use-cases"
P = "../assets/charts/portal/"
C = "../assets/charts/"


def fig(src, caption):
    return f'<figure markdown="span">\n  ![{caption.split(":")[0]}]({src})\n  <figcaption>{caption}</figcaption>\n</figure>\n'


def collapsed(title, intro, items):
    body = f"    {intro}\n\n"
    for src, cap in items:
        body += f'    <figure markdown="span">\n      ![{cap.split(":")[0]}]({src})\n      <figcaption>{cap}</figcaption>\n    </figure>\n\n'
    return f'??? note "{title}"\n{body}'


EN_INTRO = ("The figures below are the portal's own charts, captured from the **Feature Information** panel "
            "(click a feature) and from the **Charts** dock that opens with the panel's **Expand** button. "
            "Every station, dam and site chart in the portal follows the same pattern: a summary card, a preview "
            "chart, **Expand** to enlarge, **Download** for the CSV.")
PT_INTRO = ("As figuras abaixo são os gráficos do próprio portal, capturados no painel **Feature Information** "
            "(clique num elemento) e no painel **Charts** que abre com o botão **Expand**. Todos os gráficos de "
            "estações, barragens e locais seguem o mesmo padrão: um cartão-resumo, um gráfico de pré-visualização, "
            "**Expand** para ampliar, **Download** para o CSV. Os gráficos estão em inglês.")

EN_COLL = "Longer-term context (charts derived from the same API data)"
PT_COLL = "Contexto de longo prazo (gráficos derivados dos mesmos dados da API)"
EN_COLL_INTRO = ("These are not portal screens: they were rendered from the same series with `tools/use_case_charts.py` "
                 "to show what the portal's series look like over decades.")
PT_COLL_INTRO = ("Estes não são ecrãs do portal: foram gerados a partir das mesmas séries com `tools/use_case_charts.py` "
                 "para mostrar como as séries do portal se comportam ao longo de décadas.")

PAGES = {}

# ------------------------------------------------------------------ floods
PAGES["floods"] = {
    "en": (
        fig(P + "glofas-gauge-a7h004-panel.png",
            "Figure 1: Feature Information for gauge A7H004, Limpopo River at Beit Bridge (GloFAS Discharge Forecast – Verified Gauges). The card gives the 24 h, 72 h and 30-day forecasts, the flow status, the linked SWAT channel and the model run; the preview chart shows the current year.") +
        "- **Read the three numbers first**: 24.6 → 34.4 → 24.0 m³/s means a small rise this week, then recession — *Moderate* status, no alert. In the wet season the same card can read 500 → 1,500 → 900.\n"
        "- **Model run** is the date to quote in a situation report; **Linked SWAT** (cha0215) is the channel to open in the SWAT Extraction Tool.\n"
        "- The preview chart shows this year's daily flow: the two peaks near 1,500 m³/s (February and late March 2026) are the wet-season pulses that shape the annual maxima history.\n\n" +
        fig(P + "glofas-gauge-a7h004-chart.png",
            "Figure 2: The same gauge after Expand — the Charts dock with the full GloFAS record since 1979. Each colour is a forecast lead time; the orange series is the reanalysis.") +
        "- The dock shows **every archived forecast and the reanalysis** on one axis: the 2000 (≈7,000 m³/s), 2013 and 2025 (≈5,000 m³/s) floods stand out immediately.\n"
        "- Hover a point to read the value and date; drag to zoom into a season; **Download** gives the CSV with one column per lead time.\n"
        "- Compare the current year's forecast spikes (right edge) against those historical peaks to judge severity — a forecast of 2,500 m³/s at Beit Bridge is a top-ten event.\n\n" +
        fig(P + "glofas-swat-cha0978-panel.png",
            "Figure 3: The same template for a SWAT channel (GloFAS Discharge Forecast – SWAT Channels), here cha0978 on the Crocodile. Channel geometry (stream order, drained area, width, depth) helps judge whether a forecast discharge will overtop the banks.") +
        "- Channel points fill the gaps between gauges: 1,436 channels versus 363 gauges. A **channel 8.6 m deep and 696 m wide** carries 19 m³/s without notice; a first-order tributary would not.\n"
        "- **30D forecast 2.4 m³/s** against 19 m³/s today shows the dry-season recession — the forecast is for the flow to fall.\n\n" +
        fig(P + "rainfall-forecast-ingwizi-panel.png",
            "Figure 4: Rainfall Monitoring and Forecast station card (s20592s27943e, channel cha0036, upper Shashe): last 7 and 30 days, wet days, 7-day forecast and last rain, with the daily rainfall preview.") +
        "- This is the **trigger layer** for the flood workflow: when *7-day forecast* jumps to tens of millimetres over headwater channels, open the GloFAS points downstream.\n"
        "- Expand shows daily rainfall since 2020 with the forecast in green — the wet-season clusters (Dec–Feb) are where flood peaks originate.\n\n" +
        collapsed(EN_COLL, EN_COLL_INTRO, [
            (C + "floods-annual-maxima.png", "Annual peak discharge at Beit Bridge 1979–2026 with the station's p95/p99 thresholds."),
            (C + "floods-glofas-forecast.png", "The current 30-day outlook at Beit Bridge against the station thresholds."),
            (C + "floods-basin-status.png", "How the 876 forecast points were classified on 13 September 2026."),
        ])
    ),
    "pt": (
        fig(P + "glofas-gauge-a7h004-panel.png",
            "Figura 1: Feature Information da estação A7H004, rio Limpopo em Beit Bridge (GloFAS Discharge Forecast – Verified Gauges). O cartão dá as previsões a 24 h, 72 h e 30 dias, o estado do caudal, o canal SWAT associado e a corrida do modelo; a pré-visualização mostra o ano corrente.") +
        "- **Leia primeiro os três números**: 24,6 → 34,4 → 24,0 m³/s significa uma pequena subida esta semana e depois recessão — estado *Moderate*, sem alerta. Na época das chuvas o mesmo cartão pode ler 500 → 1 500 → 900.\n"
        "- **Model run** é a data a citar num relatório de situação; **Linked SWAT** (cha0215) é o canal a abrir na SWAT Extraction Tool.\n"
        "- A pré-visualização mostra o caudal diário deste ano: os dois picos perto de 1 500 m³/s (fevereiro e fim de março de 2026) são os pulsos da época das chuvas que formam o histórico de máximos anuais.\n\n" +
        fig(P + "glofas-gauge-a7h004-chart.png",
            "Figura 2: A mesma estação após Expand — o painel Charts com o registo GloFAS completo desde 1979. Cada cor é um horizonte de previsão; a série laranja é a reanálise.") +
        "- O painel mostra **todas as previsões arquivadas e a reanálise** num só eixo: as cheias de 2000 (≈7 000 m³/s), 2013 e 2025 (≈5 000 m³/s) destacam-se de imediato.\n"
        "- Passe o cursor sobre um ponto para ler valor e data; arraste para ampliar uma estação; **Download** dá o CSV com uma coluna por horizonte.\n"
        "- Compare os picos previstos do ano corrente (margem direita) com esses máximos históricos para avaliar a severidade — uma previsão de 2 500 m³/s em Beit Bridge é um evento entre os dez maiores.\n\n" +
        fig(P + "glofas-swat-cha0978-panel.png",
            "Figura 3: O mesmo modelo de cartão para um canal SWAT (GloFAS Discharge Forecast – SWAT Channels), aqui cha0978 no Crocodile. A geometria do canal (ordem, área drenada, largura, profundidade) ajuda a avaliar se um caudal previsto galgará as margens.") +
        "- Os pontos de canal preenchem os vazios entre estações: 1 436 canais contra 363 estações. Um **canal com 8,6 m de profundidade e 696 m de largura** transporta 19 m³/s sem consequências; um afluente de primeira ordem não.\n"
        "- **30D forecast 2,4 m³/s** contra 19 m³/s hoje mostra a recessão da época seca — a previsão é de descida do caudal.\n\n" +
        fig(P + "rainfall-forecast-ingwizi-panel.png",
            "Figura 4: Cartão da estação de Rainfall Monitoring and Forecast (s20592s27943e, canal cha0036, alto Shashe): últimos 7 e 30 dias, dias húmidos, previsão a 7 dias e última chuva, com a pré-visualização da chuva diária.") +
        "- É a **camada-gatilho** do fluxo de trabalho de cheias: quando a *previsão a 7 dias* salta para dezenas de milímetros sobre canais de cabeceira, abra os pontos GloFAS a jusante.\n"
        "- Expand mostra a chuva diária desde 2020 com a previsão a verde — os aglomerados da época das chuvas (dez.–fev.) são onde nascem os picos de cheia.\n\n" +
        collapsed(PT_COLL, PT_COLL_INTRO, [
            (C + "floods-annual-maxima.png", "Pico anual de caudal em Beit Bridge 1979–2026 com os limiares p95/p99 da estação."),
            (C + "floods-glofas-forecast.png", "A perspetiva atual a 30 dias em Beit Bridge contra os limiares da estação."),
            (C + "floods-basin-status.png", "Como os 876 pontos de previsão foram classificados em 13 de setembro de 2026."),
        ])
    ),
}

# ------------------------------------------------------------------ droughts
PAGES["droughts"] = {
    "en": (
        fig(P + "rainfall-anomaly-ingwizi-panel.png",
            "Figure 1: Rainfall Anomalies card for channel cha0036 (Ingwizi, upper Shashe): the current month's observed total, the climatological mean, the anomaly in mm and %, its class, plus the last 7 days and 7-day forecast, with the monthly preview chart.") +
        "- **Beware percentage anomalies in the dry season**: 0.4 mm observed against a 0.1 mm mean reads *+300 %, Very wet* — meaningless in August. Judge the class in the **wet-season months (Nov–Mar)**, or read the mm anomaly.\n"
        "- The preview chart shows monthly totals since 2001; the shape of each summer peak (tall and narrow, or low and flat) is the first visual sign of a good or failed season.\n\n" +
        fig(P + "rainfall-anomaly-ingwizi-chart.png",
            "Figure 2: The expanded chart — Total Monthly Rain (orange) and Anomaly (green), 2001–2026.") +
        "- Runs of **green below zero through a whole summer** are the meteorological-drought signal: 2002–03, 2005, 2012, 2015–16 and 2023–24 all show it.\n"
        "- The large positive spikes (Feb 2017, Jan 2021) end meteorological drought in one month; rivers, dams and boreholes take a season or more to follow.\n"
        "- **Download** the CSV to compute a 3- or 12-month running total yourself if you need an SPI-like index for the current season (the SPEI layers stop in 2021).\n\n" +
        fig(P + "rainfall-forecast-ingwizi-chart.png",
            "Figure 3: Rainfall Monitoring and Forecast, expanded — daily rainfall since 2020 (orange) with the 7-day forecast (green) at the same station.") +
        "- Daily data show **dry-spell length** inside a season, which monthly totals hide: the 2023/24 summer has few and small events compared with 2020/21.\n"
        "- The forecast points at the right edge are the sub-seasonal outlook for the station; a flat green tail in November means a late onset.\n\n" +
        fig(P + "eflow-croc-panel.png",
            "Figure 4: E-flow Monitoring and Forecasting site card (CROC-A24J-ROOIB) — the hydrological-drought check. The preview shows modelled flow since 2001; the card names the reach and site.") +
        "- When rainfall and vegetation indices agree on drought, this is the confirmation: flows sitting on or below the requirement line in **Expand** (see [Environmental flows](eflows.md)).\n\n" +
        collapsed(EN_COLL, EN_COLL_INTRO, [
            (C + "droughts-rainfall-anomaly.png", "Monthly rainfall anomaly at Ingwizi as +/- bars."),
            (C + "droughts-annual-rainfall.png", "Annual totals against the 606 mm mean; orange years below 75 % of the mean."),
            (C + "droughts-spi.png", "SPI-3 and SPI-12 at the same station — how to read the SPEI hazard layers."),
        ])
    ),
    "pt": (
        fig(P + "rainfall-anomaly-ingwizi-panel.png",
            "Figura 1: Cartão de Rainfall Anomalies para o canal cha0036 (Ingwizi, alto Shashe): total observado do mês corrente, média climatológica, anomalia em mm e %, a sua classe, mais os últimos 7 dias e a previsão a 7 dias, com a pré-visualização mensal.") +
        "- **Cuidado com anomalias percentuais na época seca**: 0,4 mm observados contra uma média de 0,1 mm lê-se *+300 %, Very wet* — sem significado em agosto. Avalie a classe nos **meses da época das chuvas (nov.–mar.)**, ou leia a anomalia em mm.\n"
        "- A pré-visualização mostra os totais mensais desde 2001; a forma de cada pico de verão (alto e estreito, ou baixo e achatado) é o primeiro sinal visual de uma estação boa ou falhada.\n\n" +
        fig(P + "rainfall-anomaly-ingwizi-chart.png",
            "Figura 2: O gráfico expandido — Total Monthly Rain (laranja) e Anomaly (verde), 2001–2026.") +
        "- Sequências de **verde abaixo de zero ao longo de todo um verão** são o sinal de seca meteorológica: 2002–03, 2005, 2012, 2015–16 e 2023–24 mostram-no.\n"
        "- Os grandes picos positivos (fev. 2017, jan. 2021) terminam a seca meteorológica num mês; rios, barragens e furos demoram uma estação ou mais a acompanhar.\n"
        "- **Download** do CSV permite calcular um total móvel de 3 ou 12 meses para um índice tipo SPI da estação corrente (as camadas SPEI terminam em 2021).\n\n" +
        fig(P + "rainfall-forecast-ingwizi-chart.png",
            "Figura 3: Rainfall Monitoring and Forecast, expandido — chuva diária desde 2020 (laranja) com a previsão a 7 dias (verde) na mesma estação.") +
        "- Os dados diários mostram a **duração dos períodos secos** dentro de uma estação, que os totais mensais escondem: o verão de 2023/24 tem poucos e pequenos eventos em comparação com 2020/21.\n"
        "- Os pontos de previsão na margem direita são a perspetiva subsazonal da estação; uma cauda verde plana em novembro significa início tardio.\n\n" +
        fig(P + "eflow-croc-panel.png",
            "Figura 4: Cartão do local de E-flow Monitoring and Forecasting (CROC-A24J-ROOIB) — a verificação de seca hidrológica. A pré-visualização mostra o caudal modelado desde 2001; o cartão identifica o troço e o local.") +
        "- Quando os índices de chuva e de vegetação concordam na seca, esta é a confirmação: caudais sobre ou abaixo da linha de requisito em **Expand** (ver [Caudais ecológicos](eflows.md)).\n\n" +
        collapsed(PT_COLL, PT_COLL_INTRO, [
            (C + "droughts-rainfall-anomaly.png", "Anomalia mensal de precipitação em Ingwizi como barras +/−."),
            (C + "droughts-annual-rainfall.png", "Totais anuais contra a média de 606 mm; anos laranja abaixo de 75 % da média."),
            (C + "droughts-spi.png", "SPI-3 e SPI-12 na mesma estação — como ler as camadas de perigo SPEI."),
        ])
    ),
}

# ------------------------------------------------------------------ eflows
PAGES["eflows"] = {
    "en": (
        fig(P + "eflow-croc-panel.png",
            "Figure 1: E-flow Monitoring and Forecasting — the site card for CROC-A24J-ROOIB (Crocodile West at Rooibokkraal) with the modelled-flow preview since 2001, Show Raw Data, Advanced Chart, Expand and Download.") +
        "- The card names the **river code** (used by the API and the SWAT Extraction Tool), the reach description and the site; the preview is present-day flow only.\n"
        "- **Advanced Chart** opens the analytics view (regime, compliance, deficit heat-map) for the site in the live portal.\n\n" +
        fig(P + "eflow-croc-chart.png",
            "Figure 2: The same site after Expand — four series: SWAT Present Flow, Natural Flow, Availability Surplus and E-Flow (the requirement), 2001–2026, m³/s.") +
        "- The **E-Flow requirement** (green) is the low, seasonal line at the bottom; present flow (pink) rides above it in most months. Where pink dips **to** the green line in winter, the reach is at Level 2–3.\n"
        "- Wet-season peaks (300–560 m³/s in 2004, 2014, 2017, 2021, 2025) are near natural — this reach is altered in the dry season, not the wet.\n"
        "- Drag across a winter to zoom: the gap between pink and green in m³/s is the deficit the alert message asks the dam operator to release.\n\n" +
        fig(P + "eflow-mapun-chart.png",
            "Figure 3: The Limpopo main stem, Shashe to Mzingwane (LIMP-A71L-MAPUN), expanded. Peaks reach 2,500 m³/s (2021) while the requirement stays below ~120 m³/s.") +
        "- On a main-stem site the wet-season peaks dwarf everything else; **zoom into the dry months** to see the deficits, or read the *Deficit* series in **Show Raw Data**.\n"
        "- Compare with Figure 2: the same requirement logic, an order of magnitude more water.\n\n" +
        fig(P + "glofas-swat-cha0978-panel.png",
            "Figure 4: The SWAT channel card for cha0978 — the Crocodile channel that feeds the e-flow site. Its Channel ID is what you type into the SWAT Extraction Tool (Flow Type, Start/End Date, FETCH DATA → MAP / TABLE / PROBFLO).") +
        "- Channel geometry (stream order 4, 3.58 million ha drained) tells you how much upstream catchment — and abstraction — sits behind the site.\n\n" +
        collapsed(EN_COLL, EN_COLL_INTRO, [
            (C + "eflows-regime-croc.png", "Monthly regime at the Crocodile site: natural vs present flow and the e-flow requirement."),
            (C + "eflows-timeseries-mapun.png", "Present flow vs requirement at LIMP-A71L-MAPUN since 2015 with deficit months shaded (log axis)."),
            (C + "eflows-compliance.png", "Annual e-flow compliance at the two sites."),
        ])
    ),
    "pt": (
        fig(P + "eflow-croc-panel.png",
            "Figura 1: E-flow Monitoring and Forecasting — o cartão do local CROC-A24J-ROOIB (Crocodile West em Rooibokkraal) com a pré-visualização do caudal modelado desde 2001, Show Raw Data, Advanced Chart, Expand e Download.") +
        "- O cartão identifica o **código do rio** (usado pela API e pela SWAT Extraction Tool), a descrição do troço e o local; a pré-visualização é só o caudal presente.\n"
        "- **Advanced Chart** abre a vista analítica (regime, conformidade, mapa de calor de défices) do local no portal em produção.\n\n" +
        fig(P + "eflow-croc-chart.png",
            "Figura 2: O mesmo local após Expand — quatro séries: SWAT Present Flow, Natural Flow, Availability Surplus e E-Flow (o requisito), 2001–2026, m³/s.") +
        "- O **requisito E-Flow** (verde) é a linha baixa e sazonal em baixo; o caudal presente (rosa) fica acima na maioria dos meses. Onde o rosa desce **até** à linha verde no inverno, o troço está em Nível 2–3.\n"
        "- Os picos da época das chuvas (300–560 m³/s em 2004, 2014, 2017, 2021, 2025) são quase naturais — este troço está alterado na época seca, não na húmida.\n"
        "- Arraste sobre um inverno para ampliar: a diferença entre rosa e verde em m³/s é o défice que a mensagem de alerta pede ao operador da barragem para descarregar.\n\n" +
        fig(P + "eflow-mapun-chart.png",
            "Figura 3: O curso principal do Limpopo, Shashe a Mzingwane (LIMP-A71L-MAPUN), expandido. Os picos atingem 2 500 m³/s (2021) enquanto o requisito fica abaixo de ~120 m³/s.") +
        "- Num local do curso principal os picos da época das chuvas ofuscam tudo o resto; **amplie os meses secos** para ver os défices, ou leia a série *Deficit* em **Show Raw Data**.\n"
        "- Compare com a Figura 2: a mesma lógica de requisito, uma ordem de grandeza mais água.\n\n" +
        fig(P + "glofas-swat-cha0978-panel.png",
            "Figura 4: O cartão do canal SWAT cha0978 — o canal do Crocodile que alimenta o local de caudal ecológico. O seu Channel ID é o que se introduz na SWAT Extraction Tool (Flow Type, Start/End Date, FETCH DATA → MAP / TABLE / PROBFLO).") +
        "- A geometria do canal (ordem 4, 3,58 milhões de ha drenados) indica quanta bacia a montante — e quanta captação — está por trás do local.\n\n" +
        collapsed(PT_COLL, PT_COLL_INTRO, [
            (C + "eflows-regime-croc.png", "Regime mensal no local do Crocodile: caudal natural vs presente e requisito de caudal ecológico."),
            (C + "eflows-timeseries-mapun.png", "Caudal presente vs requisito em LIMP-A71L-MAPUN desde 2015 com meses em défice sombreados (eixo log)."),
            (C + "eflows-compliance.png", "Conformidade anual de caudal ecológico nos dois locais."),
        ])
    ),
}

# ------------------------------------------------------------------ reservoirs
PAGES["reservoirs"] = {
    "en": (
        fig(P + "dam-massingir-panel.png",
            "Figure 1: Dams & Reservoirs Basin Level Estimates — the Massingir card: current level 90.2 %, latest estimated volume 2,038 Mm³, status Full, capacity 2,260 Mm³, dam height, reservoir area, catchment, year built, mean and min/max volume, the estimation model (altimetry_level) and its R² (0.9974), with the storage preview.") +
        "- **Model and R²** are the confidence check: *altimetry_level* with R² 0.997 is Tier 1; a *capacity_fraction* dam with no R² is a Tier 3 estimate (± 20 %).\n"
        "- **Min / max 83.9 – 2,485 Mm³** frames the history: the dam has been effectively empty (2003, 2005) and above full supply (2008).\n"
        "- **Expand ▾** offers four series — Estimated Volume, Observed Volume, % Capacity, Area; **Download this Table** gives the CSV.\n\n" +
        fig(P + "dam-massingir-chart.png",
            "Figure 2: Massingir after Expand → Estimated Volume: volume (Mm³, left axis) and % of capacity (second axis) since 2002, with the observed points overlaid.") +
        "- Where the estimate (blue) and observations (orange) coincide the model is calibrated; the straight segments (2010–13, 2016–19) are **gaps with no observations** — read them as trend only.\n"
        "- The annual saw-tooth since 2021 is the operating cycle: fill to 100–105 % in March, draw down to ~65–75 % by November for Chókwè irrigation.\n\n" +
        fig(P + "reservoir-area-massingir-chart.png",
            "Figure 3: Reservoir Levels – Water Area Timeseries for Massingir Dam, expanded: satellite water area (ha, blue) with observed volume (Mm³) and observed capacity fraction where a gauge record exists.") +
        "- The **water-area series continues after the gauge record ends (2019)** — this is how the portal monitors dams with no telemetry: area from satellite, converted to volume by the calibrated curve.\n"
        "- Area and volume move together but not proportionally (a flat reservoir loses area quickly at low levels); that non-linearity is the area–capacity curve the Tier 1 model encodes.\n\n" +
        fig(P + "dam-loskop-chart.png",
            "Figure 4: Loskop Dam (Olifants), Expand → Estimated Volume, 2016–2026 (Mm³ and %).") +
        "- Three drawdowns stand out: **2016 (to ~150 Mm³, 42 %)**, 2019 (~250 Mm³) and late 2024 (~250 Mm³) — each the end of a dry season before the summer refill.\n"
        "- The flat top at ~350–365 Mm³ is full supply; values above it are spill periods. This is the chart to read against the seasonal band in the collapsed section below.\n\n" +
        collapsed(EN_COLL, EN_COLL_INTRO, [
            (C + "reservoirs-massingir-storage.png", "Massingir storage in % of capacity since 2002 with the ensemble forecast to November 2026."),
            (C + "reservoirs-by-country.png", "Capacity and current storage of monitored dams by country."),
            (C + "reservoirs-loskop-seasonal.png", "Loskop's storage by calendar month across all years — the normal band."),
        ])
    ),
    "pt": (
        fig(P + "dam-massingir-panel.png",
            "Figura 1: Dams & Reservoirs Basin Level Estimates — o cartão de Massingir: nível atual 90,2 %, último volume estimado 2 038 Mm³, estado Full, capacidade 2 260 Mm³, altura da barragem, área da albufeira, bacia, ano de construção, volume médio e mín./máx., o modelo de estimativa (altimetry_level) e o seu R² (0,9974), com a pré-visualização do armazenamento.") +
        "- **Modelo e R²** são a verificação de confiança: *altimetry_level* com R² 0,997 é Nível 1; uma barragem *capacity_fraction* sem R² é uma estimativa de Nível 3 (± 20 %).\n"
        "- **Mín. / máx. 83,9 – 2 485 Mm³** enquadra o histórico: a barragem já esteve praticamente vazia (2003, 2005) e acima do pleno armazenamento (2008).\n"
        "- **Expand ▾** oferece quatro séries — Estimated Volume, Observed Volume, % Capacity, Area; **Download this Table** dá o CSV.\n\n" +
        fig(P + "dam-massingir-chart.png",
            "Figura 2: Massingir após Expand → Estimated Volume: volume (Mm³, eixo esquerdo) e % da capacidade (segundo eixo) desde 2002, com os pontos observados sobrepostos.") +
        "- Onde a estimativa (azul) e as observações (laranja) coincidem o modelo está calibrado; os segmentos retos (2010–13, 2016–19) são **lacunas sem observações** — leia-os apenas como tendência.\n"
        "- O dente de serra anual desde 2021 é o ciclo de operação: enche até 100–105 % em março, baixa até ~65–75 % em novembro para a irrigação de Chókwè.\n\n" +
        fig(P + "reservoir-area-massingir-chart.png",
            "Figura 3: Reservoir Levels – Water Area Timeseries para a barragem de Massingir, expandido: área de água por satélite (ha, azul) com volume observado (Mm³) e fração de capacidade observada onde existe registo de estação.") +
        "- A **série de área de água continua depois de terminar o registo da estação (2019)** — é assim que o portal monitoriza barragens sem telemetria: área por satélite, convertida em volume pela curva calibrada.\n"
        "- Área e volume movem-se juntos mas não proporcionalmente (uma albufeira plana perde área depressa a níveis baixos); essa não-linearidade é a curva área–capacidade que o modelo de Nível 1 codifica.\n\n" +
        fig(P + "dam-loskop-chart.png",
            "Figura 4: Barragem de Loskop (Olifants), Expand → Estimated Volume, 2016–2026 (Mm³ e %).") +
        "- Destacam-se três esvaziamentos: **2016 (até ~150 Mm³, 42 %)**, 2019 (~250 Mm³) e fim de 2024 (~250 Mm³) — cada um o fim de uma época seca antes do reenchimento de verão.\n"
        "- O patamar plano a ~350–365 Mm³ é o pleno armazenamento; valores acima são períodos de descarga de superfície. É este o gráfico a ler contra a faixa sazonal na secção recolhida abaixo.\n\n" +
        collapsed(PT_COLL, PT_COLL_INTRO, [
            (C + "reservoirs-massingir-storage.png", "Armazenamento de Massingir em % da capacidade desde 2002 com a previsão por conjunto até novembro de 2026."),
            (C + "reservoirs-by-country.png", "Capacidade e armazenamento atual das barragens monitorizadas por país."),
            (C + "reservoirs-loskop-seasonal.png", "Armazenamento de Loskop por mês do calendário em todos os anos — a faixa normal."),
        ])
    ),
}

# ------------------------------------------------------------------ water accounting
PAGES["water-accounting"] = {
    "en": (
        fig(P + "wa-dashboard-panel.png",
            "Figure 1: Limpopo Basin Water Balance (WA+ Dashboard) — the basin marker's card, with Show Raw Data, Advanced Chart and Balance Dashboard buttons. The Balance Dashboard opens the compiled WA+ accounts (resource-base sheet as a Sankey) in the live portal.") +
        "- This single marker is the entry point to the accounts: **Balance Dashboard** for the sheets, **Download** for the monthly CSV of every term since 2003.\n\n" +
        fig(P + "wa-dashboard-chart.png",
            "Figure 2: The WA+ site after Expand — every term of the monthly balance (some 35 series: inflows, ET by land-use class, outflows, storage change) on one axis, 2003–2021.") +
        "- The dock plots **all terms at once**, which is only useful for spotting the seasonal rhythm: the pink rainfall inflow peaks each summer; the yellow/orange ET terms follow one to two months later.\n"
        "- Turn series off in the legend to isolate a term — e.g. keep *Inflow Precipitation Rainfall* and *Outflow ET Landscape Utilized* to see that in dry summers ET exceeds rain.\n"
        "- For analysis use **Download** (one column per term) or the **Balance Dashboard**; the collapsed section below shows what the annual totals look like.\n\n" +
        fig(P + "realtime-station-a2h012-panel.png",
            "Figure 3: SWAT and Observed Sites — the card for gauge A2H012FW (Krokodil at Kalkheuwel): status, latest discharge (16.55 m³/s on 2 Sep 2026) and an Advanced Chart button. Gauges like this are the ground truth the accounts are validated against.") +
        "- Observed discharge at the basin's gauges is the **outflow term** measured, not modelled; where it disagrees with the WA+ outflow, the account needs adjusting.\n\n" +
        collapsed(EN_COLL, EN_COLL_INTRO, [
            (C + "wa-annual-balance.png", "Rainfall, total ET and outflow by year, 2003–2024 (km³/yr)."),
            (C + "wa-et-by-landuse.png", "Share of basin ET by WA+ land-use class, 2003–2020."),
            (C + "wa-landuse-share.png", "Basin area by WA+ land-use class."),
        ])
    ),
    "pt": (
        fig(P + "wa-dashboard-panel.png",
            "Figura 1: Limpopo Basin Water Balance (WA+ Dashboard) — o cartão do marcador da bacia, com os botões Show Raw Data, Advanced Chart e Balance Dashboard. O Balance Dashboard abre as contas WA+ compiladas (folha de recursos-base em Sankey) no portal em produção.") +
        "- Este marcador único é a porta de entrada das contas: **Balance Dashboard** para as folhas, **Download** para o CSV mensal de cada termo desde 2003.\n\n" +
        fig(P + "wa-dashboard-chart.png",
            "Figura 2: O local WA+ após Expand — todos os termos do balanço mensal (cerca de 35 séries: entradas, ET por classe de uso do solo, saídas, variação de armazenamento) num só eixo, 2003–2021.") +
        "- O painel traça **todos os termos de uma vez**, o que só é útil para ver o ritmo sazonal: a entrada de precipitação (rosa) atinge o pico cada verão; os termos de ET (amarelo/laranja) seguem um a dois meses depois.\n"
        "- Desligue séries na legenda para isolar um termo — p. ex. mantenha *Inflow Precipitation Rainfall* e *Outflow ET Landscape Utilized* para ver que em verões secos a ET excede a chuva.\n"
        "- Para análise use **Download** (uma coluna por termo) ou o **Balance Dashboard**; a secção recolhida abaixo mostra como ficam os totais anuais.\n\n" +
        fig(P + "realtime-station-a2h012-panel.png",
            "Figura 3: SWAT and Observed Sites — o cartão da estação A2H012FW (Krokodil em Kalkheuwel): estado, último caudal (16,55 m³/s em 2 de set. de 2026) e um botão Advanced Chart. Estações como esta são a verdade de terreno com que as contas são validadas.") +
        "- O caudal observado nas estações da bacia é o **termo de escoamento** medido, não modelado; onde discorda do escoamento WA+, a conta precisa de ajuste.\n\n" +
        collapsed(PT_COLL, PT_COLL_INTRO, [
            (C + "wa-annual-balance.png", "Precipitação, ET total e escoamento por ano, 2003–2024 (km³/ano)."),
            (C + "wa-et-by-landuse.png", "Percentagem da ET da bacia por classe de uso do solo WA+, 2003–2020."),
            (C + "wa-landuse-share.png", "Área da bacia por classe de uso do solo WA+."),
        ])
    ),
}

# ------------------------------------------------------------------ irrigation
PAGES["irrigation"] = {
    "en": (
        fig(P + "dam-loskop-panel.png",
            "Figure 1: Dams & Reservoirs Basin Level Estimates — the Loskop card (Olifants River, main use Irrigation): current level, estimated volume, status, capacity, catchment and the estimation model, with the storage preview. This is the supply check for the Loskop Irrigation Scheme.") +
        "- **Main use: Irrigation** and **catchment** tell you what the dam is for and how fast it can refill; **current level** at the start of October is the number the irrigation board sets quotas on.\n\n" +
        fig(P + "dam-loskop-chart.png",
            "Figure 2: Loskop after Expand → Estimated Volume, 2016–2026 (Mm³ and % of capacity).") +
        "- Each **saw-tooth is one irrigation season**: full after the summer rains, drawn down from May to November as the scheme takes its quota, then refilled. The depth of the tooth is the season's consumption from storage.\n"
        "- **2016** (down to ~150 Mm³, 42 %) followed the failed 2015 rains — the year quotas were cut; 2019 and late 2024 (~250 Mm³) were tight but not critical.\n"
        "- Compare the current position with the same month in previous years before committing the coming season's allocation.\n\n" +
        fig(P + "reservoir-area-massingir-chart.png",
            "Figure 3: Reservoir Levels – Water Area Timeseries for Massingir Dam — the reservoir that supplies the Chókwè and Lower Limpopo schemes (~67,000 ha irrigated). Satellite water area (ha) with observed volume where gauged.") +
        "- The 2016–19 decline and 2020 recovery visible here set the irrigated area at Chókwè in those seasons; the layer keeps monitoring after the gauge record ends (2019).\n\n" +
        fig(P + "realtime-station-a2h012-panel.png",
            "Figure 4: SWAT and Observed Sites — gauge A2H012FW on the Krokodil (Crocodile West) at Kalkheuwel, downstream of the Hartbeespoort irrigation area: latest observed discharge and an Advanced Chart button.") +
        "- River gauges below a scheme show its **return flows and abstraction** in the dry season; a gauge reading near zero while the scheme's fields are green in *Irrigated Mapping* is the signature of full abstraction.\n"
        "- The scheme-level consumption chart itself comes from **Water Use Time-series (Irrigated Areas) (Polygon)** — draw the polygon and run it; the result is monthly m³ for your area (it is an analysis process, so there is no fixed feature to click).\n\n" +
        collapsed(EN_COLL, EN_COLL_INTRO, [
            (C + "irrigation-schemes.png", "Major schemes — designed vs currently irrigated area."),
            (C + "irrigation-managed-et.png", "Mean monthly ET from managed (irrigated) land against the basin rainfall calendar."),
            (C + "irrigation-loskop-supply.png", "Loskop Dam storage by year with annual min–max."),
        ])
    ),
    "pt": (
        fig(P + "dam-loskop-panel.png",
            "Figura 1: Dams & Reservoirs Basin Level Estimates — o cartão de Loskop (rio Olifants, uso principal Irrigação): nível atual, volume estimado, estado, capacidade, bacia e modelo de estimativa, com a pré-visualização do armazenamento. É a verificação de abastecimento do perímetro de Loskop.") +
        "- **Main use: Irrigation** e **catchment** dizem para que serve a barragem e quão depressa pode reencher; o **nível atual** no início de outubro é o número com que a associação de regantes fixa as quotas.\n\n" +
        fig(P + "dam-loskop-chart.png",
            "Figura 2: Loskop após Expand → Estimated Volume, 2016–2026 (Mm³ e % da capacidade).") +
        "- Cada **dente de serra é uma campanha de irrigação**: cheia após as chuvas de verão, baixada de maio a novembro à medida que o perímetro usa a quota, depois reenchida. A profundidade do dente é o consumo da campanha a partir do armazenamento.\n"
        "- **2016** (até ~150 Mm³, 42 %) seguiu-se às chuvas falhadas de 2015 — o ano em que as quotas foram cortadas; 2019 e fim de 2024 (~250 Mm³) foram apertados mas não críticos.\n"
        "- Compare a posição atual com o mesmo mês de anos anteriores antes de comprometer a repartição da próxima campanha.\n\n" +
        fig(P + "reservoir-area-massingir-chart.png",
            "Figura 3: Reservoir Levels – Water Area Timeseries para a barragem de Massingir — a albufeira que abastece os perímetros de Chókwè e do Baixo Limpopo (~67 000 ha irrigados). Área de água por satélite (ha) com volume observado onde há estação.") +
        "- O declínio de 2016–19 e a recuperação de 2020 aqui visíveis determinaram a área irrigada em Chókwè nessas campanhas; a camada continua a monitorizar depois de terminar o registo da estação (2019).\n\n" +
        fig(P + "realtime-station-a2h012-panel.png",
            "Figura 4: SWAT and Observed Sites — estação A2H012FW no Krokodil (Crocodile West) em Kalkheuwel, a jusante da área de irrigação de Hartbeespoort: último caudal observado e um botão Advanced Chart.") +
        "- As estações a jusante de um perímetro mostram os seus **retornos e captações** na época seca; uma leitura perto de zero enquanto os campos do perímetro estão verdes em *Irrigated Mapping* é a assinatura de captação total.\n"
        "- O gráfico de consumo ao nível do perímetro vem de **Water Use Time-series (Irrigated Areas) (Polygon)** — desenhe o polígono e execute; o resultado são m³ mensais para a sua área (é um processo de análise, por isso não há um elemento fixo onde clicar).\n\n" +
        collapsed(PT_COLL, PT_COLL_INTRO, [
            (C + "irrigation-schemes.png", "Principais perímetros — área projetada vs atualmente irrigada."),
            (C + "irrigation-managed-et.png", "ET mensal média do solo gerido (irrigado) contra o calendário de precipitação da bacia."),
            (C + "irrigation-loskop-supply.png", "Armazenamento da barragem de Loskop por ano com mín.–máx. anual."),
        ])
    ),
}

HEAD = {"en": "## Reading the charts", "pt": "## Interpretar os gráficos"}

for page, langs in PAGES.items():
    for lang, body in langs.items():
        f = ROOT / (f"{page}.md" if lang == "en" else f"{page}.pt.md")
        s = io.open(f, encoding="utf-8").read()
        m = re.search(rf"^{re.escape(HEAD[lang])}\n(.*?)(?=^## )", s, flags=re.S | re.M)
        assert m, f"section not found in {f}"
        intro = EN_INTRO if lang == "en" else PT_INTRO
        new = f"{HEAD[lang]}\n\n{intro}\n\n{body}\n"
        s = s[: m.start()] + new + s[m.end():]
        io.open(f, "w", encoding="utf-8").write(s)
        print("updated", f.name)
