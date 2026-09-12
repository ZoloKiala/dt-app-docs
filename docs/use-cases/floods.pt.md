---
title: Cheias
---

# Cheias

## A pergunta

Um técnico de proteção civil ou a autoridade da bacia precisa de três respostas
à medida que um evento evolui: **vem aí uma cheia, onde atingirão os rios o
pico, e quem e o que está exposto** — e, depois, **como se compara este evento
com o passado**.

## Dados a utilizar

| Conjunto de dados | Onde no catálogo | O que indica |
| --- | --- | --- |
| **GPM IMERG Precipitation Rate (Daily)** | Flood Monitoring & Early Warning → Real-Time Flood Detection | A precipitação de ontem por satélite — o gatilho |
| **Accumulated Precipitation (10-day)** · **Precipitation Prob. > 50 / 150 / 300 mm (10-day)** | → Discharge Forecasting (GloFAS) | Quanta chuva está prevista e a probabilidade de totais extremos |
| **Flood Summary Days 1–3 / 4–10 / 11–30** | → Discharge Forecasting (GloFAS) | Onde se prevê cheia fluvial, por horizonte |
| **Reporting Points (% Exceedance)** · **5-Year / 20-Year Exceedance Prob. (30-day)** | → Discharge Forecasting (GloFAS) | Probabilidade de os pontos do rio excederem limiares de cheia |
| **GloFAS Discharge Forecast – SWAT Channels** · **– Verified Gauges** | → Discharge Forecasting (GloFAS) | Hidrogramas previstos em canais e estações (clique para o gráfico) |
| **MODIS NRT Flood (1-Day)** · **VIIRS NRT Flood (1-Day)** | → Real-Time Flood Detection | Água efetivamente observada no terreno hoje |
| **Rapid Flood Mapping (1 km extent)** · **Rapid Impact Assessment** | → Impact & Inundation | Extensão do evento e primeira estimativa de impacto |
| **100-year Flood Hazard (Climatology)** · **20 / 50-Year Flood Lines – Lower Limpopo (LIMIS)** | → Flood Hazard & Exposure | Até onde se *espera* que as cheias cheguem — referências de planeamento |
| **MODIS Flood Frequency (2001–2024)** · **MODIS Flood Exposure – Longterm** · **Year 2000 Flood Inundation Boundaries (LIMIS)** | → Flood Hazard & Exposure | A pegada histórica, incluindo a cheia de referência de 2000 |
| **Population** · **Settlements (LIMIS)** | Socio-Economic Profile | Quem está no caminho |
| **Dams & Reservoirs Basin Level Estimates** | → Supporting Hydrological Data | Armazenamento que pode atenuar — ou libertar — a onda de cheia |

## Percurso

**Antes do evento — perspetiva**

1. **Explore data → `Accumulated Precipitation (10-day)` → Add to the map**, e
   adicione **Precipitation Prob. > 150 mm (10-day)**. Probabilidades elevadas
   sobre as cabeceiras (Botswana / Gauteng–Limpopo) significam que a baixa bacia
   deve preparar-se.
2. Adicione **Flood Summary Days 1–3**, depois **4–10**, e percorra-os: o sinal
   de cheia deve propagar-se para jusante à medida que o horizonte aumenta.
3. Adicione **Reporting Points (% Exceedance)** e clique num ponto do mapa. O
   painel **Feature Information** dá a probabilidade de excedência; use **Show
   Raw Data** para os números.

**Durante o evento — observar e confirmar**

4. Adicione **GPM IMERG Precipitation Rate (Daily)** e **MODIS NRT Flood
   (1-Day)**. Onde choveu ontem e hoje aparece água parada, a previsão está a
   confirmar-se.
5. Adicione **GloFAS Discharge Forecast – Verified Gauges** e clique na estação
   mais próxima da comunidade em causa: o gráfico mostra o caudal previsto
   face aos limiares.

**Exposição**

6. Adicione **Population** e **Settlements (LIMIS)** por baixo das camadas de
   cheia (arraste para reordenar na área de trabalho, reduza a opacidade da
   camada de cheia). Use **Compare** com **100-year Flood Hazard (Climatology)**
   para ver se a pegada prevista está dentro ou além da referência de projeto.

**Depois do evento**

7. Adicione **Rapid Flood Mapping (1 km extent)** e **Rapid Impact Assessment**,
   e compare a extensão cartografada com **MODIS Flood Frequency (2001–2024)** e
   os **Year 2000 Flood Inundation Boundaries (LIMIS)** para classificar o evento
   historicamente.
8. Capture as cenas principais como **Story** e **Share / Print** para o
   relatório de situação.

## Interpretar o resultado

- **Camadas de probabilidade não são extensões.** As camadas *Flood Summary* e
  *Exceedance* dizem quão *provável* é a cheia, não onde a água ficará — combine
  com as camadas NRT de observação para a extensão real.
- A coerência entre fontes é o sinal mais forte: previsão de chuva → excedência
  de caudal → água NRT observada, tudo alinhado num mesmo troço.
- As **Flood Lines (LIMIS)** do Baixo Limpopo são referências de engenharia;
  uma pegada prevista além da linha de 50 anos é excecional.

## Limites a ter em conta

- **O IMERG não mostra nada em dias secos** — uma camada vazia não é uma camada
  avariada. É também quase em tempo real, com atraso; verifique a data na linha
  temporal.
- A deteção NRT de cheias por MODIS/VIIRS é **diária e ótica**, e não vê água sob
  nuvens e vegetação; use-a para confirmar, não para excluir.
- O GloFAS é um **modelo global** ajustado aos canais da bacia; as estações
  verificadas são a âncora — confie mais nas previsões de canal onde uma estação
  concorda.
- Várias camadas LIMIS são **instantâneos históricos** (p. ex. a cheia de 2000);
  não se atualizam.

## Relacionados

[Monitorização de albufeiras](reservoirs.md) · [Secas](droughts.md) ·
[Ferramentas do Mapa — Comparar](../guide/map-tools.md#comparar) ·
[Informação do elemento](../guide/data-catalogue.md#informacao-do-elemento)
