# AULA 2 — ANÁLISE MULTIVARIADA DE DADOS E AGRUPAMENTO (K-MEANS)

## APRENDIZADO DE MÁQUINA NÃO SUPERVISIONADO (262GGR6044A) — Graduação em IA, FMU

---

## 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Não Supervisionado (262GGR6044A)
**Aula:** 2 — "Unidade 2"
**Livro-base (parte 1):** *Preparação e Análise Exploratória de Dados* — Rafael Albuquerque (SAGAH), capítulo "Análise multivariada de dados"
**Material complementar (parte 2):** Experimento/Roteiro de laboratório virtual "Machine Learning: Agrupamento das Flores" (sumário teórico baseado em Faceli et al., 2021 e Lenz et al., 2020)

**Objetivos de aprendizagem (da Unidade):**
- Conceituar a análise multivariada.
- Descrever as formas de condução de uma análise multivariada de dados.
- Identificar o tipo de visualização e as respectivas variáveis envolvidas.

**Objetivos do experimento de agrupamento:**
- Reconhecer o que é a tarefa de análise de agrupamentos.
- Reconhecer o funcionamento do algoritmo k-means.
- Identificar as principais métricas para avaliação de resultados do algoritmo a priori.
- Implementar e testar uma versão do algoritmo k-means utilizando a base de dados de flores íris.

---

## 2. Resumo e Contextualização

A Aula 2 tem dois blocos de conteúdo complementares:

1. **Análise multivariada de dados** — fundamentos estatísticos para analisar múltiplas variáveis simultaneamente, dividida em técnicas de dependência (causa-efeito) e interdependência (padrões subjacentes sem variável dependente definida), além de formas de visualização desses dados.
2. **Machine Learning — Agrupamento (clustering)**, com foco no algoritmo **k-means**, primeira técnica de aprendizado não supervisionado detalhada na disciplina em nível de algoritmo e implementação prática (laboratório virtual com o dataset de flores íris).

Esse segundo bloco é o primeiro contato direto da disciplina com uma técnica central de **aprendizado não supervisionado** propriamente dito — o tema que dá nome à disciplina.

---

## 3. Conceitos Fundamentais e Explicações

### 3.1 Conceito de Análise Multivariada de Dados

Segundo Hair et al. (2009), análise multivariada é um conjunto de técnicas estatísticas que são extensões de métodos de análise **univariada** (uma variável) e **bivariada** (duas variáveis). Para um problema ser considerado multivariado, todas as variáveis envolvidas devem ser **aleatórias e relacionadas**, de modo que seus efeitos não sejam interpretados separadamente.

Os dados multivariados podem ser representados como uma **matriz de informações**, em que cada linha é uma amostra de cada variável e **xij** é a medida da variável *j* sobre o item/indivíduo *i*.

#### Conceitos fundamentais

- **Variável estatística:** combinação linear de variáveis, alicerce da análise multivariada. Escrita matemática: `w1·X1 + w2·X2 + w3·X3 + ... + wn·Xn`, onde Xn é a variável observada e wn é o peso determinado pela técnica multivariada.
- **Escalas de medida:**
  - **Métricas:** usadas em quantidade/grau (escalas intervalares e de razão) — permitem o mais alto nível de precisão.
  - **Não métricas:** apontam diferença de tipo/natureza, indicando presença ou ausência de uma característica.
- **Erro de medida:** grau em que os valores observados divergem do valor "verdadeiro"/esperado de uma variável — ligado à imprecisão da coleta.

A análise multivariada se divide em **técnicas exploratórias** (simplificação da estrutura de variabilidade dos dados) e **técnicas de inferência**.

---

### 3.2 Formas de Condução da Análise Multivariada

Duas categorias, segundo o tipo de relacionamento entre as variáveis:

#### Técnicas de Dependência
Uma variável (ou conjunto) é **dependente** de outras (**independentes**), em relação de causa-efeito. Buscam descrever ou prever valores.

> **Atenção, inconsistência do capítulo *(complementação)*:** em uma passagem, o capítulo diz que as variáveis *independentes* são as que o modelo tentará prever ou explicar, e que as *dependentes* são as que afetam as independentes. Isso está **invertido** em relação à definição padrão: a **dependente** é a prevista ou explicada, e as **independentes** a explicam. Use a definição padrão, que é a coerente com os exemplos do próprio capítulo (ex.: despesas com jantares como dependente).

