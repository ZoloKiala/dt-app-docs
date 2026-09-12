---
title: Uso de água na irrigação
---

# Monitorização do uso de água na irrigação

## A pergunta

Um planeador de recursos hídricos ou o gestor de um perímetro quer saber **onde
estão as áreas irrigadas, se estão a crescer e quanta água consomem** ao longo
de uma campanha — sem esperar por declarações de licenças ou levantamentos de
campo.

## Dados a utilizar

| Conjunto de dados | Onde no catálogo | O que indica |
| --- | --- | --- |
| **Irrigated Mapping** | Natural Basin Characteristic → Land Cover and Land Use | Áreas irrigadas derivadas de satélite, como série temporal |
| **Irrigation Areas (LIMIS)** | Water Resources → Water Infrastructure | Perímetros de irrigação registados / cartografados (limites de referência) |
| **Water Use Time-series (Irrigated Areas) (Polygon)** | Water Use Monitoring and Analysis | Um processo de análise: escolha uma área e obtenha a sua série temporal de uso de água |
| **WaPOR Downscaled** · **ETa Monthly Limpopo** | Natural Basin Characteristic → Climate | Evapotranspiração real — a água efetivamente consumida pelas culturas |
| **Blue ET Africa** · **Green ET Africa** | Water Use Monitoring and Analysis → Water Accounting → Evapotranspiration & Water Use | Separa o consumo em água fornecida pela irrigação (*azul*) e água da chuva (*verde*) |
| **Beneficial Fraction Africa** · **ET Fraction Africa** | mesmo grupo | Quanto da água consumida faz trabalho útil (crescimento das culturas) |
| **Land Use** · **Land Use (LIMIS)** | Natural Basin Characteristic → Land Cover and Land Use | Contexto: agricultura vs. vegetação natural vs. aglomerados |

## Percurso

1. **Explore data → Search the catalogue → `Irrigated Mapping` → Add to the map.**
   A camada varia no tempo, pelo que surge uma linha temporal por baixo do mapa.
2. Use **Ideal Zoom** no cartão da área de trabalho para enquadrar a camada e as
   setas da linha temporal para percorrer as datas. Os campos irrigados
   destacam-se como formas regulares e nítidas que se mantêm verdes na estação
   seca.
3. Adicione **Irrigation Areas (LIMIS)** e compare: irrigação detetada *fora* dos
   perímetros registados é o primeiro sinal de uso não licenciado ou em expansão.
4. Adicione **Blue ET Africa**. Na área de trabalho, reduza a **opacidade** para
   ~60% para manter os campos visíveis por baixo. ET azul elevada sobre um campo
   significa que está a usar água de irrigação, não chuva.
5. Use **Compare** ([Ferramentas do Mapa](../guide/map-tools.md#comparar)) para
   colocar **Blue ET** à esquerda e **Green ET** à direita no mesmo mês — o
   contraste separa de imediato a agricultura irrigada da de sequeiro.
6. Para quantificar um perímetro: abra **Water Use Time-series (Irrigated Areas)
   (Polygon)** em *Water Use Monitoring and Analysis*, selecione ou desenhe a
   área de interesse e execute. O resultado é uma série temporal de uso de água
   para esse polígono, que pode ler diretamente ou descarregar.
7. **Story → Capture Scene** para as datas antes/depois, e **Share / Print** a
   ligação.

## Interpretar o resultado

- O **crescimento da área irrigada** entre anos é o indicador principal; use a
  linha temporal em *Irrigated Mapping* e capture uma cena por ano.
- **Blue ET ≫ Green ET** sobre um campo confirma a dependência da irrigação e dá
  uma estimativa de consumo em mm — multiplique pela área para obter o volume.
- Uma **Beneficial Fraction** baixa sobre um bloco irrigado indica água perdida
  por evaporação do solo em vez de crescimento das culturas — candidato a
  medidas de eficiência.

## Limites a ter em conta

- Os produtos de ET por satélite são **estimativas modeladas** na sua resolução
  nativa (WaPOR downscaled, camadas de ET à escala de África); use-os para
  padrões e tendências, e valide volumes com captações medidas onde existam.
- **Irrigated Mapping** é classificado a partir de imagens; a nebulosidade na
  estação húmida pode reduzir a confiança em datas isoladas — observe várias.
- O processo **Water Use Time-series** por polígono corre no servidor; áreas
  grandes demoram mais e exige sessão iniciada.

## Relacionados

[Contabilidade da água](water-accounting.md) · [Secas](droughts.md) ·
[Área de Trabalho — séries temporais](../guide/workbench.md#series-temporais)
