---
title: Projeto
---

# Visão Geral do Projeto

O Portal WebGIS disponibiliza uma interface abrangente e intuitiva para
visualizar conjuntos de dados climáticos e de recursos hídricos. Agrega e
interpola dados de múltiplas fontes — imagens de satélite, dados de sensores no
terreno e resultados de modelos numéricos — armazenados sobretudo na AWS.

## Enquadramento

O projeto Portal WebGIS Fase 2, desenvolvido para o Instituto Internacional de
Gestão da Água (IWMI), disponibiliza um portal web geoespacial avançado para
visualizar e interagir com conjuntos de dados espaciais relevantes para a bacia
do Rio Limpopo. A plataforma integra um Gémeo Digital (DT) da bacia.

A Fase 2 assenta na base estabelecida na Fase 1, tirando partido da framework
TerriaJS — uma plataforma de código aberto reconhecida pela exploração de
catálogos geoespaciais na web. O portal inspira-se em plataformas como a
Digital Earth Africa (DE Africa) e incorpora melhorias resultantes do retorno
recolhido na Fase 1.

## Objetivos

| Objetivo | Descrição |
| --- | --- |
| **Visualização geoespacial** | Desenvolver uma aplicação web que constitua a base do Gémeo Digital, para visualizar e interagir com dados espaciais específicos da bacia do Rio Limpopo |
| **Funcionalidades cartográficas** | Implementar funcionalidades essenciais como ampliação, deslocamento e controlo de camadas |
| **Integração de dados** | Integrar fontes geoespaciais diversas para disponibilizar informação rigorosa e atualizada |
| **Experiência do utilizador** | Oferecer uma interface intuitiva para navegação e exploração de dados sem atritos |
| **Compatibilidade entre navegadores** | Garantir que o portal funciona eficazmente em diferentes navegadores e dispositivos |

## Âmbito

O portal abrange os seguintes componentes principais:

- **Portal responsivo** — um portal WebGIS interativo concebido para
  dispositivos diversos.
- **Integração de dados geoespaciais** — dados agregados a partir de APIs e
  outras fontes.
- **Visualização avançada** — ferramentas para visualizar dados relativos a
  áreas irrigadas.
- **Assistente com IA** — um assistente conversacional para apoiar os
  utilizadores em questões e navegação.
- **Mapas de séries temporais melhorados** — mapas de séries temporais
  corrigidos e melhorados para uma melhor análise de dados.
- **Shapefiles adicionais** — inclusão de shapefiles adicionais para uma
  cobertura de dados mais completa.
- **Implementação na AWS** — alojamento na AWS para elevada disponibilidade e
  escalabilidade.

## Nesta secção

<div class="grid cards" markdown>

-   :material-sitemap: **[Implementação Técnica](architecture.md)**

    Arquitetura da plataforma, integração das fontes de dados e conjunto de
    funcionalidades.

-   :material-source-branch: **[Processo de Desenvolvimento](development.md)**

    A abordagem iterativa em três fases seguida na construção do portal.

-   :material-cloud-upload: **[Implementação e Manutenção](deployment.md)**

    Implementação na AWS, manutenção contínua e apoio ao utilizador.

</div>