| Técnica | Quando usar | Exemplo teórico (livro) | Exemplo real de aplicação *(complementação)* |
|---|---|---|---|
| **Regressão múltipla** | Quando há **uma única variável dependente métrica**, relacionada a duas ou mais variáveis independentes métricas, e o objetivo é prever/explicar mudanças nela. | Despesas mensais com jantares fora (dependente) previstas por renda familiar, tamanho da família e idade do chefe de família (independentes). | Imobiliárias estimando o preço de um imóvel (dependente) a partir de metragem, nº de quartos, distância do centro e idade do imóvel (independentes). |
| **Análise conjunta** | Quando se quer avaliar a **importância de atributos e seus níveis** na aceitação de um produto/serviço/ideia, testando combinações de variáveis não métricas. | Avaliação de aceitação de novos produtos/serviços. | Empresas de eletrônicos testando combinações de cor, capacidade de bateria e preço para definir a configuração "ideal" de um novo smartphone. |
| **Análise discriminante múltipla (MDA)** | Quando a variável dependente é **não métrica**, dicotômica ou multicotômica, e o objetivo é classificar entidades em grupos conhecidos. | Distinguir consumidores de marcas nacionais x importadas. | Bancos classificando solicitantes de crédito em "aprovado" x "negado" com base em renda, histórico e idade. |
| **MANOVA / MANCOVA** | Quando há **várias variáveis independentes não métricas** (tratamentos) e **duas ou mais variáveis dependentes métricas** a serem analisadas simultaneamente. | Explorar relações entre tratamentos categóricos e variáveis métricas. | Indústria farmacêutica avaliando o efeito de diferentes dosagens de um medicamento (tratamento) sobre pressão arterial e frequência cardíaca (duas dependentes) ao mesmo tempo. |
| **Análise de correlação canônica** | Quando se quer correlacionar simultaneamente **diversas** variáveis dependentes métricas com **diversas** variáveis independentes métricas. | Obter pesos que maximizem a correlação entre os dois conjuntos de variáveis. | Estudos de RH relacionando um conjunto de indicadores de satisfação no trabalho com um conjunto de indicadores de desempenho (produtividade, absenteísmo, qualidade). |
| **Modelagem de equações estruturais** | Quando o problema envolve **várias variáveis dependentes** inter-relacionadas, exigindo várias regressões múltiplas estimadas ao mesmo tempo. | Estimação conjunta de várias equações de regressão. | Pesquisas de marketing testando, em um único modelo, como marca, qualidade percebida e preço influenciam simultaneamente satisfação e lealdade do cliente. |

#### Técnicas de Interdependência
Nenhuma variável é definida como dependente/independente — todas são analisadas simultaneamente para entender **padrões subjacentes** aos dados, sem suposições prévias sobre as variáveis.

| Técnica | Quando usar | Exemplo teórico (livro) | Exemplo real de aplicação *(complementação)* |
|---|---|---|---|
| **Análise fatorial** | Quando há muitas variáveis correlacionadas entre si e se quer **reduzir a dimensionalidade**, condensando-as em fatores/componentes menores. | *(não detalhado no capítulo-base desta aula — ver comparação PCA x Análise Fatorial na Aula 3)* | Pesquisas de satisfação com dezenas de perguntas sendo reduzidas a poucos "fatores" latentes (ex.: "atendimento", "preço", "qualidade do produto"). |
| **Análise de cluster (agrupamento)** | Quando se quer **classificar entidades em grupos não predefinidos**, com base apenas em similaridade entre elas. | Reconhecimento de grupos de consumidores com características semelhantes. | Plataformas de streaming agrupando usuários por padrão de consumo para gerar recomendações (conecta com o algoritmo k-means da seção 3.4). |
| **Escala multidimensional** | Quando o objetivo é **mapear percepções** de similaridade/preferência em um espaço multidimensional, sem dados métricos diretos. | Detectar produtos com perfil de consumidor semelhante. | Pesquisas de posicionamento de marca, mapeando como consumidores percebem a proximidade entre marcas concorrentes (ex.: Coca-Cola x Pepsi x marcas próprias). |
| **Análise de correspondência** | Quando se quer mapear a relação entre **variáveis não métricas categóricas**, algo que outras técnicas interdependentes não cobrem. | Correlacionar marcas de celular com perfis de consumidores (adolescentes, adultos, idosos). | Pesquisas eleitorais relacionando partido/candidato (categórico) com faixa etária ou região (categórico), identificando associações visuais em um mapa de correspondência. |

