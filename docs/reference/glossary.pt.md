---
title: Glossário
---

# Glossário

Termos e siglas utilizados nesta documentação. Os nomes que aparecem na
interface do portal são apresentados em inglês, tal como surgem no ecrã.

### Plataforma e projeto

**Gémeo Digital (Digital Twin, DT)**
: Uma representação virtual da bacia do Rio Limpopo, construída a partir de
  imagens de satélite, dados de sensores no terreno e resultados de modelos
  numéricos.

**TerriaJS**
: A framework geoespacial de código aberto sobre a qual o portal assenta.
  Compõe catálogos de dados espaciais combinando curadoria manual com consulta
  em tempo real de serviços online.

**IWMI**
: International Water Management Institute (Instituto Internacional de Gestão
  da Água) — a organização para a qual o portal foi desenvolvido.

**DE Africa**
: Digital Earth Africa, uma das plataformas que inspirou o desenho do portal.

**NationalMap**
: A plataforma cartográfica nacional da Austrália, também construída sobre
  TerriaJS.

**Cesium ion**
: O componente da plataforma que fornece cartografia 3D, atribuição dos dados e
  seleção do mapa de base.

### Interface

**Workbench** (*Área de Trabalho*)
: O painel à esquerda que lista todos os conjuntos de dados ativos no mapa, com
  controlos de visibilidade, opacidade, estilo e remoção.
  Ver [Área de Trabalho](../guide/workbench.md).

**Data Catalogue** (*Catálogo de Dados*)
: A coleção temática de conjuntos de dados disponíveis para adicionar ao mapa.
  Ver [Catálogo de Dados](../guide/data-catalogue.md).

**My Data** (*Os Meus Dados*)
: A secção para adicionar ficheiros locais ou serviços web próprios, sem os
  carregar para a plataforma. Ver [Os Meus Dados](../guide/my-data.md).

**Story / Story Editor** (*História / Editor de histórias*)
: A ferramenta narrativa para captar cenas do mapa acompanhadas de texto.
  Ver [Histórias e Partilha](../guide/sharing.md).

**Capture Scene** (*Captar cena*)
: A ação que guarda a vista atual do mapa, o título e a descrição como um passo
  de uma história.

**Split Screen Mode** (*Modo de ecrã dividido*)
: A vista de comparação que coloca dois conjuntos de dados lado a lado.
  Ver [Funcionalidade Compare](../guide/map-tools.md#funcionalidade-compare).

**Pedestrian Mode** (*Modo peão*)
: Uma vista dos dados ao nível da rua, a partir do solo.

**Ideal Zoom** (*Ampliação ideal*)
: Uma opção por conjunto de dados que desloca o mapa para a vista que melhor
  enquadra esses dados.

**Feature Information** (*Informação do elemento*)
: O painel que apresenta os atributos subjacentes a um elemento do mapa
  selecionado, com exportação em CSV e JSON.

### Dados e serviços

**WMS**
: Web Map Service — norma para a difusão de imagens cartográficas
  georreferenciadas, aceite pelo *Add Web Data*.

**WFS**
: Web Feature Service — norma para a difusão da geometria e dos atributos de
  elementos cartográficos, aceite pelo *Add Web Data*.

**GetCapabilities URL**
: O endereço do serviço apresentado na pré-visualização de um conjunto de
  dados, utilizado para o integrar noutro software SIG.

**GeoTIFF**
: Formato de imagem matricial com georreferenciação incorporada; suportado pelo
  *My Data*.

**GeoJSON**
: Formato baseado em JSON para codificar elementos geográficos; suportado pelo
  *My Data*.

**KML / KMZ**
: Keyhole Markup Language (e a respetiva forma comprimida) para anotação
  geográfica; suportado pelo *My Data*.

**Shapefile**
: Formato vetorial de utilização generalizada; suportado pelo *My Data*.

**DOI**
: Digital Object Identifier — o identificador persistente de citação indicado
  no painel de pré-visualização de um conjunto de dados.

**SIG**
: Sistema de Informação Geográfica (em inglês, *GIS*).

### Hidrologia e ambiente

**SWAT**
: Soil and Water Assessment Tool — o modelo hidrológico que fornece os dados de
  caudal atual e de contribuições incrementais.

**E-flow** (*caudal ecológico*)
: O regime de caudais necessário para sustentar os ecossistemas da bacia. O
  portal publica regiões de caudal ecológico, monitorização e previsão, níveis
  de alerta e avisos.

**Availability Surplus** (*excedente disponível*)
: No gráfico de caudal ecológico, o excedente disponível em quantidade ou
  unidade.

**Deficit** (*défice*)
: No gráfico de caudal ecológico, o défice ou a ausência de dados.

**CHIRPS**
: Climate Hazards Group InfraRed Precipitation with Station data — a fonte do
  conjunto de dados de precipitação histórica.

**VCI**
: Vegetation Condition Index (Índice de Condição da Vegetação) — um conjunto de
  dados de ocupação do solo disponível como série temporal.

**GeoMAD**
: O produto de geomediana e desvio absoluto mediano, aqui publicado como
  Rolling Monthly GeoMAD (Sentinel-2).

**Sentinel-2**
: A missão de satélite que está na origem das imagens mensais do portal.

**Water Observations from Space**
: Conjunto de dados de satélite com o resumo integral da água superficial
  observada.

**Nuvem de pontos 3D** (*3D Point Cloud*)
: Dados de elevação de alta resolução recolhidos por drone, disponíveis para o
  Rio Oliphants e para o Sistema do Rio Crocodile (Superior e Inferior).
