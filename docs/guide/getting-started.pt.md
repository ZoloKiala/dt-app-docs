---
title: Primeiros Passos
---

# Primeiros Passos

## Vídeo: uma visita rápida

<div class="video-wrap" markdown>
<video controls preload="metadata" poster="../../assets/v2/v2-main-map.png">
  <source src="../../assets/video/limpopo-getting-started.mp4" type="video/mp4">
  <track kind="captions" src="../../assets/video/limpopo-getting-started.vtt" srclang="en" label="English" default>
  O seu navegador não suporta vídeo incorporado.
  <a href="../../assets/video/limpopo-getting-started.mp4">Descarregar o tutorial</a>.
</video>
</div>

*Uma visita de ~2,5 minutos: início de sessão, exploração de dados, a área de
trabalho, mapas de base e partilha. A narração e as legendas estão em inglês
(voz sintética); ative as legendas com o botão **CC**.*

## Iniciar sessão

O portal v2 tem acesso controlado: ao abrir
[limpopo.digitaltwins.iwmi.org](https://limpopo.digitaltwins.iwmi.org/) é
encaminhado para a página **Digital Twin Applications Single Sign-On** antes de
o mapa carregar. Pode iniciar sessão de três formas:

- **Email e palavra-passe** — introduza as credenciais e clique em **Sign In**
  (marque **Remember me** para se manter com sessão iniciada; use
  **Forgot Password?** para repor).
- **Iniciar sessão com o Google** — use a sua conta Google.
- **Iniciar sessão com a Microsoft** — use a sua conta Microsoft.

Os novos utilizadores podem **Register** (*Registar*) na ligação no fundo da
página de início de sessão.

Após iniciar sessão, a barra superior mostra **Account** (*Conta*) e
**Log out** (*Terminar sessão*); use **Account** para gerir o seu perfil.

!!! info "Precisa de acesso?"
    Se não conseguir iniciar sessão ou registar-se, contacte a equipa
    geoespacial do IWMI através de
    [iwmigeospatial@gmail.com](mailto:iwmigeospatial@gmail.com).

## O ecrã de boas-vindas

No primeiro carregamento, o portal mostra um painel de boas-vindas
**"Let's get you started"** (*Vamos começar*) sobre o mapa.

<figure markdown="span">
  ![O painel de boas-vindas da v2 sobre a bacia do Limpopo](../assets/v2/v2-welcome.png)
  <figcaption>Figura 1: O painel de boas-vindas &ldquo;Let's get you started&rdquo;.</figcaption>
</figure>

Oferece três formas de entrar:

- **Take the tour** (*Fazer a visita*) — uma visita guiada interativa que
  identifica cada comando no ecrã.
- **I'll need some help** (*Vou precisar de ajuda*) — abre o guia de ajuda.
- **Explore map data** (*Explorar dados do mapa*) — fecha o painel e abre
  diretamente o [Catálogo de Dados](data-catalogue.md).

Feche o painel com **Close message and don't show me this again** (ou o **✕**)
para ir diretamente para o mapa. Segue-se uma pequena dica a apontar para
**Help** na barra superior — clique em **Got it, thanks!** para a limpar.

!!! tip "Primeira visita? Faça a visita guiada"
    A visita identifica cada comando, o que torna o resto deste guia muito mais
    fácil de seguir.

## A interface principal

<figure markdown="span">
  ![A interface principal do portal](../assets/v2/v2-main-map.png)
  <figcaption>Figura 2: A interface principal — a área de trabalho e os controlos de dados à esquerda, o globo 3D ao centro, as ferramentas do mapa à direita e a barra de conta e ferramentas no topo.</figcaption>
</figure>

A interface tem quatro zonas:

- **Área de trabalho (esquerda)** — o logótipo IWMI / LIMCOM / CGIAR Digital
  Transformation, a pesquisa de localização, os botões **Explore data** e
  **Upload data**, e a lista de conjuntos de dados atualmente no mapa. Ver
  [Área de Trabalho](workbench.md).
- **Mapa (centro)** — o globo 3D Cesium, com o contorno da bacia sobre imagens
  de satélite.
- **Ferramentas do mapa (direita)** — orientação, ampliação, localização,
  comparação, modo peão e medição. Ver [Ferramentas do Mapa](map-tools.md).
- **Barra superior** — **About**, **Account**, **Log out** à esquerda;
  **Map Settings**, **Help**, **Story** e **Share / Print** à direita.

## Procurar uma localização

A barra **Search for locations** no topo da área de trabalho salta para um
local dentro da bacia do Rio Limpopo. A pesquisa é geocodificada e restrita à
área de estudo da bacia.

## Explorar dados do mapa

Clique em **Explore data** (ou **Explore map data** no painel de boas-vindas)
para abrir o [Catálogo de Dados](data-catalogue.md). Pode adicionar vários
conjuntos de dados de uma só vez; cada um é depois gerido a partir da
[Área de Trabalho](workbench.md).

## Controlos interativos do mapa

Os controlos de navegação principais comportam-se como em qualquer mapa web:

- **Ampliar e deslocar** — navegue nos dados de forma intuitiva.
- **Mapas de base** — escolha um mapa de fundo em
  [Map Settings](map-tools.md#definicoes-do-mapa) (o conjunto da v2 inclui
  Bing, OpenStreetMap, Esri, Dark Matter, Positron e mais).
- **2D / 3D** — alterne entre o globo 3D, uma vista 3D suave e um mapa 2D plano
  nas definições do mapa.
- **Séries temporais** — explore a evolução temporal com a linha temporal,
  quando o conjunto de dados a disponibiliza.

## Acessibilidade e compatibilidade

- **Multiplataforma** — funciona em todos os principais navegadores.
- **Responsivo** — adapta-se a tablets e ecrãs menores.

## Passos seguintes

[Explorar o Catálogo de Dados :octicons-arrow-right-24:](data-catalogue.md){ .md-button .md-button--primary }
[Adicionar dados próprios :octicons-arrow-right-24:](my-data.md){ .md-button }