**Critério de escolha da técnica:** a natureza dos dados (métrica ou não métrica) é um dos principais fatores. Dados métricos: diferem em quantia/grau (idade, temperatura, lucro). Dados não métricos: diferem em tipo/natureza (tamanho da casa: pequeno/médio/grande).

> Os exemplos marcados como *(complementação)* são aplicações de mercado acrescentadas para fixação — não constam no capítulo-base e não devem ser atribuídos ao professor ou ao livro.

#### 3.2.1 Problema → Técnica → Por quê *(complementação — cenários de vida real)*

> Cenários acrescentados para fixação. As técnicas e suas condições de uso seguem o capítulo-base (Hair et al., 2009); os problemas são ilustrativos.

**Primeiro, como decidir (roteiro de 3 perguntas):**
1. Existe uma variável "alvo" que quero prever ou explicar? **Sim → dependência. Não → interdependência.**
2. A variável alvo (e as explicativas) são **métricas** (números com quantidade/grau) ou **não métricas** (categorias)?
3. Quantas variáveis alvo? **Uma** ou **várias**?

##### Técnicas de dependência

**1. Regressão múltipla**
- **Imagine que** uma rede de restaurantes quer prever o faturamento mensal de cada loja nova.
- **Variáveis:** faturamento (alvo, métrica); população do bairro, ticket médio, nº de concorrentes próximos (explicativas, métricas).
- **Técnica:** regressão múltipla.
- **Porque:** há **uma única** variável alvo métrica e **várias** explicativas métricas, e o objetivo é prever a magnitude do valor.

**2. Análise conjunta**
- **Imagine que** um fabricante de notebooks quer saber o que mais pesa na decisão de compra (marca, memória RAM, preço, cor) sem precisar lançar todas as combinações no mercado.
- **Técnica:** análise conjunta.
- **Porque:** ela testa combinações de níveis de atributos não métricos, observa a preferência (dependente) em cada uma e revela a **importância de cada atributo e de cada nível**, economizando recursos.

**3. Análise discriminante múltipla (MDA)**
- **Imagine que** um banco precisa classificar um solicitante de crédito como "bom pagador" ou "mau pagador".
- **Variáveis:** classe (alvo, **não métrica** dicotômica); renda, idade, nível de endividamento (explicativas, métricas).
- **Técnica:** análise discriminante múltipla.
- **Porque:** o alvo é categórico com grupos **já conhecidos** e o objetivo é prever a que grupo uma nova pessoa pertence. *(É a lógica de classificação supervisionada.)*

**4. MANOVA / MANCOVA**
- **Imagine que** uma escola testa três métodos de ensino e quer comparar o efeito deles sobre a nota de matemática **e** a de português ao mesmo tempo.
- **Técnica:** MANOVA.
- **Porque:** a variável explicativa é categórica (método de ensino) e há **duas ou mais dependentes métricas** analisadas simultaneamente. Se também fosse preciso descontar o efeito da nota anterior dos alunos (uma covariável não controlada), usaria-se a **MANCOVA**.

**5. Correlação canônica**
- **Imagine que** uma empresa quer entender como um conjunto de hábitos de estudo dos alunos (horas por semana, frequência, acessos à plataforma) se relaciona com um conjunto de resultados (notas em várias disciplinas).
- **Técnica:** análise de correlação canônica.
- **Porque:** há **vários** indicadores de cada lado, todos métricos, e o interesse é a correlação máxima entre os **dois conjuntos**. Na regressão múltipla, o lado do alvo teria uma única variável.

**6. Modelagem de equações estruturais**
- **Imagine que** uma operadora quer testar, em um único modelo, como qualidade do atendimento e preço influenciam a satisfação, e como a satisfação influencia a lealdade e a recompra.
- **Técnica:** modelagem de equações estruturais.
- **Porque:** existem **várias relações encadeadas**, em que uma variável explica outra que por sua vez explica uma terceira. Um conjunto de regressões múltiplas é estimado **ao mesmo tempo**.

##### Técnicas de interdependência

**7. Análise fatorial**
- **Imagine que** uma pesquisa de clima organizacional tem 40 perguntas, muitas respondidas de forma parecida entre si.
- **Técnica:** análise fatorial.
- **Porque:** não há variável alvo e há muitas variáveis correlacionadas. Ela as condensa em poucos fatores (ex.: "liderança", "remuneração", "ambiente"), deixando o padrão menos diluído. *(Conecta com PCA x FA da Aula 3.)*

