---
title: Catálogo de Dados
---

# Catálogo de Dados

## Vídeo: visita rápida

<div class="video-wrap" markdown>
<video controls preload="metadata" poster="../../assets/v2/v2-data-catalogue.png">
  <source src="../../assets/video/quick-data-catalogue.mp4" type="video/mp4">
  <track kind="captions" src="../../assets/video/quick-data-catalogue.vtt" srclang="en" label="English">
  O seu navegador não suporta vídeo incorporado.
  <a href="../../assets/video/quick-data-catalogue.mp4">Descarregar o vídeo</a>.
</video>
</div>

*Uma visita de um minuto sobre encontrar, pré-visualizar e adicionar dados. A narração e as legendas estão em inglês (voz sintética); ative as legendas com o botão **CC**.*


Clique em **Explore data** na área de trabalho (ou **Explore map data** no
painel de boas-vindas) para abrir o **Data Catalogue** (*Catálogo de Dados*).
Na v2, é um painel de dois lados: a árvore de categorias à esquerda e a
pré-visualização de um conjunto de dados à direita.

<figure markdown="span">
  ![O Catálogo de Dados da v2 com as suas onze categorias](../assets/v2/v2-data-catalogue.png)
  <figcaption>Figura 3: O Catálogo de Dados. O painel esquerdo lista as onze categorias temáticas; ao selecionar um conjunto de dados, este é pré-visualizado à direita.</figcaption>
</figure>

No topo do painel estão dois separadores — **Data** (o catálogo curado) e
**My Data** (os seus próprios ficheiros, ver [Os Meus Dados](my-data.md)) — uma
caixa **Search the catalogue** (*Pesquisar no catálogo*), e um botão **Done**
(*Concluído*) que o devolve ao mapa.

## As onze categorias

A v2 alarga o catálogo de cinco para **onze** categorias temáticas. Cinco são
novas desde a versão de 2024 (assinaladas **Nova**):

| Categoria | Conteúdo |
| --- | --- |
| **Natural Basin Characteristic** | Fisiografia, ocupação e uso do solo, nuvens de pontos 3D, clima |
| **Flood Monitoring & Early Warning** | **Nova** — camadas de monitorização de cheias e alerta precoce |
| **Drought Monitoring & Risk Assessment** | **Nova** — camadas de monitorização e risco de seca |
| **Socio-Economic Profile** | Dados de população e demografia |
| **Water Resources** | Fontes de água superficial e infraestruturas |
| **Citizen Science** | **Nova** — observações da comunidade (p. ex. miniSASS, FishTRAC) |
| **Water Use Monitoring and Analysis** | **Nova** — contabilidade e monitorização do uso da água |
| **Ecosystems** | Regiões de caudal ecológico, monitorização, alertas e avisos |
| **Satellite Images** | GeoMAD (Sentinel-2), Water Observations from Space |
| **Data Sources & Providers** | **Nova** — proveniência e informação dos fornecedores do catálogo |

Ver [Temas dos Dados](datasets.md) para um percurso pelo conteúdo de cada
categoria.

## Pesquisar no catálogo

Use **Search the catalogue** para encontrar um conjunto de dados pelo nome em
todas as categorias — mais rápido do que percorrer a árvore.

## Pré-visualizar e adicionar dados

Clique numa categoria para a expandir e selecione um conjunto de dados. A sua
**pré-visualização** aparece no painel direito, com uma descrição e um comando
de **adição** (o ícone **+**). A informação típica inclui:

1. **Descrição do conjunto de dados** — o que são os dados e a sua relevância.
2. **Adicionar ao mapa** — desenha o conjunto no globo (o ícone **+**; mantenha
   **Shift** e clique em **+** para adicionar vários de uma vez).
3. **Contacto do serviço** — quem contactar sobre os dados.
4. **GetCapabilities URL** — para integrar o conjunto noutro software SIG.
5. **DOI e fonte dos dados** — identificador de citação e fornecedor principal.

!!! tip "Adicionar vários de uma vez"
    O catálogo indica *"Press Shift and click + to add multiple datasets."* Use
    **Go to the map** ou **Done** quando terminar a seleção.

Depois de adicionado, um conjunto de dados aparece na
[Área de Trabalho](workbench.md), onde o pode ativar, ajustar a opacidade,
reestilizar, representar graficamente e comparar.

## Informação do elemento

Ao clicar num elemento do mapa abre-se a sua **Feature Information** — os
atributos por detrás desse ponto, com opções para descarregar a tabela
subjacente (CSV ou JSON) e mostrar os dados brutos. Para conjuntos com dimensão
temporal, um gráfico e uma linha temporal permitem explorar a evolução num
intervalo de datas escolhido.

## Passos seguintes

[Explorar os temas dos dados :octicons-arrow-right-24:](datasets.md){ .md-button .md-button--primary }
[Gerir camadas na Área de Trabalho :octicons-arrow-right-24:](workbench.md){ .md-button }
