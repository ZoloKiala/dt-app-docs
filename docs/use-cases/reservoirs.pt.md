---
title: Monitorização de albufeiras
---

# Monitorização de albufeiras

## A pergunta

Um operador de barragem, uma entidade de abastecimento em alta ou a equipa da
LIMCOM quer saber **quão cheias estão as albufeiras da bacia, como cada uma
evoluiu ao longo da estação e que afluências as próximas semanas deverão
trazer** — incluindo para barragens sem telemetria, observando-as a partir do
espaço.

## Dados a utilizar

| Conjunto de dados | Onde no catálogo | O que indica |
| --- | --- | --- |
| **Dams and Reservoirs (LIMIS)** | Water Resources → Reservoirs and Storage | As barragens registadas: localização, nome, atributos |
| **Dams & Reservoirs Basin Level Estimates** | mesmo grupo (também em Flood Monitoring → Supporting Hydrological Data) | Nível de armazenamento estimado por barragem, em toda a bacia |
| **Reservoir Levels – Water Area Timeseries** | mesmo grupo | Área de superfície da água ao longo do tempo, derivada de satélite — um indicador indireto do nível, para qualquer barragem |
| **Reservoir Levels – DEA by Original ID** · **– Aggregated by Channel** · **– Yearly Aggregated by Channel** | mesmo grupo | O mesmo sinal por massa de água, por canal fluvial e como resumos anuais |
| **Waterbodies from DEA (Raster WMS)** · **Water Observations – All-Time Frequency** | Water Resources → Surface Waterbodies | Onde a água está normalmente presente e com que frequência — a pegada de referência |
| **Rolling Monthly GeoMAD (Sentinel-2)** | Satellite Images | Uma imagem mensal sem nuvens para inspecionar uma albufeira à vista |
| **Streamflow Gauging Stations (LIMIS)** · **Verified Monitoring Stations (LIMIS)** · **SWAT and Observed Sites** | Water Resources → Streamflow Monitoring | Estações de afluência a montante da barragem |
| **GloFAS Discharge Forecast – SWAT Channels** | Flood Monitoring → Discharge Forecasting | Afluência prevista para o canal que alimenta a barragem |
| **Gráfico de previsão da albufeira** | Clique numa albufeira com previsão ativa | Nível previsto para o período seguinte |

## Percurso

1. **Explore data → pesquise `Reservoir` → adicione `Dams & Reservoirs Basin
   Level Estimates`**, depois **Dams and Reservoirs (LIMIS)** para os nomes. Use
   **Ideal Zoom**.
2. **Clique numa barragem.** O painel **Feature Information** dá os atributos e,
   onde a previsão está ativa, um **gráfico de previsão da albufeira**. Use
   **Show Raw Data** ou o descarregamento CSV/JSON para a tabela.
3. Adicione **Reservoir Levels – Water Area Timeseries** e clique na mesma
   albufeira: o gráfico mostra a área de superfície da água ao longo do tempo.
   Uma área a encolher na estação seca e a recuperar depois das chuvas é o ciclo
   normal; um declínio plurianual é a preocupação.
4. Para uma **visão de longo prazo**, adicione **Reservoir Levels – Yearly
   Aggregated by Channel** e compare anos lado a lado.
5. **Veja-o.** Adicione **Rolling Monthly GeoMAD (Sentinel-2)** e coloque a linha
   temporal em duas datas com um ano de intervalo; use **Compare**
   (esquerda/direita) para ver a linha de costa mover-se. Adicione **Water
   Observations – All-Time Frequency** para ver a pegada de armazenamento pleno
   que a albufeira *deveria* preencher.
6. **Afluências.** Adicione **Streamflow Gauging Stations (LIMIS)** e **GloFAS
   Discharge Forecast – SWAT Channels**; clique no canal a montante da barragem
   para o hidrograma previsto. Afluência prevista crescente com a albufeira
   baixa é boa notícia; com a albufeira cheia é risco de descarga (ver
   [Cheias](floods.md)).
7. Capture uma cena por albufeira como **Story** para a reunião de operações.

## Interpretar o resultado

- **A área de água é um indicador indireto do volume.** Converta com a curva
  área–capacidade da barragem onde a tiver; caso contrário leia-a como
  indicador *relativo* e de tendência.
- Compare a pegada atual com a camada **All-Time Frequency**: a diferença entre
  onde a água *costuma* estar e onde está *agora* é o défice de armazenamento
  visível.
- Os **agregados anuais** suavizam a sazonalidade e expõem o declínio estrutural
  por assoreamento, sobre-alocação ou seca.

## Limites a ter em conta

- As séries de área de água por satélite são **óticas**: falhas por nuvens na
  estação húmida e braços estreitos e arborizados de uma albufeira reduzem a
  precisão.
- A área não capta a **profundidade**; uma albufeira pouco profunda pode parecer
  cheia com pouca água.
- As *estimativas* de nível e as previsões são **modeladas** onde não há
  telemetria — não substituem uma estação onde ela existe.
- Os gráficos de previsão exigem **sessão iniciada**.

## Relacionados

[Cheias](floods.md) · [Caudais ecológicos](eflows.md) ·
[Contabilidade da água](water-accounting.md) ·
[Ferramentas do Mapa — Comparar](../guide/map-tools.md#comparar)