**8. Análise de cluster (k-means)**
- **Imagine que** um e-commerce quer segmentar sua base de clientes, mas ninguém definiu antes quais seriam os segmentos.
- **Técnica:** análise de cluster, por exemplo com o **k-means** (seção 3.4).
- **Porque:** os grupos **não são predefinidos** e precisam emergir da similaridade entre os clientes. É a diferença-chave para a discriminante (problema 3), em que os grupos já existem.

**9. Escala multidimensional**
- **Imagine que** uma cervejaria quer descobrir quais marcas os consumidores percebem como "parecidas" com a sua.
- **Técnica:** escala multidimensional (mapeamento perceptual).
- **Porque:** os dados são **julgamentos de similaridade ou preferência**, que a técnica converte em distâncias num mapa. Marcas próximas no mapa competem pelo mesmo perfil de consumidor.

**10. Análise de correspondência**
- **Imagine que** uma fabricante de celulares quer ver quais marcas se associam a quais faixas etárias (adolescente, adulto, idoso).
- **Técnica:** análise de correspondência.
- **Porque:** as duas variáveis são **categóricas (não métricas)** e o objetivo é um mapa de associação entre elas, algo que as outras técnicas de interdependência não fazem.

##### Confusões frequentes (e como desfazer)

| Dúvida | Como diferenciar |
|---|---|
| Discriminante x Cluster | Discriminante: grupos **já conhecidos**, prevê a classe. Cluster: grupos **desconhecidos**, descobre os grupos. |
| Regressão múltipla x Correlação canônica | Regressão: **uma** dependente métrica. Canônica: **várias** dependentes métricas. |
| Análise fatorial x Cluster | Fatorial agrupa **variáveis** (colunas). Cluster agrupa **indivíduos/objetos** (linhas). |
| Dependência x Interdependência | Há variável alvo? Sim → dependência. Não → interdependência. |

---

### 3.3 Tipos de Visualização de Dados Multivariados

Usando como exemplo a base de dados de **qualidade de vinhos** (branco/tinto), com atributos como acidez fixa, acidez volátil, ácido cítrico, açúcar residual, cloretos, dióxido de enxofre (livre/total), densidade, sulfatos, álcool e qualidade.

Ferramentas Python citadas: **Pandas** (leitura), **Matplotlib** (plotagem) e **Seaborn** (personalização).

| Tipo de visualização | Uso |
|---|---|
| **Histograma (1D)** | Distribuição dos valores de cada atributo isoladamente |
| **Matriz de correlação (heatmap)** | Correlação entre todos os atributos simultaneamente, via gradiente de cor |
| **Gráfico de dispersão (scatter)** | Bicorrelação entre pares de atributos |
| **Scatter 3D** | Comparação de grupos (ex.: vinho branco x tinto) considerando uma terceira dimensão |
| **Scatter 3D com profundidade** | Dados contínuos em três eixos (largura, comprimento, profundidade) |
| **Gráfico de barras com matiz (hue) e facetas** | Três categorias com valores discretos, usando tonalidade e subparcelas para suportar a terceira dimensão |
| **Gráfico de densidade** | Forma da distribuição dos dados (ex.: nível de sulfato em vinho branco x tinto) |

Também são mencionadas visualizações em **4D e 6D** para perspectivas adicionais.

---

### 3.4 Machine Learning — Agrupamento (Clustering)

**Definição:** técnica **não supervisionada** de machine learning que, a partir de dados **não rotulados**, encontra estrutura interna na forma de grupos (clusters), de acordo com características/atributos em comum (Almeida, Carvalho e Menino, 2020).

**Aplicações citadas:** sistemas de recomendação (produtos, filmes/séries por streaming), segmentação de mercado, análise de dados estatísticos, análise de redes sociais, segmentação de imagem, detecção de anomalias.

#### Três estratégias principais de agrupamento

| Estratégia | Como funciona |
|---|---|
| **Por partição** | Cria partições no espaço dos dados; cada partição é um cluster; cada dado pertence a **um único** cluster |
| **Hierárquico** | Agrupa de forma hierárquica — top-down (de um grande grupo para menores) ou bottom-up (de um grupo por dado para grupos maiores). Um cluster pode conter outros menores; um dado pode pertencer a mais de um cluster simultaneamente |
| **Por densidade** | Forma grupos com base em regiões de alta densidade de dados, separando-as de regiões de baixa densidade |

