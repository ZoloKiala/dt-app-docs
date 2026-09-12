---
title: Contabilidade da água
---

# Contabilidade da água

## A pergunta

Um planeador de bacia ou analista da LIMCOM precisa de um **balanço coerente da
água da bacia**: quanta chega como chuva, quanta sai por evaporação e
transpiração, quanta escoa, quanta é consumida por cada setor, e como esse
balanço está a mudar — a base de evidência para a alocação entre os quatro
países ribeirinhos.

## Dados a utilizar

| Termo do balanço | Conjunto de dados | Onde no catálogo |
| --- | --- | --- |
| **Entrada: precipitação** | **CHIRPS Historical Rainfall** · **Rainfall Stations (LIMIS)** · **Number of Rainy Days** | Natural Basin Characteristic → Climate; Water Use Monitoring and Analysis → Water Accounting |
| **Saída: consumo** | **Evaporation Africa** · **Transpiration Africa** · **Interception Africa** | Water Use Monitoring and Analysis → Water Accounting → Evapotranspiration & Water Use |
| **Consumo por origem** | **Blue ET Africa** (irrigação / águas superficiais e subterrâneas) · **Green ET Africa** (chuva) | mesmo grupo |
| **Produtividade do uso** | **Beneficial Fraction Africa** · **ET Fraction Africa** · **Evaporative Stress Index Africa** | mesmo grupo |
| **Saída: escoamento** | **Mean Annual Runoff (LIMIS)** · **Runoff Zones (LIMIS)** · **SWAT Incremental Contributions** | Climate; → Basin Water Balance |
| **Procura setorial** | **Hydropower Evaporation Footprint (Africa)** · **Irrigation Areas (LIMIS)** · **Water Use Time-series (Irrigated Areas) (Polygon)** | → Sectoral Demand; Water Resources; Water Use Monitoring and Analysis |
| **Transferências e armazenamento** | **Inter-basin Water Transfers (LIMIS)** · **Dams & Reservoirs Basin Level Estimates** | Water Resources |
| **Verdade de terreno** | **Water Balance Stations (LIMIS)** · **Evaporation Stations (LIMIS)** · **Streamflow Gauging Stations (LIMIS)** | Water Resources → Streamflow Monitoring; Climate |
| **As próprias contas** | **Water Balance Dashboard** | Aberto a partir do menu do portal — as contas de água da bacia compiladas |

## Percurso

1. **Enquadre o balanço.** Explore data → adicione **CHIRPS Historical Rainfall**
   e **Evaporation Africa**. Coloque a linha temporal no mesmo mês em ambos.
   Chuva a entrar, evaporação a sair: onde a evaporação excede a precipitação, a
   paisagem está a consumir armazenamento.
2. **Separe o consumo.** Substitua *Evaporation* por **Blue ET Africa** e **Green
   ET Africa**, usando **Compare** lado a lado. A ET azul é água que teve de ser
   fornecida — a parte gerida do balanço; a ET verde é chuva usada no local.
3. **Avalie a produtividade.** Adicione **Beneficial Fraction Africa**. Consumo
   elevado com fração benéfica baixa é água perdida sem benefício — o primeiro
   sítio onde procurar poupanças.
4. **Siga o escoamento.** Adicione **SWAT Incremental Contributions** e **Mean
   Annual Runoff (LIMIS)**: que sub-bacias geram o rio, e como se compara a
   contribuição modelada com a média de longo prazo.
5. **Atribua setores.** Adicione **Irrigation Areas (LIMIS)** e **Hydropower
   Evaporation Footprint (Africa)**; para um número ao nível do perímetro,
   execute **Water Use Time-series (Irrigated Areas) (Polygon)** sobre o limite
   do perímetro.
6. **Contabilize transferências e armazenamento.** Adicione **Inter-basin Water
   Transfers (LIMIS)** e **Dams & Reservoirs Basin Level Estimates** — a água que
   atravessa a fronteira ou fica armazenada fecha o balanço.
7. **Verifique com as estações.** Adicione **Water Balance Stations (LIMIS)** e
   **Evaporation Stations (LIMIS)**; clique numa estação para valores observados
   e valide os termos de satélite.
8. **Abra o Water Balance Dashboard** a partir do menu do portal para as contas
   compiladas, e cruze-as com as camadas que reuniu no mapa.
9. Guarde a vista montada como **Story**, uma cena por termo do balanço.

## Interpretar o resultado

- Pense em **uma unidade**: as camadas de ET estão em mm por período;
  multiplique pela área para obter volume, e mantenha precipitação e ET no mesmo
  período ao comparar.
- **A ET azul é a água negociável.** Onde se concentra — e em que país — é o
  cerne da conversa sobre alocação.
- Uma **tendência crescente da ET azul** com precipitação estável e níveis de
  albufeira a descer é a assinatura da sobre-alocação.

## Limites a ter em conta

- Os produtos de ET à escala de África são **saídas de modelo a resolução
  continental**; são coerentes em toda a bacia (o que a contabilidade exige) mas
  devem ser calibrados com estações antes de serem citados como volumes.
- O **Mean Annual Runoff (LIMIS)** é uma média de longo prazo, não um valor
  atual.
- A captação de águas subterrâneas só é parcialmente visível (através da ET azul
  e das camadas de aquíferos); uma conta completa precisa de dados de furos.
- O dashboard e o processo de série temporal por polígono exigem **sessão
  iniciada**.

## Relacionados

[Uso de água na irrigação](irrigation.md) · [Monitorização de albufeiras](reservoirs.md) ·
[Secas](droughts.md) · [Catálogo de Dados](../guide/data-catalogue.md)
