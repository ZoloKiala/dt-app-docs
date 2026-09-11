---
title: Implementação Técnica
---

# Implementação Técnica

## Arquitetura da plataforma

O Portal WebGIS assenta na framework **TerriaJS**, escolhida pela capacidade de
compor catálogos de dados espaciais combinando curadoria manual com consulta em
tempo real de serviços online. O TerriaJS sustenta também plataformas de
referência como o NationalMap australiano e o Digital Twin Visualisation
Service de Nova Gales do Sul.

<figure markdown="span">
  ![A página inicial da framework TerriaJS](../assets/images/image1.png)
  <figcaption>Figura 1: A página inicial da framework TerriaJS.</figcaption>
</figure>

### Integração das fontes de dados

A plataforma integra várias classes de dados:

| Fonte | Contributo |
| --- | --- |
| **Imagens de satélite** | Provenientes do Google Earth Engine e dos registos de dados abertos da AWS |
| **Resultados de modelos numéricos** | Previsões e simulações em tempo real da hidrologia da bacia |
| **Dados in-situ** | Dados de sensores recolhidos na bacia, que fornecem validação no terreno para os dados de satélite e de modelo |

## Principais funcionalidades

O conjunto de funcionalidades foi moldado pelo retorno da Fase 1 e por
plataformas como a Digital Earth Africa.

- **Visualização de dados** — capacidades melhoradas de visualização 2D e 3D.
- **Sincronização de dados** — sincronização em tempo real com as fontes de
  dados.
- **Controlo de camadas** — um painel robusto de gestão de camadas organizado
  por área temática.
- **Ferramentas interativas** — exportação de mapas, opções de partilha e barra
  de séries temporais.
- **Funcionalidade de pesquisa** — barra de pesquisa geocodificada restrita à
  área de estudo.
- **Catálogo de dados** — um catálogo abrangente para exploração e seleção de
  dados.

### Controlos interativos do mapa

- **Ampliar e deslocar** — controlos padrão para navegação intuitiva nos dados
  espaciais.
- **Painel de controlo de camadas** — ativar e desativar camadas temáticas para
  uma análise dirigida.

### Ferramentas de visualização de dados

- **Análise de séries temporais** — explorar a evolução temporal dos dados,
  como os níveis de água ou o uso do solo ao longo do tempo.
- **Mapas de base personalizáveis** — visualizar os dados sobre diferentes
  mapas de fundo.

### Exportação e partilha de dados

- **Exportação de mapas** — exportar a vista atual do mapa como ficheiro de
  imagem, incluindo as camadas de dados e anotações selecionadas.
- **Capacidade de partilha** — gerar ligações partilháveis para que outros
  possam abrir uma vista ou configuração de dados específica.

### Assistente com IA

Está integrado no portal um assistente conversacional com inteligência
artificial, para apoiar os utilizadores em questões e navegação.

## Experiência do utilizador e desenho da interface

A interface foi concebida para ser intuitiva, com ênfase na simplicidade e na
acessibilidade. O desenho espelha a plataforma DE Africa e o NationalMap, com
melhorias que respondem aos requisitos específicos do IWMI e do projeto da
bacia do Rio Limpopo.

### Funcionalidades de acessibilidade

- **Compatibilidade entre navegadores** — compatível com todos os principais
  navegadores, garantindo uma experiência consistente em vários dispositivos.
- **Design responsivo** — a interface adapta-se a vários tamanhos de ecrã,
  incluindo tablets e telemóveis.

## Versão e informação do sistema

- **Portal:** <https://limpopo.digitaltwins.iwmi.org/>
- **Versão do TerriaMap:** `0.4.1`
- **Versão do TerriaJS:** `8.9.5`
- **Data de compilação:** 2026-05-15
- **Componentes da plataforma:** Cesium ion para cartografia 3D, atribuição dos
  dados e seleção do mapa de base.
