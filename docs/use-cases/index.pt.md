---
title: Casos de Uso
---

# Casos de Uso

O [Guia do Utilizador](../guide/index.md) explica o que faz cada comando. Estas
páginas mostram como **responder a uma pergunta real** com o portal, do início ao
fim — que conjuntos de dados abrir, por que ordem, e como interpretar o que vê.

Todos os conjuntos de dados aqui referidos existem hoje no catálogo do portal.
Os nomes são escritos exatamente como aparecem em **Explore data**, para que os
possa encontrar com **Search the catalogue**.

<div class="grid cards" markdown>

-   :material-sprinkler-variant: **[Uso de água na irrigação](irrigation.md)**

    Onde está a irrigação a expandir-se, e quanta água consome?

-   :material-waves: **[Cheias](floods.md)**

    Está a formar-se uma cheia, onde atingirá o pico, e quem está exposto?

-   :material-weather-sunny-alert: **[Secas](droughts.md)**

    Qual o stress da vegetação, dos solos e dos rios, e qual a perspetiva?

-   :material-fish: **[Caudais ecológicos](eflows.md)**

    Os rios estão a receber o caudal de que os ecossistemas precisam?

-   :material-water-check: **[Monitorização de albufeiras](reservoirs.md)**

    Quão cheias estão as barragens, e como evoluem os níveis?

-   :material-scale-balance: **[Contabilidade da água](water-accounting.md)**

    De onde vem a água da bacia, e para onde vai?

</div>

## Como cada caso de uso está organizado

| Secção | O que lhe dá |
| --- | --- |
| **A pergunta** | Quem pergunta, a decisão que precisa de tomar e com que frequência consulta |
| **Em resumo** | Os números-chave da bacia hoje, obtidos da API de dados do portal |
| **Como se encadeia o fluxo de trabalho** | Um diagrama dos conjuntos de dados e dos pontos de decisão |
| **Dados a utilizar** | Os conjuntos de dados exatos, onde estão, e o que cada um indica |
| **Percurso** | Passos numerados, com os nomes dos botões do portal |
| **Interpretar os gráficos** | Gráficos reais construídos a partir das mesmas séries que o portal mostra ao clicar numa estação ou barragem, e o que procurar |
| **Indicadores e o que fazer** | Limiares e a ação que normalmente desencadeiam |
| **Exemplo prático** | O fluxo de trabalho aplicado a uma situação real, com os números |
| **Lista de verificação** | O que um relatório desta análise deve conter |
| **Limites a ter em conta** | Latência, pressupostos dos modelos e cobertura — para não sobreinterpretar os dados |

!!! info "Sobre os gráficos"
    Os gráficos destas páginas são os do próprio portal: capturas do cartão
    **Feature Information** e do painel **Charts** (botão **Expand**) para
    estações, barragens e locais reais, obtidas do catálogo de produção em
    setembro de 2026. Onde o contexto de longo prazo ajuda, um bloco recolhido
    acrescenta gráficos gerados a partir das mesmas séries da API
    (`api.digitaltwins.iwmi.org`) — identificados como derivados, não ecrãs do
    portal. Os rótulos estão em inglês. Os diagramas de fluxo e as tabelas de
    indicadores são orientações, não regras operacionais oficiais; confirme os
    limiares com os procedimentos da sua instituição.

!!! tip "Guarde a sua análise como uma história"
    Quando tiver uma vista que responde à sua pergunta, use **Story → Capture
    Scene** para registar as camadas, o tempo e a câmara, e depois
    **Share / Print** para entregar aos colegas uma única ligação que a reproduz.
    Ver [Histórias e Partilha](../guide/sharing.md).

!!! note "Alguns gráficos exigem sessão iniciada"
    Os gráficos de estações e locais (caudal, precipitação, caudal ecológico,
    previsões de albufeiras) são servidos pela API de dados do IWMI e exigem que
    tenha sessão iniciada. As camadas do mapa funcionam em qualquer caso.