#### As cinco etapas da tarefa de agrupamento

1. **Preparação dos dados de entrada:** normalização, transformação e limpeza dos dados.
2. **Definição da medida de proximidade:** escolha de função de similaridade/dissimilaridade conforme o contexto e o tipo de dado.
3. **Agrupamento dos dados:** aplicação do algoritmo.
4. **Validação:** análise dos resultados gerados.
5. **Interpretação dos resultados:** etapa mais subjetiva — compreender e descrever a relação entre elementos de um mesmo cluster.

#### Algoritmo k-means

Algoritmo de **agrupamento por partição**, simples e muito utilizado (Faceli et al., 2021). Particiona o conjunto de dados em **k** clusters (k definido pelo usuário), com base em uma medida de similaridade — comumente a **distância euclidiana**.

**Funcionamento (resumo):**
1. Escolhem-se **k pontos (centroides)** no espaço, normalmente inicializados de forma aleatória.
2. Cada dado é atribuído ao cluster do centroide mais similar (menor distância).
3. Os centroides são **recalculados** com base nos dados atribuídos.
4. Cada dado tem sua similaridade recalculada e pode ser realocado para outro cluster.
5. O processo se repete até que **não haja mais mudanças nos centroides** (convergência) ou se atinja o número máximo de iterações definido.

> *(Pseudocódigo do algoritmo k-means apresentado na Figura 2 do material — Lenz et al., 2021, p. 51; e exemplo visual de execução com k=4 e seis iterações até a convergência — Figura 3, fonte Agor153, 2012.)*

**Ponto-chave conceitual (do pré-teste/pós-teste):** como é não supervisionado, o k-means **não utiliza rótulos** — o próprio objetivo é encontrar relações/agrupamentos desconhecidos nos dados. No dataset de flores íris, por exemplo, o atributo "tipo de flor" (rótulo) **não é usado** no agrupamento, justamente por ser a técnica não supervisionada.

---

## 4. Exemplos, Aplicações e Material Prático

### Experimento de laboratório virtual: "Agrupamento das Flores"

- **Dataset:** flores íris (três espécies), descrito por atributos de largura/comprimento de pétala e sépala, além do atributo "tipo de flor" (não usado no agrupamento).
- **Procedimento:** configurar a simulação, selecionar K=2 (e depois outros valores de K), randomizar posição inicial dos centroides, executar o algoritmo passo a passo, analisar zonas de cada centroide, repetir para outros conjuntos de dados.
- **Perguntas de avaliação do experimento (roteiro):**
  1. Qual a consequência de variar as posições iniciais dos centroides?
  2. Qual seria o K otimizado para o conjunto de dados escolhido?
  3. Qual seria a posição final dos centroides com esse K otimizado, considerando a influência das condições iniciais no resultado final?

*(O experimento em si é interativo, hospedado na plataforma de ensino — não reproduzido aqui; registro apenas do roteiro e perguntas.)*

### Questões de fixação (não avaliativas) — Pré-teste e Pós-teste de Machine Learning

> Preservadas como estavam no material, sem gabarito (não fornecido no documento-fonte). Útil para revisão/simulado.

**Pré-teste (5 questões, resumo dos temas):** estratégias de agrupamento (partição x densidade x hierárquico); ordem das 5 etapas do agrupamento; diferença entre aprendizado supervisionado e não supervisionado; objetivo da função de proximidade no k-means; k-means como técnica que busca relações desconhecidas em dados não rotulados.

**Pós-teste (5 questões, resumo dos temas):** condição de parada do k-means (convergência dos centroides); por que o dataset íris busca 3 clusters (3 valores do atributo tipo de flor); afirmações sobre k-means (maximizar similaridade intragrupo/minimizar intergrupo; algoritmo de partição); por que o atributo "tipo de flor" não é usado no aprendizado não supervisionado (é o rótulo); tarefa que o k-means resolve (segmentar compradores em grupos de perfis, por exemplo).

*(Os enunciados completos com as 3 alternativas de cada questão estão no PDF original, caso queira revisá-los na íntegra antes de um simulado.)*

### Atividade 2 (A2): 5 questões avaliativas e gabarito

> A plataforma não mostra o gabarito. O gabarito abaixo foi deduzido do capítulo e **conferido pela pontuação** (3 de 5 acertos). Enunciados completos no PDF da unidade.

