---
title: Caudais ecológicos
---

# Caudais ecológicos (e-flows)

## A pergunta

Um ecólogo, um regulador da bacia ou o operador de uma barragem precisa de
saber **se cada troço do Limpopo está a receber o caudal de que o seu
ecossistema precisa**, onde os caudais caíram abaixo dos níveis de alerta, e
**como uma alteração nas descargas ou nas captações mudaria o risco ecológico**.

## Dados a utilizar

| Conjunto de dados | Onde no catálogo | O que indica |
| --- | --- | --- |
| **E-flow Monitoring and Forecasting** | Drought Monitoring & Risk Assessment → Hydrological Drought & E-flows | Caudal atual modelado vs. requisito de caudal ecológico, por local, com previsão — clique para o gráfico |
| **Eflow Alert Levels** | mesmo grupo | Classe de alerta atual em cada local monitorizado |
| **Eflow Warnings** · **E-Flow Warning Status (LIMIS)** | mesmo grupo; Ecosystems → E-Flow Modeling & Risk | Troços atualmente em aviso |
| **E-flow Risk Regions** | mesmo grupo | As regiões ecológicas usadas na avaliação de risco |
| **SWAT Modelled Discharge** · **SWAT and Observed Sites** | Water Resources → Streamflow Monitoring | Caudal atual modelado e as estações contra as quais é verificado |
| **SWAT Incremental Contributions** | Water Use Monitoring and Analysis → Basin Water Balance | Quanto caudal cada sub-bacia acrescenta ao rio |
| **Aquatic Ecoregions (LIMIS)** · camadas **Suitability Class / Suitability Map** | Ecosystems → Ecological Monitoring | Contexto ecológico para interpretar um défice |
| **SWAT Extraction Tool** | Ferramentas do mapa (canto inferior direito) | Consulta caudais modelados para um canal e intervalo de datas; o separador **PROBFLO** liga o caudal ao risco ecológico |

## Percurso

1. **Explore data → pesquise `E-flow` → adicione `E-flow Monitoring and
   Forecasting`.** Os locais surgem ao longo da rede hidrográfica.
2. Adicione **Eflow Alert Levels** por cima. A cor indica a classe atual; comece
   pelo pior.
3. **Clique num local.** O gráfico abre com quatro séries — **SWAT Present
   Flow**, **E-Flow** (o requisito), **Availability Surplus** e **Deficit**. Passe
   o cursor sobre qualquer ponto para ler valores; arraste sobre o gráfico ou
   escolha datas de início e fim para focar uma estação.
4. Adicione **SWAT Incremental Contributions** para perceber *porquê*: um défice
   num local a jusante com contribuições saudáveis a montante aponta para
   captações ou armazenamento pelo meio, e não para uma bacia seca.
5. Adicione **SWAT and Observed Sites** e compare o caudal modelado com a
   estação mais próxima no gráfico — é a medida da confiança no modelo nesse
   troço.
6. **Teste de cenários.** Abra a **SWAT Extraction Tool** (ícone inferior
   direito). Escolha o **Flow Type** (p. ex. *Natural Flows*), introduza o
   **Channel ID** do local em que clicou, defina **Start / End Date** e **FETCH
   DATA**. Use o separador **MAP** para confirmar o canal, **TABLE** para os
   números e **PROBFLO** para ver a categoria de risco ecológico que o caudal
   implica.
7. Adicione **Aquatic Ecoregions (LIMIS)** e as camadas **Suitability** para
   ponderar um défice pela sensibilidade do troço.
8. Capture o mapa de alertas e o gráfico como **Story** para a comissão de
   caudais ecológicos.

## Interpretar o resultado

- O **Deficit** é o número operacional: quanto abaixo do requisito está o rio,
  em unidades de caudal, e durante quanto tempo. Défices curtos na estação seca
  podem ser naturais; **défices prolongados na estação húmida** são o sinal de
  alarme.
- As séries de previsão permitem agir antes de a classe de alerta mudar — uma
  previsão de caudal atual descendente a cruzar a linha E-Flow é a sua margem
  de antecipação.
- Use as **Incremental Contributions** para atribuir a falta a uma sub-bacia —
  é aí que uma intervenção (descarga, limite de captação) atuaria.

## Limites a ter em conta

- Todos os caudais aqui são **saídas do modelo SWAT**, calibradas com estações.
  Onde a estação mais próxima discorda do modelo, dê mais peso à estação.
- Os requisitos de caudal ecológico são eles próprios o produto de um método de
  avaliação; as categorias de risco do **PROBFLO** são probabilísticas, não
  limiares de dano.
- Os gráficos de local e a SWAT Extraction Tool chamam a API de dados do IWMI e
  **exigem sessão iniciada**.

## Relacionados

[Secas](droughts.md) · [Monitorização de albufeiras](reservoirs.md) ·
[Ferramentas do Mapa — Ferramenta de extração SWAT](../guide/map-tools.md#ferramenta-de-extracao-swat)
