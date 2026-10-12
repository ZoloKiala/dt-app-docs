---
title: Assistente Water Copilot
---

# Assistente Water Copilot

O **Water Copilot** é o assistente de IA do portal. Faz uma pergunta sobre a
bacia do Limpopo em linguagem natural e ele responde executando os próprios
serviços de dados do Digital Twin: registos de precipitação, monitorização de
caudais ecológicos, armazenamento em albufeiras, estações de cheias,
contabilidade da água, produtos de satélite e a biblioteca de documentos do
projeto. As respostas chegam como texto, gráficos, tabelas e ligações de
descarga, num painel ao lado do mapa.

É uma forma diferente de chegar aos mesmos dados que o catálogo contém. Onde
o catálogo lhe pede que encontre um conjunto de dados e o adicione como camada,
o assistente permite pedir diretamente o número, o gráfico ou a comparação que
realmente pretende.

<figure markdown="span">
  ![O painel do Water Copilot aberto sobre o mapa](../assets/v2/v2-water-copilot-panel.png)
  <figcaption>Figura 17: O Water Copilot abre no canto inferior direito, com um botão de expansão, um seletor de idioma e um pedido de início de sessão.</figcaption>
</figure>

## Abrir o assistente

Clique no ícone redondo de chatbot no **canto inferior direito do mapa** (a
sua dica de ecrã diz **Open Chatbot**, *Abrir chatbot*). Abre-se um painel
sobre o canto do mapa.

- O botão de **expansão** (⛶) no topo do painel passa para ecrã inteiro;
  clique de novo para voltar ao canto. O **×** fecha o painel.
- O **seletor de idioma** (bandeira e **EN**) no topo do painel alterna o
  assistente entre inglês e português.
- Da primeira vez, o assistente pede-lhe para iniciar sessão (**Sign In**).
  Utilize a mesma conta IWMI Digital Twins com que entrou no portal. Quem
  utiliza pela primeira vez pode registar-se (**Register**) no mesmo ecrã.

!!! info "O painel é separado do mapa"
    Os gráficos, mapas e ficheiros que o assistente produz aparecem dentro do
    painel como imagens e ligações. Não são adicionados ao mapa como camadas.
    Para colocar dados no mapa, utilize o [Catálogo de Dados](data-catalogue.md);
    para analisar uma área desenhada no mapa, utilize as ferramentas de análise
    do grupo **Water Use Monitoring and Analysis** (*Monitorização e análise do
    uso da água*).

## O que pode perguntar

O assistente responde apenas a partir dos serviços de dados do Digital Twin,
pelo que o seu âmbito é o âmbito desses serviços. Em traços largos:

| Tema | O que consegue fazer | Exemplo de pergunta |
| --- | --- | --- |
| Precipitação | Encontrar estações perto de um local e devolver séries históricas e de previsão com um gráfico | *Mostra a precipitação perto de Tzaneen nos últimos seis meses.* |
| Caudais ecológicos | Valores atuais e estado de alerta nos locais de caudal ecológico, gráficos de conformidade, detalhes dos locais | *Que locais de caudal ecológico estão em alerta este mês?* |
| Albufeiras e seca | Encontrar uma barragem pelo nome, estado do armazenamento, gráficos de armazenamento e sazonais, panorama do armazenamento em toda a bacia | *Qual o nível da barragem de Massingir e como se compara este ano?* |
| Cheias | Estações de cheias, classificação da gravidade atual, eventos passados, hidrogramas e períodos de retorno, animações de cheias | *Onde está a ocorrer inundação neste momento na bacia?* |
| Contabilidade da água | Panorama da bacia, balanço hídrico por ano, frações de evapotranspiração, disponibilidade per capita, fecho da bacia, stress ambiental, mapas mensais | *Faz uma análise completa de contabilidade da água da bacia.* |
| Uso da água | Consumo mensal de água das áreas irrigadas em redor de um local | *Quanta água usaram as explorações irrigadas perto de Hoedspruit no ano passado?* |
| Saúde dos rios | Locais MiniSASS de ciência cidadã, pontuações, tendências e painéis | *Que rios têm as melhores pontuações MiniSASS?* |
| Produtos de satélite | Listar produtos do Open Data Cube, as suas datas e bandas, e gerar uma imagem de mapa | *Mostra o mapa mais recente de área irrigada da bacia inferior.* |
| Modelo hidrológico | Caudais mensais simulados por canal pelo modelo SWAT, presente e natural, de 2001 a 2025 | *Compara o caudal presente e natural do canal cha0125 em 2020.* |
| Documentos | Pesquisar a biblioteca de literatura da bacia e os relatórios e publicações do próprio Digital Twin | *O que dizem os relatórios sobre as águas subterrâneas no Limpopo?* |
| Réguas limnimétricas | Ler um nível de água a partir de uma fotografia de uma régua | Anexe a fotografia e indique a estação. |

