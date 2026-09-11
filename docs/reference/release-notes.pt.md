---
title: Notas de Versão
---

# Notas de Versão

O que mudou entre o portal descrito pelo guia **v1** (TerriaMap `0.1.2` /
TerriaJS `8.7.1`, agosto de 2024) e o portal atualmente em funcionamento em
[limpopo.digitaltwins.iwmi.org](https://limpopo.digitaltwins.iwmi.org/).

!!! info "Fonte"
    Compilado a partir de `dt_limpopo/CHANGES.md` no repositório
    [iwmihq/dt-app](https://github.com/iwmihq/dt-app) e do `version.json` da
    instalação em produção. As entradas correspondem às versões do TerriaMap;
    cada uma incorpora uma atualização do TerriaJS.

## Versão atualmente em produção

| Campo | Valor |
| --- | --- |
| Portal | <https://limpopo.digitaltwins.iwmi.org/> |
| Pré-produção | <https://limpopo.staging.digitaltwins.iwmi.org/> |
| TerriaMap | `0.4.1` |
| TerriaJS | `8.9.5` |
| Data de compilação | 2026-05-15 |

## O que isto significa para os utilizadores

As alterações visíveis durante a utilização do portal:

- **A interface foi redesenhada.** O TerriaMap `0.4.0` trouxe "um novo aspeto
  da interface, com alterações à área de trabalho e a outros painéis". A
  [Área de Trabalho](../guide/workbench.md) e os painéis em seu redor já não
  têm o aspeto apresentado na v1.
- **As opções de mapa de base mudaram.** Os mapas de base da Carto —
  *positron*, *dark matter* e *black marble* — foram removidos das predefinições
  por passarem a exigir uma licença comercial da Carto. Em sua substituição, o
  **OpenStreetMap** passou a ser um mapa de base predefinido.
- **Mais formatos de dados podem ser adicionados.** O catálogo passou a
  suportar **I3S** (camadas de cena 3D indexadas) e **COG** (GeoTIFF otimizado
  para a nuvem), pelo que mais serviços externos podem ser integrados através de
  [Add Web Data](../guide/my-data.md#adicionar-dados-da-web).
- **As camadas ArcGIS são desenhadas mais depressa.** Os serviços de elementos
  ArcGIS passaram a suportar tiling, ativado automaticamente quando o servidor
  o permite.
- **Correções de representação.** Foram corrigidos vários erros de GeoJSON e de
  mapeamento por regiões que podiam deixar elementos por desenhar.

## Histórico de versões

### 0.4.1 — 2025-04-24

- TerriaJS `8.9.3`, com uma correção para o mapeamento por regiões e a
  representação de GeoJSON.

### 0.4.0 — 2025-04-04

- TerriaJS `8.9.2`. **Alteração incompatível.**
    - **Novo aspeto da interface**, com alterações à área de trabalho e a
      outros painéis.
    - Suporte de tiling para serviços de elementos ArcGIS, ativado por
      predefinição quando o servidor o permite e não são usados estilos de
      marcador/ponto não suportados.
    - Correção de uma regressão na representação de GeoJSON que deixava alguns
      elementos por desenhar.

### 0.3.0 — 2025-02-18

- TerriaJS `8.8.0`. **Alteração incompatível**, mas interna à compilação:
  Webpack 5, Sass 1.80+ e conversão de módulos CommonJS para ESM. Sem impacto
  para o utilizador.

### 0.2.4 — 2024-12-19

- TerriaJS `8.7.11`. Adicionados `clampToGround` e `dataSourceUri` aos traits
  do item de catálogo KML.

### 0.2.3 — 2024-11-29

- TerriaJS `8.7.10`. **OpenStreetMap adicionado como mapa de base
  predefinido.**

### 0.2.2 — 2024-11-22

- TerriaJS `8.7.9`. **Alteração incompatível:** os mapas de base da Carto
  *positron*, *dark matter* e *black marble* foram removidos das predefinições,
  por passarem a exigir uma licença Carto Enterprise ou Grantee.
- Adicionados `I3SCatalogItem` e `CogCatalogItem`.

### 0.2.1 — 2024-08-07

- TerriaJS `8.7.5`.

### 0.1.2 — 2024-05-02

- TerriaJS `8.7.1`. **Esta é a versão descrita na
  [documentação v1](index.md).** A compilação do portal aí documentada tinha a
  data de 2024-08-26.

## Implementação

O portal é compilado e implementado a partir de
[iwmihq/dt-app](https://github.com/iwmihq/dt-app) através de GitHub Actions, que
enviam imagens de contentor para o **Amazon ECR** e as implementam no
**Amazon ECS**.

- Os ramos com o sufixo `_prod` são implementados em produção
  (`dt_limpopo_prod` → produção do Limpopo); os ramos sem sufixo correspondem a
  pré-produção.
- Os segredos do `dt_limpopo` estão guardados no GitHub e são injetados durante
  a compilação da imagem; os restantes serviços leem-nos do AWS Secrets
  Manager.
- A autenticação em toda a plataforma Digital Twin é assegurada pelo
  **Keycloak** em <https://auth.iwmi.org>.

Ver [Implementação e Manutenção](../project/deployment.md) para mais detalhes.
