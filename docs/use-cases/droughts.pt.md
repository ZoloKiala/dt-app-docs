---
title: Secas
---

# Secas

## A pergunta

Um técnico de extensão agrícola, uma entidade gestora de abastecimento ou uma
comissão de bacia quer saber **se se está a instalar uma seca, quão severa é
face a anos anteriores, que setores estão em risco e como se apresenta a
próxima estação**.

A seca constrói-se por fases, e o catálogo está organizado da mesma forma:
meteorológica (chuva), depois stress do solo e da vegetação, depois hidrológica
(rios e águas subterrâneas), depois risco setorial.

## Dados a utilizar

| Fase | Conjunto de dados | Onde no catálogo |
| --- | --- | --- |
| Défice de chuva | **CHIRPS Historical Rainfall** · **Number of Rainy Days** · **Rainfall Anomalies** | Drought Monitoring & Risk Assessment → Meteorological Drought |
| Défice de chuva (índices) | **Drought Hazard – SPEI 3-month / 6-month / 12-month (2010–2021)** | → Meteorological Drought |
| Solo | **SMAP Surface Soil Moisture (L4, Daily)** · **SMAP Root Zone Soil Moisture (L4, Daily)** · **SMAP-Sentinel High-Res Soil Moisture (1 km)** | → Soil Moisture |
| Vegetação | **The Vegetation Condition Index (VCI)** · **MODIS NDVI 16-Day Composite** · **VIIRS NDVI 8-Day Composite** · **NDVI Anomaly (DEA)** | → Vegetation & Crop Stress |
| Stress hídrico | **Evaporative Stress Index Africa** | → Evaporative Stress & Water Use |
| Rios | **E-flow Monitoring and Forecasting** · **Eflow Alert Levels** · **Eflow Warnings** | → Hydrological Drought & E-flows |
| Águas subterrâneas | **Groundwater Drought Risk (Updated)** · **Groundwater Level Points** | Water Resources → Groundwater |
| Risco por setor | **Drought Risk – Agriculture / Food & Nutrition / Water Sector (3, 6, 12-month)** | → Sectoral Drought Risk |
| Perspetiva | **Limpopo Rainfall Anomaly Forecast** · **Limpopo Temperature Anomaly Forecast** · **Seasonal Forecast Anomaly (7-month)** · **Sub-Seasonal Outlook (5–6 weeks)** | Natural Basin Characteristic → Climate; Flood Monitoring → Seasonal & Sub-Seasonal |

## Percurso

1. **Comece pela vegetação — o sinal mais visível.** Explore data → pesquise
   `VCI` → adicione **The Vegetation Condition Index (VCI)**. Use a linha
   temporal para comparar este mês com o mesmo mês de anos anteriores; o VCI já
   está normalizado face ao histórico, pelo que valores baixos significam *pior
   do que o habitual*, e não apenas *estação seca*.
2. **Confirme com NDVI Anomaly (DEA)** (adicione e use **Compare** face ao VCI).
   A concordância entre dois produtos de vegetação independentes é um sinal de
   seca robusto.
3. **Verifique a causa — a chuva.** Adicione **CHIRPS Historical Rainfall** e
   recue na linha temporal ao longo da estação; adicione **Rainfall Anomalies** e
   clique num círculo de estação para o gráfico. Depois adicione **Drought
   Hazard – SPEI 3-month** para o défice normalizado.
4. **Verifique o solo.** Adicione **SMAP Root Zone Soil Moisture (L4, Daily)**. O
   défice na zona radicular, e não apenas a secura superficial, é o que limita
   as culturas.
5. **Verifique os rios.** Adicione **Eflow Warnings** e **Eflow Alert Levels**,
   depois **E-flow Monitoring and Forecasting** e clique num local para o
   gráfico. Rios abaixo dos caudais ecológicos marcam a transição para seca
   hidrológica (ver [Caudais ecológicos](eflows.md)).
6. **Traduza em risco.** Adicione **Drought Risk – Agriculture (3-month)** e
   **Drought Risk – Water Sector (3-month)** com **Population** por baixo para
   ver onde as condições de stress encontram as pessoas.
7. **Olhe em frente.** Adicione **Limpopo Rainfall Anomaly Forecast** e o
   **Seasonal Forecast Anomaly (7-month)**: uma perspetiva seca sobre um défice
   já instalado é o gatilho para ação antecipada.
8. Guarde a sequência como **Story** — uma cena por fase faz um briefing
   convincente.

## Interpretar o resultado

- **A convergência conta.** Um índice isolado pode enganar; VCI + anomalia NDVI
  + SPEI + humidade do solo a apontar na mesma direção é uma seca.
- Use as camadas SPEI e de risco a **3, 6 e 12 meses** em conjunto: 3 meses
  captura uma estação falhada, 12 meses um défice plurianual que atinge
  albufeiras e aquíferos.
- A seca das águas subterrâneas **atrasa-se** meses face à seca superficial; um
  risco crescente nas camadas de aquíferos indica uma recuperação longa mesmo
  depois de a chuva regressar.

## Limites a ter em conta

- As camadas de perigo **SPEI cobrem 2010–2021** — uma climatologia de
  referência, não um índice em tempo real. Use o CHIRPS e as previsões de
  anomalia para a estação atual.
- NDVI/VCI respondem a **qualquer** alteração da vegetação (colheita, fogo,
  desmatação), não só à seca — cruze com a precipitação.
- O SMAP é grosseiro (o produto SMAP-Sentinel a 1 km é mais fino mas menos
  frequente).
- As previsões sazonais são **anomalias probabilísticas**; leia-as como
  probabilidades, não como previsões determinísticas.

## Relacionados

[Caudais ecológicos](eflows.md) · [Uso de água na irrigação](irrigation.md) ·
[Área de Trabalho — séries temporais](../guide/workbench.md#series-temporais)