!!! note "Em desenvolvimento"
    As ferramentas à escala da parcela que refinam a evapotranspiração WaPOR
    de 300 m para 20 m, as mesmas disponíveis no grupo **Water Use Monitoring
    and Analysis** do catálogo, estão a ser ligadas ao assistente. Até lá,
    utilize-as no mapa e não na conversa.

## Como responde

Alguns hábitos estão incorporados, e conhecê-los torna o assistente mais fácil
de utilizar.

- **Procura a resposta em vez de a recordar.** Para qualquer pergunta factual
  ou numérica executa os serviços de dados e apresenta o que devolvem. Se não
  houver dados para o que pediu, di-lo e sugere uma alternativa: outro período,
  uma estação próxima, uma agregação mais grosseira.
- **Os gráficos aparecem na resposta e os dados podem ser descarregados.**
  Quando um serviço produz um gráfico, ele surge na resposta; quando produz um
  ficheiro, recebe uma ligação **Download CSV** (*Descarregar CSV*).
- **Cada análise termina com um resumo, as principais conclusões e uma
  interpretação**, com as unidades e o período abrangido indicados.
- **Pergunta antes de assumir.** Datas, estações, barragens e canais são
  escolha sua, por isso, quando uma pergunta deixa algo em aberto, o
  assistente apresenta as opções e aguarda, em vez de escolher por si.
- **Copy** (*Copiar*) em qualquer resposta copia o texto, ou a imagem, para
  utilizar noutro lado.

## Fazer boas perguntas

- **Indique o local.** Uma vila, um rio, uma barragem ou um regadio chegam. Se
  o assistente pedir coordenadas, indique uma localidade próxima, ou latitude
  e longitude em graus decimais.
- **Indique o período.** Datas no formato `AAAA-MM-DD` funcionam melhor. Para
  produtos mensais, `AAAA-MM` é suficiente.
- **Diga "completa"** quando quiser o quadro inteiro da contabilidade da água;
  o assistente executa então todo o conjunto de análises em vez de uma só.
- **Peça o CSV** quando quiser levar os números consigo.
- **Saiba que dados são atuais.** Valores e alertas de caudal ecológico,
  precipitação, monitorização de cheias e estado das albufeiras são quase em
  tempo real. Produtos de satélite, resultados do modelo SWAT e documentos não
  são, e o assistente indicará o período que utilizou.
- **Seja preciso com o modelo.** Os canais SWAT estão numerados de `cha0002` a
  `cha1436`; utilize o código do canal e não o nome do rio.

## Conversas, comentários e conta

As suas conversas ficam guardadas na sua conta, para poder retomar uma
anterior. Cada resposta tem um **polegar para cima** e um **polegar para
baixo**; utilize-os, com um comentário se quiser, porque as avaliações chegam
à equipa que mantém o assistente e orientam o que ele melhora. Os dados da sua
conta do portal estão em **Account** (*Conta*) na barra superior (ver
[Ajuda e Apoio](help-support.md#conta)).

## Limitações

- O assistente vale o que valem os dados por trás dele. Confirme o período, as
  unidades e a estação ou local utilizados antes de agir com base num valor,
  sobretudo quando ele lhe disse que os dados estavam incompletos.
- O uso de água baseado na evapotranspiração é a água consumida pelas culturas
  e pelo solo, e não a água captada de um rio ou canal. A captação será
  superior.
- Pedidos grandes, muitos meses ou muitas estações de uma vez, demoram mais e
  podem ser truncados. Pergunte por partes se uma resposta parecer cortada.
- Não adiciona camadas ao mapa, não edita a sua área de trabalho nem altera as
  definições do portal.