| Questão | Tema | Resposta marcada | Correta | Situação |
|---|---|---|---|---|
| 1 | Conceito de técnicas de dependência | E | **B** | ✗ |
| 2 | Regressão múltipla × correlação canônica | E | **E** | ✓ |
| 3 | Conceito de análise multivariada | C | **C** | ✓ |
| 4 | Variável estatística e escalas de medida | C | **C** | ✓ |
| 5 | Melhor representação da correlação entre todos os atributos | D | **B** | ✗ |

**Q1:** a técnica de dependência tem uma variável (ou conjunto) **dependente**, prevista ou explicada pelas **independentes** (B). As alternativas A e D descrevem técnicas de **interdependência**. A alternativa C é a mais confusa: ela chama as variáveis dependentes de "as técnicas" (erro de formulação) e reproduz a frase do capítulo com os papéis em ordem oposta à da passagem invertida do livro (ver o aviso na seção 3.2). Os papéis que ela atribui seguem a definição padrão, mas a frase está mal construída, e a B é a definição direta. Regra: **dependência tem variável alvo; interdependência não tem**.

**Q5:** o **heatmap** (matriz de correlação) cruza todos os atributos com todos e mostra a correlação pelo gradiente de cor (B). O gráfico de **densidade** (D) mostra a forma da distribuição de uma variável, não correlação. A alternativa E está errada porque o heatmap cobre todos os pares.

**Regra rápida:** histograma e densidade mostram **uma variável**; scatter mostra **um par**; heatmap mostra **todas contra todas**.

---

## 5. Minhas Observações e Dúvidas

*(Aguardando — Dani ainda não leu o material no momento do envio. Espaço reservado para observações a incluir via "Atualizar aula".)*

---

## 6. Referências e Conexões com Outros Conteúdos

**Livro-base (parte 1 — Análise Multivariada):**
ALBUQUERQUE, R. *Preparação e análise exploratória de dados* — capítulo "Análise multivariada de dados". SAGAH.

**Referências citadas no capítulo:**
- ESTATÍSTICA e matrizes. [S. l., 201-?].
- HAIR, J. F. et al. *Análise multivariada de dados*. 6. ed. Porto Alegre: Bookman, 2009.
- KUMAR, S.; SINGH, S. K.; MISHRA, P. Multivariate analysis: an overview. *Journal of Dentofacial Sciences*, v. 2, n. 3, p. 19–26, 2013.
- SARKAR, D. The art of effective visualization of multi-dimensional data. *Towards Data Science*, 2018.
- VIALI, L. *Série estatística multivariada: introdução*. [S. l., 199-?].

**Leitura recomendada:** LEONI, R. C.; SAMPAIO, N. A. de S.; CORREA, S. M. Estatística multivariada aplicada ao estudo da qualidade do ar. *Revista Brasileira de Meteorologia*, v. 32, n. 2, p. 235–241, 2017.

**Material complementar (parte 2 — Agrupamento/k-means):**
- ALMEIDA, A.; CARVALHO, F.; MENINO, F. *Introdução ao machine learning*. GitHub, 2020.
- FACELI, K. et al. *Inteligência artificial: uma abordagem de aprendizado de máquina*. São Paulo: LTC, 2021.
- LENZ, M. L. et al. *Fundamentos de aprendizagem de máquina*. Porto Alegre: Sagah, 2020.
- AGOR153. K-means convergence to a local minimum. *Wikimedia Commons*, 2012.

**Conexões com a disciplina anterior (Aquisição e Preparação de Dados — 262GGR6046A):**
- A etapa 1 do agrupamento ("preparação dos dados de entrada: normalização, transformação e limpeza") retoma diretamente os conceitos de ETL e normalização vistos naquela disciplina.

**Conexões internas à disciplina:**
- **Análise fatorial** (técnica de interdependência, Aula 2) se conecta com a comparação **PCA x Análise Fatorial** da Aula 3 — ambas tratam de redução de dimensionalidade.
- **Análise de cluster** (Aula 2, nível conceitual) é expandida em profundidade técnica no experimento de **k-means** — primeiro algoritmo de aprendizado não supervisionado tratado com pseudocódigo e implementação prática na disciplina.
- O **aprendizado não supervisionado** (ML, visto na Aula 1 via livro de Engenharia do Conhecimento) ganha aqui seu primeiro algoritmo concreto (k-means), confirmando-se como eixo central da disciplina.
