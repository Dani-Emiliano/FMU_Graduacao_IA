# AULA 3 — ANÁLISE DE COMPONENTES PRINCIPAIS (PCA) E TRATAMENTO DE OUTLIERS

## APRENDIZADO DE MÁQUINA NÃO SUPERVISIONADO (262GGR6044A) — Graduação em IA, FMU

---

## 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Não Supervisionado (262GGR6044A)
**Aula:** 3 — "Unidade 3"
**Livros-base:**
- *Aprendizado de Máquina* — Juliane Soares, capítulo "Análise de componentes principais".
- *Preparação e Análise Exploratória de Dados* — Leandro Botelho Alves de Miranda, capítulo "Tratando outliers em Pandas e Numpy".

**Objetivos de aprendizagem da Unidade:**
- Conceituar a análise de componentes principais (PCA).
- Descrever a metodologia da PCA.
- Identificar aplicações da PCA no contexto de aprendizagem de máquina.
- Definir outliers.
- Identificar outliers usando intervalo interquartis e box-plots.
- Determinar a remoção, ou não, de outliers conforme as características da base de dados.

---

## 2. Resumo e Contextualização

A Aula 3 reúne dois temas de preparação e redução de dados:

1. **PCA** — técnica de redução de dimensionalidade que concentra a informação de muitas variáveis em poucos componentes não correlacionados. É a continuação direta da comparação PCA × Análise Fatorial (infográfico desta unidade) e da análise fatorial vista na Aula 2.
2. **Outliers** — como defini-los, identificá-los (intervalo interquartil, box-plot, distância de Mahalanobis) e decidir se devem ser removidos. Retoma o tratamento de outliers visto na disciplina anterior (Aquisição e Preparação de Dados, Aula 4), agora com implementação em Python.

**Aprofundamento:** a PCA recebe tratamento detalhado na seção **3.9** (teoria, matemática, exemplo numérico, critérios, limitações, uso no aprendizado supervisionado), a pedido da Dani, porque o tema reaparece com frequência na disciplina de Aprendizado Supervisionado. A execução prática está no pacote `aula03_vscode/` (seção 4.6).

**Ponto de ligação entre os dois temas:** a PCA é sensível à escala das variáveis, e outliers distorcem médias e variâncias. Por isso, limpeza e padronização vêm antes da PCA.

---

## 3. Conceitos Fundamentais e Explicações

### 3.1 PCA × Análise Fatorial *(infográfico da unidade)*

Ambas são técnicas de **redução de dimensionalidade**, com a mesma função geral: minimizar a perda de informação no reconhecimento de padrões.

| Aspecto | PCA | Análise Fatorial (FA) |
|---|---|---|
| **Significado** | Componente: nova dimensão em que as variáveis derivadas são linearmente independentes entre si | Fator: elemento comum (subjacente) em que diversas variáveis se correlacionam |
| **Função** | Decompõe os dados em menores quantidades de componentes | Entende como os fatores capturam grande parte da informação de um conjunto de variáveis |
| **Suposição** | Identifica dimensões compostas dos preditores observados | Pressupõe que os fatores existem nos dados fornecidos |
| **Objetivo** | Explicar o máximo possível de variância cumulativa nos preditores/variáveis | Explicar covariâncias/correlações entre as variáveis |
| **Variação explicada** | Componentes explicam toda a variação nos dados | Fatores não são diretamente mensuráveis; há um termo de erro único para cada variável |
| **Processo** | Componentes = combinações lineares das variáveis originais | Variáveis originais = combinações lineares dos fatores |
| **Representação** | Y = W1·PC1 + W2·PC2 + ... + W10·PC10 | X1 = W1·F + e1; X2 = W2·F + e2... (F = fator, W = peso, e = erro) |
| **Interpretação dos pesos** | Correlação entre escores padronizados dos preditores e os componentes | Associação de cada variável com o fator subjacente (coeficientes de regressão padronizados) |
| **Estimativa dos pesos** | Matriz de correlação → autovetores estimados como coeficientes | Determinados pelo processo de análise fatorial |
| **Hierarquia** | Primeiro as variáveis, depois os pesos por regressão | Primeiro os fatores, depois os retornos dos fatores por regressão |

**Quando usar qual:** PCA para reduzir preditores correlacionados a um conjunto menor; FA para entender e testar fatores latentes que causam variação nos dados.

---

### 3.2 PCA — Conceitos Básicos *(livro-base: Soares)*

- **Extração de características:** processamento que mapeia um espaço de alta dimensão em um de baixa dimensão com perda mínima de informação (Kong; Hu; Duan, 2017). A PCA é uma das técnicas mais usadas para isso.
- **Componentes principais:** direções em que ocorrem as maiores variações dos dados, correspondendo aos **autovetores associados aos maiores autovalores**.
- A PCA identifica o **menor número de variáveis não correlacionadas** a partir de um conjunto maior, enfatizando a variação e capturando padrões **fortes** (não os fracos).
- É um método **não paramétrico**, usado em modelos preditivos e análise exploratória, compressão de imagens, reconhecimento facial, neurociência e computação gráfica.
- Serve para reduzir o número de preditores quando há muitos em relação às observações e para **evitar multicolinearidade** (preditores correlacionados entre si, ou seja, fatores redundantes).
- Usa **transformação ortogonal**. O número de componentes deve ser menor ou igual ao menor número de observações. É **sensível ao dimensionamento** (escala) das variáveis originais.
- Fundamenta-se em métodos de projeção: encontra linhas, planos e hiperplanos que aproximam os dados no sentido de **mínimos quadrados**, maximizando a variância ao longo do novo eixo.
- **Escala automática:** subtrair a média de cada variável e dividir pelo desvio-padrão. Matematicamente, equivale a uma decomposição em autovetores da matriz de covariância.

**Termos-chave:**

| Termo | Significado |
|---|---|
| **Variância** | Variação dos pontos de dados distribuídos no espaço |
| **Covariância** | Grau em que variáveis se movem na mesma direção; revela dependências entre características |
| **Autovetor (eigenvector)** | Direção do eixo (componente); compreende as alterações nos dados |
| **Autovalor (eigenvalue)** | Variância transportada em uma direção específica |
| **Componentes principais** | Novo conjunto de variáveis, independentes, que retêm a informação importante das originais |

**Propriedades dos componentes principais:** são projeções em diferentes direções; reduzem dimensionalidade; são **ortogonais**; o primeiro tem sempre a **maior variância** e o último a menor.

---

### 3.3 PCA — Metodologia (passo a passo)

Segundo Jaadi (2021) e Vasconcelos ([200-?]):

1. **Obter o conjunto de dados.**
2. **Padronizar** as variáveis contínuas. Sem isso, variáveis com intervalos maiores dominam as de intervalos menores e geram resultados tendenciosos.
   - Média: μ = (Σ xᵢ) / n
   - Desvio-padrão: σ = √( Σ (xᵢ − μ)² / n )
   - Padronização: z = (x − μ) / σ
3. **Calcular a matriz de covariância** (simétrica d × d, d = nº de dimensões). A diagonal principal traz a variância de cada variável (Cov(x,x) = Var(x)). Sinal positivo: variam juntas; negativo: inversamente correlacionadas. Variáveis muito correlacionadas contêm informação redundante.
   - Covariância: Cov(w,x) = Σ (wᵢ − w̄)(xᵢ − x̄) / (n − 1)
4. **Calcular autovetores e autovalores** da matriz de covariância M. Eles vêm sempre em **pares**. Autovetores definem as direções dos eixos com mais informação (os componentes); autovalores definem a variância transportada por cada um.
   - Mv = λv, que leva a (M − λI)v = 0 e, para v ≠ 0, det(M − λI) = 0.
5. **Ordenar os autovalores** em ordem decrescente: o maior corresponde ao 1º componente principal, e assim por diante.
6. **Calcular a variância explicada:** autovalor de cada componente ÷ soma dos autovalores.
7. **Decidir quantos componentes manter**, considerando a informação perdida nos descartados. Com os mantidos, forma-se a **matriz de vetores** (feature vector).

> Observação sobre as fórmulas: no PDF original elas aparecem como imagens. Aqui estão em notação padrão, de acordo com o que o texto descreve.

**Característica do resultado:** o novo conjunto tem componentes **não correlacionados**, com os mais informativos no início. Poucos componentes podem expressar **até 95%** da informação original (Mueller; Massaron, 2016).

---

### 3.4 PCA — Aplicações

| Área | Aplicação (livro) |
|---|---|
| **Neurociência** | Identificar propriedades de estímulos que aumentam a probabilidade de disparo de um neurônio; identificar o neurônio pela forma do potencial de ação; detectar atividade coordenada de grandes conjuntos neuronais |
| **Finanças quantitativas** | Redução de dimensionalidade de problemas complexos; análise da curva de juros; cobertura de carteiras de renda fixa; modelos de taxas de juros; previsão de retornos; alocação de ativos; algoritmos de negociação |
| **Compressão de imagem** | Algoritmo de compressão de baixas perdas, mantendo a qualidade próxima da original |
| **Reconhecimento facial** | Geração do conjunto de **Eigenfaces** a partir de imagens de rostos, reduzindo a complexidade estatística da representação |

**Estudo de caso do livro: PCA na evolução temporal da covid-19** (Nobi; Tuhin; Lee, 2021)
- Séries diárias de óbitos e casos confirmados de **25 países**, de abril/2020 a fevereiro/2021, em janelas de um mês.
- Analisaram-se o **1º e o 2º maiores autovalores** e seus autovetores. Autovalor alto significa maior semelhança (correlação) entre os países mais afetados. O pico do 1º autovalor ocorreu em abril de 2020, quando o vírus se espalhou mundialmente.
- Os **coeficientes de PC** (correlação entre componentes e a variação normalizada de casos/óbitos) projetados em PC1 × PC2 mostram onde os países se posicionam. Países **distantes da origem** viveram momentos críticos; países **agrupados** tinham situações semelhantes; países **próximos da origem** tinham bons cenários.
- Conclusão do livro: a PCA permitiu identificar os países mais gravemente afetados e apoiar a previsão da transmissão de doenças.

---

### 3.5 Outliers — Conceito *(livro-base: Miranda + infográfico)*

- **Outlier:** ponto de dados diferente dos demais. Também chamado de anormalidade, discordante, desviante ou anomalia (Aggarwal, 2015). Tem efeito desproporcional em estatísticas como a média, podendo levar a **interpretações enganosas**.
- **Ruído × outlier:** ruído são exemplos errados (ruído de classe) ou erros nos valores dos atributos. Outlier é um conceito **mais amplo**: inclui erros, mas também dados discordantes que surgem de **variação natural** da população ou do processo. Por isso, outliers frequentemente trazem informação útil.
- **Causas (infográfico):** erro de medição ou de entrada; corrupção de dados; valores discrepantes **reais** (ex.: desempenho acima do normal de um atleta). O livro acrescenta falhas mecânicas, mudanças no comportamento do sistema, comportamento fraudulento e erro do instrumento.
- **Aplicações da detecção:** controle de fraudes, detecção de intrusão, detecção de robôs na web, previsão do tempo, aplicação da lei, diagnósticos médicos.
- **Univariado × multivariado:** no univariado, valores muito grandes ou muito pequenos nas caudas da distribuição são outliers. No multivariado, outliers são amostras com **combinações incomuns** no espaço multidimensional; o valor pode parecer normal em cada dimensão isolada.
- **Não há maneira precisa de definir outliers** em geral (infográfico): é preciso interpretar as observações e decidir se o valor é atípico ou não.

### 3.6 Método do Intervalo Interquartil (IQR) e Box-plot

- **Q1** = 25º percentil; **Q3** = 75º percentil; **IQR = Q3 − Q1**.
- O **box-plot** usa mediana, quartis, mínimo e máximo: caixa entre Q1 e Q3, linha da mediana dentro dela, "bigodes" até o mínimo/máximo e pontos isolados para os outliers.

**Cercas (fences):**

| Cerca | Fórmula | Classificação |
|---|---|---|
| Interna inferior | Q1 − 1,5 × IQR | Além dela: **outlier moderado** |
| Interna superior | Q3 + 1,5 × IQR | Além dela: **outlier moderado** |
| Externa inferior | Q1 − 3 × IQR | Além dela: **outlier extremo** |
| Externa superior | Q3 + 3 × IQR | Além dela: **outlier extremo** |

- **Método IQ × método de Tukey (conforme o livro):** no método IQ, removem-se **todos** os outliers possíveis e prováveis; no de Tukey, apenas os **prováveis** são descartados.
- **Saiba mais (livro):** scatterplots e histogramas também ajudam a visualizar outliers em variáveis univariadas.
- **Fique atento (livro):** os tamanhos das amostras devem ser iguais ao usar a abordagem da amplitude estudentizada.

### 3.7 Outliers Multivariados — Distância de Mahalanobis

- Método padrão baseado em distância (McLachlan, 1999). É a distância entre um **ponto e uma distribuição**, e não entre dois pontos; equivale a uma "distância euclidiana multivariada" que considera a covariância.
- Fórmula: **MDᵢ = √[ (xᵢ − x̄)ᵀ C⁻¹ (xᵢ − x̄) ]**, onde C = matriz de covariância, x̄ = vetor médio, xᵢ = i-ésima observação.
- **Critério:** MD² é comparado ao quantil 0,975 da distribuição **qui-quadrado** com *m* graus de liberdade (*m* = nº de variáveis). A observação é candidata a outlier se **MD > √χ²(m; 0,975)**. Isso vale porque MD² de dados normais multivariados segue qui-quadrado.

---

### 3.8 Remover ou não remover? *(o que o material diz)*

O objetivo da unidade é "determinar a remoção, ou não, de outliers de acordo com as características da base". O material oferece estes critérios:
- Depois de detectar, é preciso entender se os outliers precisam ser **removidos ou corrigidos**.
- A decisão depende de **interpretar a causa**: erro (medição, entrada, corrupção) × valor real (variação natural, fraude, desempenho excepcional).
- Outliers podem ser exatamente a informação procurada (fraudes, falhas, intrusões).

*(Conexão com a disciplina anterior: em análise de fraude, outlier é insight; em análise de comportamento, pode ser distorção.)*

### 3.9 PCA em profundidade *(complementação — aprofundamento pedido pela Dani)*

> **Origem do conteúdo:** o capítulo-base cobre a PCA em nível introdutório (conceitos, passo a passo, aplicações). Esta seção aprofunda o método com teoria padrão de estatística multivariada e aprendizado de máquina. **Não é conteúdo do livro nem do professor** e não deve ser atribuída a eles. Os números dos exemplos foram calculados e conferidos em código (veja `aula03_vscode/`).

#### 3.9.0 PCA em linguagem prática *(leia isto primeiro)*

> Esta subseção traduz a PCA para o dia a dia, sem depender da matemática. As seções 3.9.1 a 3.9.13 aprofundam a teoria.

**Em 30 segundos**

Você tem uma planilha com muitas colunas. Várias delas "contam a mesma história" (por exemplo, área, número de quartos e valor de um imóvel crescem juntos). A PCA cria **poucas colunas novas**, chamadas **componentes**, que **resumem** as colunas antigas, da mais informativa para a menos informativa. Você fica com as primeiras e descarta as últimas, perdendo pouca informação.

**Três coisas que a PCA NÃO é:**

| A PCA não... | O que ela faz de fato |
|---|---|
| **Escolhe** quais colunas manter (isso é *seleção de variáveis*) | **Cria colunas novas**, misturando as antigas |
| **Prevê** algo nem usa rótulo | É não supervisionada: só olha como as colunas se relacionam |
| **Apaga** informação sozinha | Só há perda quando **você** descarta componentes. Com todos mantidos, nada se perde |

**Tradutor: termo da aula → português do dia a dia**

| Termo da aula | Em português simples | Pergunta que responde |
|---|---|---|
| **Variância** | Quanto os valores se espalham; "quanta informação" a coluna tem | Essa coluna varia o bastante para ser interessante? |
| **Padronizar** | Colocar todas as colunas na mesma régua (média 0, desvio 1) | Salário em reais e idade em anos podem ser comparados? |
| **Matriz de covariância (ou correlação)** | Tabela que mostra quais colunas "andam juntas" | Quais colunas contam a mesma história? |
| **Componente principal** | Coluna-resumo nova | Como resumir tudo em poucas colunas? |
| **Autovetor** | A "receita" da coluna-resumo: quanto de cada coluna original entra nela | Como o componente é montado? |
| **Autovalor** | A "importância" da coluna-resumo: quanta informação ela guarda | Esse componente vale manter? |
| **Variância explicada** | Porcentagem da informação original que a coluna-resumo guarda | Quanto estou preservando? |
| **Cargas (loadings)** | Os números da receita | Quais colunas originais definem esse componente? |
| **Scores** | A "nota" de cada linha nas colunas novas | Onde cada imóvel ou cliente se posiciona? |
| **Ortogonal / não correlacionado** | Cada coluna-resumo traz informação diferente, sem repetir | Os componentes se repetem? (não) |
| **Reduzir dimensionalidade** | Ficar com menos colunas | |

**Os passos do livro em "receita de bolo"** (correspondem aos passos da seção 3.3)

| # | Em português simples | Por que se faz |
|---|---|---|
| 1 | **Colocar na mesma régua** (padronizar) | Sem isso, a coluna com números maiores domina |
| 2 | **Ver quais colunas andam juntas** (matriz de covariância) | É nas colunas que andam juntas que há o que resumir |
| 3 | **Achar as "direções" em que os dados mais se espalham** (autovetores e autovalores) | É como girar uma câmera até achar o ângulo em que os dados aparecem mais espalhados |
| 4 | **Ordenar da mais para a menos informativa** | O PC1 é sempre o mais importante |
| 5 | **Decidir quantas colunas-resumo manter** | Equilíbrio entre simplificar e perder informação |
| 6 | **Reescrever os dados nas colunas novas** (scores) | É a planilha resumida que você vai usar |

**Exemplo prático: 10 imóveis, 5 colunas** *(fictício; números calculados no script `aula03_vscode/pca_exemplo_imoveis.py`)*

| Imóvel | Área (m²) | Quartos | Banheiros | Valor (R$ mil) | Distância ao centro (km) |
|---|---|---|---|---|---|
| 1 | 45 | 1 | 1 | 280 | 12 |
| 2 | 52 | 2 | 1 | 320 | 3 |
| 3 | 60 | 2 | 1 | 360 | 8 |
| 4 | 75 | 2 | 2 | 450 | 15 |
| 5 | 80 | 3 | 2 | 500 | 5 |
| 6 | 95 | 3 | 2 | 610 | 10 |
| 7 | 110 | 3 | 3 | 700 | 2 |
| 8 | 130 | 4 | 3 | 820 | 14 |
| 9 | 150 | 4 | 4 | 980 | 4 |
| 10 | 180 | 5 | 4 | 1200 | 9 |

**Passo 1: quais colunas andam juntas?** Área, quartos, banheiros e valor têm correlação entre **0,90 e 1,00** entre si: contam a mesma história (o "tamanho" do imóvel). A distância ao centro quase não se relaciona com elas (entre −0,05 e −0,12).

**Passo 2: o resultado da PCA**

| Componente | Informação guardada | Acumulada |
|---|---|---|
| PC1 | 77,8% | 77,8% |
| PC2 | 19,9% | 97,6% |
| PC3 | 1,9% | 99,5% |
| PC4 | 0,4% | 100% |
| PC5 | 0,0% | 100% |

Duas colunas novas guardam **97,6%** da informação das cinco originais.

**Passo 3: ler a "receita" (cargas)**

| Coluna original | Entra no PC1 | Entra no PC2 |
|---|---|---|
| Área | 0,51 | 0,07 |
| Quartos | 0,49 | 0,00 |
| Banheiros | 0,49 | 0,00 |
| Valor | 0,50 | 0,05 |
| Distância ao centro | −0,06 | 1,00 |

- **PC1** é feito, em partes quase iguais, de área, quartos, banheiros e valor. Você pode **chamá-lo de "porte do imóvel"**.
- **PC2** é praticamente só a distância ao centro. Você pode **chamá-lo de "localização"**.
- Dar nome ao componente é **interpretação sua**, não resultado da PCA. E o sinal pode inverter de uma execução para outra (isso não muda o significado).

**Passo 4: usar as "notas" (scores)**

| Imóvel | PC1 (porte) | PC2 (localização) | Leitura |
|---|---|---|---|
| 10 | 3,66 | 0,42 | O maior porte da lista |
| 1 | −2,69 | 0,72 | O menor porte |
| 4 | −1,19 | 1,48 | Pequeno e **longe** do centro (15 km) |
| 7 | 0,73 | −1,38 | Médio e **perto** do centro (2 km) |

**Passo 5: quanto se perde?** Com 2 componentes em vez de 5, o erro médio em cada célula da tabela é de **0,11 desvio-padrão**. É pouco.

**O que isso significa na prática:** 5 colunas viraram 2, e as duas são **interpretáveis** ("porte" e "localização"). Em um modelo, em vez de 4 colunas de tamanho que repetem a mesma informação, você usaria 1.

> **Atenção:** se o objetivo fosse **prever o valor**, a coluna valor não entraria na PCA dos preditores (ela é a resposta, não um preditor).

**Código mínimo (rode no VS Code):**
```python
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(imoveis)        # 1) mesma régua
pca = PCA().fit(X)                                 # 2) a PCA
print(pca.explained_variance_ratio_)               # 3) quanta informação cada componente guarda
print(pd.DataFrame(pca.components_[:2].T, index=imoveis.columns))  # 4) a "receita"
```

**Por que padronizar? (exemplo prático)**

Imagine uma planilha de clientes com **renda (em reais, na casa dos milhares)** e **idade (em anos, na casa das dezenas)**. A PCA procura onde os números mais se espalham. Como a renda varia em milhares, ela "grita mais alto" e vira praticamente o componente 1, mesmo que a idade seja igualmente importante. Padronizar coloca as duas na mesma régua.

Número real do dataset Wine (13 colunas): **sem padronizar**, o PC1 explica 99,8% e é quase só a coluna `proline` (valores na casa dos 700); **padronizando**, o PC1 cai para 36,2% e passa a refletir várias colunas.

**Como ler o resultado em 3 perguntas**

| Pergunta | Onde olhar | Como decidir |
|---|---|---|
| **1. Quanta informação guardei?** | Tabela de variância explicada (acumulada) | 90% a 95% para compressão; 2 ou 3 componentes para gráfico (sempre informe a porcentagem nos eixos) |
| **2. O que cada componente significa?** | Cargas (a "receita") | Olhe os maiores valores em valor absoluto; sinais opostos são os dois lados do mesmo eixo; dê um nome |
| **3. Onde cada linha cai?** | Scores (as "notas") | Valores grandes (positivos ou negativos) são extremos naquele eixo; perto de 0 é o típico |

**Cenários de vida real: "Imagine que..."**

**1. Indicadores que se repetem**
- **Imagine que** você tem uma planilha com 40 indicadores de desempenho de lojas e muitos medem quase a mesma coisa.
- **Será analisado por** PCA (depois de padronizar).
- **Porque** ela resume os 40 em poucos eixos (por exemplo, "volume de vendas" e "eficiência"), e o ranking de lojas deixa de contar a mesma informação várias vezes.

**2. Aplicação profissional (sugestão, não é conteúdo da aula)**
- **Imagine que** sua área avalia demandas com 12 critérios (valor, risco, esforço, urgência, alinhamento estratégico...) e vários se repetem na prática.
- **Será analisado por** PCA sobre os critérios das demandas já avaliadas.
- **Porque** critérios correlacionados pesam em dobro numa pontuação simples. A PCA mostra quais eixos realmente diferenciam as demandas (por exemplo, "valor para o negócio" × "esforço e risco") e permite montar um mapa de priorização em 2D. A decisão final continua sendo de negócio.

**3. Quando a PCA não ajuda**
- **Imagine que** suas colunas são independentes entre si (correlação perto de zero).
- **Será analisado por** outra técnica, ou usado como está.
- **Porque** a PCA só comprime quando as colunas andam juntas. Sem correlação, cada componente guarda a mesma quantidade de informação e não há o que descartar.

**Perguntas que costumam travar**

| Pergunta | Resposta curta |
|---|---|
| A PCA escolhe as melhores variáveis? | Não. Cria variáveis novas, misturando as antigas |
| Perco informação? | Só o que você descartar. Com todos os componentes, nada se perde |
| Dá para voltar à planilha original? | Com todos os componentes, exatamente. Com menos, de forma aproximada (erro de reconstrução, seção 3.9.3) |
| Por que o PC1 é sempre o mais importante? | Por construção: é a direção de maior espalhamento. O PC2 é a próxima, perpendicular à primeira |
| O que "ortogonal" significa aqui? | Cada componente traz informação nova, sem repetir a anterior |
| Carga negativa é ruim? | Não. Indica sentido oposto dentro do componente. O sinal do componente inteiro pode inverter sem mudar o significado |
| A PCA separa grupos? | Não é o objetivo, e ela não usa rótulo. Às vezes os grupos aparecem (como no Wine), mas não é garantido |
| Preciso saber álgebra linear? | Para usar, não. Para explicar em prova, basta saber: **autovetor = direção** e **autovalor = quanta variação há naquela direção** |
| Qual a diferença para análise fatorial? | A PCA **resume** colunas em poucas colunas novas; a análise fatorial **procura causas ocultas** (fatores) por trás das colunas (seção 3.1) |

#### 3.9.1 A ideia em uma frase

A PCA encontra **novos eixos** (combinações lineares das variáveis originais), ordenados por **quanta variação dos dados cada um explica**, e permite ficar só com os primeiros.

**Analogia da sombra:** imagine um objeto 3D iluminado por uma lâmpada, projetando sombra na parede. Dependendo do ângulo da luz, a sombra mostra muita ou pouca informação sobre a forma do objeto. A PCA escolhe o ângulo em que a sombra fica **o mais espalhada possível** (maior variância), ou seja, a que mais preserva a estrutura.

![Intuição geométrica da PCA](../2_Laboratorios/aula03_vscode/saidas_exemplo/00_intuicao_pca_2d.png)

*Painel 1: dados com os eixos PC1 (maior variância) e PC2 (perpendicular). Painel 2: os mesmos pontos rotacionados; descartar PC2 equivale a "achatar" os pontos sobre o eixo PC1. Neste exemplo simulado, PC1 guarda 95,5% da variância.*

**Ponto essencial:** a PCA **não muda os dados**, ela **gira o sistema de coordenadas**. Com p variáveis você obtém p componentes (sem perda nenhuma). A redução vem de **descartar os últimos componentes**, que carregam pouca variância.

#### 3.9.2 Por que usar: os problemas que a PCA resolve

| Problema | Como a PCA ajuda | Exemplo |
|---|---|---|
| **Muitas variáveis** (alta dimensionalidade) | Resume em poucos componentes | 300 sensores de uma máquina viram 5 a 10 componentes |
| **Multicolinearidade** (preditores correlacionados) | Gera componentes **não correlacionados** entre si | Regressão com renda, patrimônio e gasto que se movem juntos |
| **Redundância** | Combina variáveis que dizem a mesma coisa | Peso e IMC medindo parte do mesmo fenômeno |
| **Visualização** | Projeta em 2D ou 3D | Ver clusters de clientes em um gráfico |
| **Ruído** | Descartar componentes de baixa variância remove parte do ruído | Compressão de imagem com pouca perda |
| **Custo computacional** | Menos colunas, treino mais rápido | Modelo com milhares de variáveis |
| **Distâncias perdem sentido em alta dimensão** | Reduz antes de aplicar k-means ou KNN | Segmentação de clientes com 50 variáveis |

#### 3.9.3 Matemática: de onde vêm autovetores e autovalores

**Objetivo:** achar a direção **w** (vetor de comprimento 1) em que a variância dos dados projetados seja máxima.

1. Os dados projetados em **w** têm variância **wᵀCw**, onde **C** é a matriz de covariância.
2. Maximizar **wᵀCw** sujeito a **‖w‖ = 1** (multiplicadores de Lagrange) leva a **Cw = λw**. Ou seja, **w é um autovetor de C** e a variância obtida é o próprio **autovalor λ**.
3. O maior autovalor dá o PC1. Os seguintes são os próximos autovetores. Como C é **simétrica**, seus autovetores são **ortogonais** (teorema espectral), e daí os componentes serem perpendiculares.
4. Decomposição: **C = V Λ Vᵀ**, em que as colunas de V são os autovetores e Λ é a diagonal dos autovalores.
5. **Scores** (coordenadas das observações nos novos eixos): **Z = X · V**. A covariância dos scores é **Λ (diagonal)**, o que significa que **os componentes não são correlacionados**.
6. **Variância explicada:** o traço de C (soma das variâncias) é igual à soma dos autovalores. Para dados padronizados, a soma vale p. Logo, a variância explicada pelo componente *i* é **λᵢ / Σλ** (= λᵢ / p).

**Fórmulas úteis:**

| Conceito | Fórmula | Observação |
|---|---|---|
| Padronização | z = (x − μ) / σ | Obrigatória quando as escalas diferem |
| Covariância | Cov(w,x) = Σ(wᵢ − w̄)(xᵢ − x̄) / (n − 1) | Diagonal = variâncias |
| Autovalor/autovetor | Cv = λv ⇒ det(C − λI) = 0 | Vêm em pares |
| Variância explicada | λᵢ / Σλ | Acumulada = soma cumulativa |
| Scores | Z = X·V | Posição de cada linha nos novos eixos |
| Cargas escaladas | vᵢⱼ · √λᵢ | Aproxima a correlação variável j × componente i (dados padronizados) |
| Reconstrução | X̂ = Zₖ · Vₖᵀ | Usando só os k primeiros componentes |
| Erro de reconstrução | Σ dos autovalores descartados | Conferido no script (célula 11) |
| SVD | X = U S Vᵀ ⇒ λᵢ = sᵢ² / (n − 1) | O scikit-learn usa SVD (numericamente mais estável) |

**Covariância ou correlação?** Padronizar os dados equivale a usar a **matriz de correlação**. Use-a quando as variáveis têm unidades ou escalas diferentes (caso mais comum). Use só a centralização (matriz de covariância) quando todas estão na mesma unidade e a magnitude tem significado, como pixels de imagens.

**Nota sobre `n` e `n − 1`:** o capítulo usa `n` no desvio-padrão, o `StandardScaler` também (ddof = 0), e a matriz de covariância costuma usar `n − 1`. Isso muda levemente os autovalores, **mas não muda as proporções de variância explicada** nem as direções.

#### 3.9.4 Exemplo numérico completo, à mão (2 variáveis)

**Problema:** 6 alunos, com horas de estudo (x) e nota (y).

| Aluno | Horas (x) | Nota (y) |
|---|---|---|
| 1 | 2 | 55 |
| 2 | 4 | 62 |
| 3 | 5 | 66 |
| 4 | 7 | 78 |
| 5 | 9 | 85 |
| 6 | 10 | 92 |

**Passo 1 — Padronizar.** Médias: x̄ = 6,17 e ȳ = 73,0. Desvios (n − 1): sₓ = 3,06 e s_y = 14,31.

| Aluno | zₓ | z_y |
|---|---|---|
| 1 | −1,361 | −1,258 |
| 2 | −0,708 | −0,769 |
| 3 | −0,381 | −0,489 |
| 4 | 0,272 | 0,349 |
| 5 | 0,926 | 0,839 |
| 6 | 1,253 | 1,328 |

**Passo 2 — Matriz de covariância dos dados padronizados** (= matriz de correlação):

```
C = | 1,0000  0,9955 |
    | 0,9955  1,0000 |
```
A diagonal é 1 (variância de cada variável padronizada) e **r = 0,9955**.

**Passo 3 — Autovalores:** det(C − λI) = 0 ⇒ (1 − λ)² − 0,9955² = 0 ⇒ **λ = 1 ± 0,9955**:
- λ₁ = **1,9955**
- λ₂ = **0,0045**

**Passo 4 — Autovetores** (para qualquer matriz de correlação 2 × 2 com r > 0):
- v₁ = (0,7071; 0,7071), isto é, **PC1 = (zₓ + z_y) / √2** (uma "média" das duas variáveis)
- v₂ = (−0,7071; 0,7071), isto é, **PC2 = (z_y − zₓ) / √2** (a "diferença" entre elas)

**Passo 5 — Variância explicada:**
- PC1: 1,9955 / 2 = **99,77%**
- PC2: 0,0045 / 2 = **0,23%**

**Passo 6 — Scores** (exemplo, aluno 1): PC1 = (−1,361 − 1,258) / 1,4142 = **−1,852**; PC2 = (−1,258 + 1,361) / 1,4142 = **0,073**.

| Aluno | PC1 | PC2 |
|---|---|---|
| 1 | −1,852 | 0,073 |
| 2 | −1,044 | −0,043 |
| 3 | −0,615 | −0,076 |
| 4 | 0,440 | 0,055 |
| 5 | 1,248 | −0,062 |
| 6 | 1,824 | 0,053 |

**Passo 7 — Reduzir para 1 componente.** Os valores de PC2 são quase zero. Guardar só PC1 mantém 99,77% da informação e o erro de reconstrução é 0,0038 (= 0,0045 × 5/6, o autovalor descartado ajustado por n − 1).

**O que este exemplo ensina:**
- Com duas variáveis padronizadas, os autovalores são sempre **1 + r** e **1 − r**, e os eixos são sempre as diagonais.
- **r próximo de 1** ⇒ uma dimensão basta (muita redundância). **r = 0** ⇒ λ₁ = λ₂ = 1 e **não há o que comprimir**.
- Essa é a lógica de toda PCA: ela só comprime quando **existe correlação** entre as variáveis.

#### 3.9.5 Quantos componentes manter?

| Critério | Como funciona | Quando usar | Resultado no dataset Wine |
|---|---|---|---|
| **Variância acumulada** | Mantém componentes até atingir um limiar (90% a 95% é a convenção) | Quando o objetivo é preservar informação (compressão, pré-processamento) | 95% exige **10** componentes |
| **Critério de Kaiser** | Mantém os de autovalor > 1 (na matriz de correlação) | Triagem rápida, dados padronizados | **3** componentes |
| **Scree plot (cotovelo)** | Procura o ponto em que a curva dos autovalores "dobra" | Exploração visual | Cotovelo perto de **3 a 4** |
| **Desempenho do modelo** | Escolhe *k* por validação cruzada no problema real | Quando a PCA alimenta um modelo supervisionado | Veja célula 10 |
| **Objetivo de visualização** | Fixa 2 ou 3 | Gráficos | 2 componentes = 55,4% |

Os limiares (90%, 95%, autovalor > 1) são **convenções**, não leis, e os critérios podem divergir (como no Wine: 3 contra 10). A decisão depende do objetivo e do custo de perder informação.

#### 3.9.6 Como interpretar o resultado

- **Scores:** onde cada observação cai nos novos eixos. Observações próximas são parecidas.
- **Cargas (loadings):** quanto cada variável original contribui para cada componente. Cargas altas em valor absoluto indicam as variáveis que "definem" o componente.
- **O sinal é arbitrário.** Multiplicar um componente por −1 não muda nada. Por isso comparar duas execuções exige olhar o valor absoluto.
- **Nomear componentes é interpretação**, não resultado. Exemplo no Wine: PC1 reúne flavonoides, fenóis totais e OD280 (um "perfil fenólico"); PC2 reúne intensidade de cor, álcool e prolina.
- **Biplot:** setas próximas apontam para variáveis correlacionadas; setas opostas, para correlação negativa; seta longa indica variável bem representada nesse plano.
- **Cuidado:** o componente é uma mistura das variáveis, então **perde interpretabilidade** direta. Não se deve concluir causalidade a partir de um componente.

#### 3.9.7 Pressupostos e limitações

| Limitação | Consequência | Como lidar | Exemplo |
|---|---|---|---|
| **Sensível à escala** | A variável de maior escala domina o PC1 | Padronizar | No Wine **sem padronizar**, PC1 explica 99,8% e é praticamente só a `proline` |
| **Sensível a outliers** | Médias e variâncias distorcidas giram os eixos | Tratar/avaliar outliers antes, ou usar PCA robusta | 3 linhas erradas baixaram o PC1 de 36,2% para 32,2% |
| **Só captura relações lineares** | Estruturas curvas não são resumidas | Kernel PCA, ou técnicas de visualização não lineares | Dados em formato de espiral |
| **Variância não é relevância** | Em problemas supervisionados, a direção mais útil para o alvo pode ter pouca variância e ser descartada | Validar *k* pelo desempenho; considerar métodos supervisionados | Variável fraca em variância, mas que separa as classes |
| **Exige variáveis numéricas contínuas** | Categorias não têm média nem variância com sentido | Análise de correspondência (Aula 2) ou codificar com cuidado | Marca × faixa etária |
| **Não aceita valores ausentes** | Erro de execução | Imputar ou remover antes | Pesquisa com respostas em branco |
| **Perde interpretabilidade** | "Componente 3" não tem unidade de negócio | Analisar cargas; usar quando interpretar variáveis não é o foco | Modelo regulado que precisa explicar cada variável |
| **Instável em amostras pequenas** | Componentes mudam com poucos dados | Mais observações; reamostragem | Estudo-piloto com 20 linhas |
| **Limite de componentes** | O número de componentes é no máximo min(observações, variáveis) (o capítulo cita o número de observações). Na prática, centralizar os dados reduz em 1 o número de componentes com informação | Conferir o formato da matriz | 30 linhas × 1000 colunas ⇒ no máximo 30 componentes (29 com informação) |

#### 3.9.8 PCA no aprendizado supervisionado

A PCA é **não supervisionada** (não vê o rótulo), mas é muito usada como **pré-processamento** em problemas supervisionados.

| Uso | Quando usar | Exemplo teórico | Exemplo real |
|---|---|---|---|
| **Combater multicolinearidade** (regressão por componentes principais) | Preditores muito correlacionados desestabilizam os coeficientes | Renda, patrimônio e gasto mensal juntos | Modelo de crédito com dezenas de indicadores financeiros correlacionados |
| **Reduzir dimensionalidade antes de modelar** | Muitas variáveis, poucas observações, risco de overfitting ou treino lento | 500 variáveis e 200 linhas | Genômica: milhares de genes por paciente |
| **Visualizar classes** | Entender se as classes se separam | Projeção do Wine em PC1 × PC2 | Ver se clientes que cancelam formam grupo distinto |
| **Pré-processar antes de KNN, SVM ou k-means** | Algoritmos baseados em distância sofrem em alta dimensão | k-means com 50 variáveis | Segmentação de clientes |
| **Remover ruído** | Os últimos componentes carregam principalmente ruído | Imagens ruidosas | Sinais de sensores industriais |

**Cuidados essenciais:**
1. **Vazamento de dados (data leakage):** ajuste o `StandardScaler` e a `PCA` **somente no treino** e apenas **transforme** o teste. Fazer a PCA na base inteira antes de dividir "vaza" informação do teste. A solução é o `Pipeline`.
2. **Não há garantia de melhora.** No Wine, a regressão logística teve acurácia (validação cruzada) de 0,984 sem PCA, 0,968 com 2 componentes e 0,975 com 95% da variância. A PCA reduziu 13 variáveis para 10 sem ganho de desempenho.
3. **Árvores e florestas** normalmente não precisam de PCA (não são sensíveis a escala nem a multicolinearidade da mesma forma).
4. **Interpretabilidade:** importâncias de variáveis passam a ser "importância de componentes".
5. **Salve o pipeline treinado** (`scaler` + `pca` + modelo) com `joblib`, como já visto na disciplina anterior, para aplicar a mesma transformação a dados novos.

#### 3.9.9 Variantes (apenas menção, não faz parte do material)

| Variante | Para que serve |
|---|---|
| **Kernel PCA** | Capturar estruturas **não lineares** |
| **Incremental PCA** | Dados que não cabem na memória (processa em lotes) |
| **Sparse PCA** | Cargas esparsas, mais fáceis de interpretar |
| **Randomized PCA / TruncatedSVD** | Matrizes muito grandes ou esparsas (ex.: texto) |
| **PCA robusta** | Reduzir a influência de outliers |
| **Whitening** (`whiten=True`) | Deixar os componentes com variância 1 (útil para alguns modelos) |

#### 3.9.10 Quando usar a PCA: tabela de decisão

| Situação | Usar PCA? | Exemplo teórico | Exemplo real |
|---|---|---|---|
| Muitas variáveis numéricas **correlacionadas** | **Sim** | 50 indicadores que variam juntos | Indicadores financeiros de empresas |
| Precisa visualizar dados de alta dimensão em 2D/3D | **Sim** | Projetar 13 variáveis em PC1 × PC2 | Mapa de perfis de clientes |
| Variáveis quase **não correlacionadas** | **Não compensa** | Com r ≈ 0 os autovalores são iguais e nada comprime | Variáveis independentes entre si |
| Dados **categóricos** | **Não** (use correspondência) | Marca × faixa etária | Pesquisa de satisfação com opções fixas |
| Precisa **explicar cada variável** ao negócio/regulador | **Evitar** | Modelo de crédito auditável | Score de risco com justificativa por variável |
| Quer **testar fatores latentes** | **Prefira análise fatorial** | Traços psicológicos medidos por um questionário | Pesquisa de clima organizacional |
| Estrutura **não linear** | **Prefira Kernel PCA** ou outra técnica | Dados em espiral | Imagens com variações complexas |

#### 3.9.11 Cenários de vida real: "Imagine que..." *(complementação)*

**1. Regressão com preditores colados**
- **Imagine que** você tem um modelo de risco de crédito com 80 indicadores financeiros fortemente correlacionados e os coeficientes da regressão estão instáveis.
- **Será analisado por** PCA seguida de regressão (regressão por componentes principais).
- **Porque** a PCA gera componentes **não correlacionados**, eliminando a multicolinearidade, e permite manter poucos componentes.

**2. Dashboard para o marketing**
- **Imagine que** a equipe de marketing tem 200 métricas por cliente e quer **ver** se existem grupos.
- **Será analisado por** PCA para 2 dimensões e gráfico de dispersão (PC1 × PC2).
- **Porque** a projeção preserva a maior variância possível em 2D, o que torna agrupamentos visíveis. (Sempre informe a variância explicada nos eixos, para não superinterpretar.)

**3. Detecção de anomalia em sensores**
- **Imagine que** uma indústria monitora 300 sensores de uma máquina e quer detectar comportamento anormal.
- **Será analisado por** PCA treinada com dados de funcionamento normal e **erro de reconstrução** como alarme.
- **Porque** o comportamento normal ocupa poucos componentes. Um ponto anômalo é mal reconstruído pelos primeiros componentes, e o erro alto revela o outlier. *(Conecta PCA com a parte de outliers desta aula.)*

**4. Segmentação com muitas variáveis**
- **Imagine que** você precisa segmentar clientes com 50 variáveis numéricas.
- **Será analisado por** padronização, depois PCA (mantendo 90% a 95%) e depois **k-means** (Aula 2).
- **Porque** em alta dimensão as distâncias perdem contraste, e variáveis redundantes pesam em dobro nos centroides. A PCA reduz e decorrela antes do agrupamento.

**5. Reconhecimento facial (exemplo do livro)**
- **Imagine que** um sistema precisa reconhecer rostos a partir de milhares de pixels por imagem.
- **Será analisado por** PCA sobre as imagens (**eigenfaces**).
- **Porque** a PCA encontra poucas "faces base" que representam a variação principal, reduzindo a complexidade estatística da representação.

**6. Quando NÃO usar**
- **Imagine que** você tem uma pesquisa em que todas as respostas são categorias (marca preferida, faixa etária, região).
- **Será analisado por** análise de correspondência, e **não** por PCA.
- **Porque** a PCA depende de média e variância, que não fazem sentido para categorias.

#### 3.9.12 Erros comuns (checklist)

1. Esquecer de **padronizar** quando as escalas diferem.
2. Aplicar a PCA **antes** de dividir treino e teste (vazamento).
3. Interpretar o **sinal** de um componente como se tivesse significado.
4. Usar PCA em variáveis **categóricas** ou com valores ausentes.
5. Escolher o número de componentes por uma regra fixa, **sem validar** no objetivo real.
6. **Ignorar outliers**, que giram os eixos.
7. Tratar um componente como se fosse uma variável original, ou concluir **causalidade**.
8. Esquecer de **salvar** scaler e PCA treinados para aplicar a dados novos.

#### 3.9.13 Mapa: teoria → NumPy → scikit-learn

| Etapa da teoria | NumPy (na mão) | scikit-learn |
|---|---|---|
| Padronizar | `(X - X.mean(0)) / X.std(0)` | `StandardScaler().fit_transform(X)` |
| Matriz de covariância | `np.cov(Xp, rowvar=False)` | (interno) |
| Autovalores e autovetores | `np.linalg.eigh(C)` | `pca.explained_variance_`, `pca.components_` |
| Ordenar | `np.argsort(autovals)[::-1]` | (já vêm ordenados) |
| Variância explicada | `autovals / autovals.sum()` | `pca.explained_variance_ratio_` |
| Scores | `Xp @ autovetores` | `pca.transform(Xp)` |
| Manter 95% | `np.cumsum(...) >= 0.95` | `PCA(n_components=0.95)` |
| Reconstrução | `Z[:, :k] @ V[:, :k].T` | `pca.inverse_transform(...)` |
| Pipeline sem vazamento | — | `Pipeline([("pad", StandardScaler()), ("pca", PCA(...)), ("clf", ...)])` |

**Leitura recomendada (documentação oficial):** a página sobre decomposição de sinais em componentes (PCA) do guia do usuário do scikit-learn.

---

## 4. Exemplos, Aplicações e Material Prático

### 4.1 Bibliotecas usadas nos códigos do capítulo

| Biblioteca | Onde aparece | Papel |
|---|---|---|
| **Pandas** | `quantile`, `DataFrame`, `concat`, `sort_values` | Manipulação dos dados |
| **NumPy** | `np.percentile` | Cálculo de quartis nas funções de outliers |
| **Seaborn** | `sns.boxplot` | Box-plot |
| **Matplotlib** | `import matplotlib.pyplot as plt` (bloco da Mahalanobis) | Importada; base dos gráficos |
| **Scikit-learn** | `from sklearn.covariance import MinCovDet` | Estimador da covariância para a distância de Mahalanobis |
| `glob` | Importada no bloco da Mahalanobis | Não é usada no código |

**Resposta direta:** o capítulo usa **Pandas, NumPy e Scikit-learn**, mas também **Seaborn** (box-plot) e **Matplotlib**. Apesar do título "Pandas e Numpy", o Scikit-learn entra só na parte multivariada.

### 4.2 Código do capítulo (preservado)

**Box-plot de uma variável (Figura 2):**
```python
import seaborn as sns
sns.boxplot(x=boston_df['DIS'])
```

**Quartis e IQR por coluna:**
```python
Q1 = boston_df.quantile(0.25)
Q3 = boston_df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
```

**Linhas que contêm outliers (em qualquer coluna):**
```python
df_outliers = boston_df[((boston_df < (Q1 - 1.5 * IQR)) | (boston_df > (Q3 + 1.5 * IQR))).any(axis=1)]
```
Resultado no livro: **232 linhas × 13 colunas** marcadas. Na matriz booleana, `True` indica outlier e `False` indica valor válido:
```python
(df_outliers < (Q1 - 1.5 * IQR)) | (df_outliers > (Q3 + 1.5 * IQR))
```

**Função que devolve a variável sem os outliers (univariado):**
```python
import numpy as np
def apagar_outlier(valores):
    factor = 1.5
    q3, q1 = np.percentile(valores, [75, 25])
    iqr = q3 - q1
    parte_baixa = q1 - (iqr * factor)
    parte_alta = q3 + (iqr * factor)
    return [v for v in valores if v > parte_baixa and v < parte_alta]
```

**Função que identifica os outliers e seus índices (univariado):**
```python
import numpy as np
def identificar_outlier(valores):
    factor = 1.5
    q3, q1 = np.percentile(valores, [75, 25])
    iqr = q3 - q1
    parte_baixa = q1 - (iqr * factor)
    parte_alta = q3 + (iqr * factor)
    return valores[(valores < parte_baixa) | (valores > parte_alta)]

outliers = identificar_outlier(boston_df['DIS'])
outliers
```
Saída do livro (todos acima da cerca interna superior):
```
351    10.7103
352    10.7103
353    12.1265
354    10.5857
355    10.5857
Name: DIS, dtype: float64
```

**Distância de Mahalanobis (multivariado):**
```python
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.covariance import MinCovDet
%matplotlib inline

mcd = MinCovDet(assume_centered=True, random_state=42)
cov = mcd.fit(boston_df)
distancias = pd.DataFrame(cov.dist_, index=boston_df.index, columns=['Distancia Mahalanobis'])
resultados = pd.concat([boston_df, distancias], axis=1)
resultados.sort_values(by='Distancia Mahalanobis', ascending=False).head()
```
Resultado no livro: as 5 maiores distâncias são das linhas 380, 418, 405, 410 e 414 (da ordem de 6567, 4446, 3596, 2123 e 1563), todas com `CRIM` muito alto. O livro conclui que há grande chance de serem outliers.

### 4.3 Receita prática: identificar e remover outliers *(complementação)*

> Esta subseção é complementação. Organiza o código do capítulo em um fluxo reutilizável e acrescenta o passo de remoção em DataFrame, que o capítulo não mostra explicitamente.

```python
import numpy as np
import pandas as pd
import seaborn as sns

# 1) Visualizar: box-plot de cada variável numérica
sns.boxplot(data=df.select_dtypes("number"), orient="h")

# 2) Calcular limites pelo IQR (por coluna)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
inferior = Q1 - 1.5 * IQR
superior = Q3 + 1.5 * IQR

# 3) Marcar (não remover ainda): True = outlier
mascara = (df < inferior) | (df > superior)
print(mascara.sum())          # quantos outliers por coluna
print(mascara.any(axis=1).sum())  # quantas LINHAS têm algum outlier

# 4) Decidir e tratar
df_sem_outliers = df[~mascara.any(axis=1)]      # a) remover linhas com outlier
df_limitado = df.clip(lower=inferior, upper=superior, axis=1)  # b) limitar aos extremos (cap)
```

**Lições práticas:**
- O `df_outliers` do livro mostra **só as linhas com outlier**. O inverso (`~mascara.any(axis=1)`) é a base **sem** eles.
- Remover toda linha com qualquer outlier em qualquer coluna pode eliminar boa parte da base. No exemplo do livro, são 232 linhas sinalizadas, quase metade de uma base de ~506 linhas. Por isso, **marque primeiro, avalie depois**.
- Alternativas à remoção: **limitar** os valores aos extremos (`clip`), **investigar** individualmente, ou **manter** e usar métodos robustos (ex.: RobustScaler, visto na disciplina anterior).
- Para outliers **multivariados**, combine o IQR coluna a coluna com a Mahalanobis, que enxerga combinações incomuns.

**Quadro de decisão (complementação):**

| Se o outlier for... | Exemplo | Decisão sugerida |
|---|---|---|
| Erro de entrada ou medição | Idade = 450 | Corrigir ou remover |
| Corrupção de dados | Valor impossível após integração | Remover ou reimputar |
| Valor real e relevante para o objetivo | Transação fraudulenta | **Manter** e investigar |
| Valor real, mas distorce o modelo | Atleta de desempenho excepcional em uma média | Limitar (cap) ou usar métodos robustos |

### 4.4 PCA na prática com Scikit-learn *(complementação)*

> Versão curta. O roteiro completo, testado e com resultados reais está em `aula03_vscode/` (seção 4.6), e a teoria aprofundada na seção 3.9.

> O capítulo de PCA não traz código. Este exemplo ilustra a metodologia da seção 3.3 e a observação de "até 95% da informação".

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1) Padronizar (passo 2 da metodologia)
X = StandardScaler().fit_transform(df.select_dtypes("number"))

# 2) PCA mantendo componentes suficientes para explicar 95% da variância
pca = PCA(n_components=0.95)
componentes = pca.fit_transform(X)

print(pca.explained_variance_ratio_)             # variância explicada por componente
print(pca.explained_variance_ratio_.cumsum())    # acumulada
print(pca.components_)                           # autovetores (direções dos eixos)
```
Correspondência com a teoria: `explained_variance_ratio_` = autovalor ÷ soma dos autovalores; `components_` = autovetores; componentes já saem ordenados do maior para o menor.

### 4.5 Atividade 3 (A3) — 5 questões avaliativas

> **Gabarito deduzido do texto do capítulo-base** (a plataforma não mostra o gabarito). Conferência: as respostas dadas pela Dani somaram **2 acertos de 5 (nota 4)**, o que coincide com este gabarito. Tentativa 1 de 2.

| Questão | Tema | Resposta marcada | Correta | Situação |
|---|---|---|---|---|
| 1 | Afirmações sobre a PCA | D (II, apenas) | **D** | ✓ |
| 2 | Vantagens da PCA (V ou F) | A (V–V–V–F) | **C (V–F–V–F)** | ✗ |
| 3 | Funcionamento (componentes) | B (I, apenas) | **A (II e III)** | ✗ |
| 4 | Metodologia (V ou F) | C (F–F–V) | **B (V–F–V)** | ✗ |
| 5 | Componentes principais | C (I, II e III) | **C** | ✓ |

**Por que cada resposta está certa (com o trecho do livro que a sustenta):**

| Q | Afirmação | V/F | Justificativa |
|---|---|---|---|
| 1 | I. PCA reconhece **um maior número** de variáveis não correlacionadas | F | O livro diz o **menor** número de variáveis não correlacionadas |
| 1 | II. Componentes principais são as direções de maior variação | V | Definição do livro |
| 1 | III. Captura os padrões **mais fracos** | F | Enfatiza a variação e captura padrões **fortes** |
| 2 | A compactação dos dados é suportada logo que os padrões são descobertos | V | Livro: "assim que os padrões são encontrados, a compactação também é suportada" |
| 2 | Vantagem: ser **insensível** ao posicionamento relativo das variáveis | F | A PCA é **sensível ao dimensionamento** (escala) das variáveis; e isso não é vantagem, é ponto de cuidado |
| 2 | Aproxima os dados da forma mais viável para os mínimos quadrados | V | Livro: aproximação por mínimos quadrados |
| 2 | Uso principal em tabelas **univariadas** | F | É para tabelas **multivariadas** |
| 3 | I. Componentes novos permanecem correlacionados | F | Não são correlacionados |
| 3 | II. Os com mais informação ficam no início | V | Livro |
| 3 | III. Os recursos novos não são relacionados | V | Livro: "não são correlacionados" |
| 4 | Com muita diferença de intervalo, as variáveis de intervalo menor são dominadas pelas de intervalo maior | V | Livro: por isso se padroniza |
| 4 | Média e desvio-padrão são calculados **após** a padronização | F | São calculados **antes**: eles são necessários **para** padronizar |
| 4 | A matriz de covariância mostra como as variáveis variam da média entre si | V | Livro |
| 5 | I, II e III | V, V, V | Autovetores a partir da covariância; autovetores e autovalores em pares; eixos de maior informação definidos pelos autovetores |

**Pegadinhas desta atividade (padrão das trocas):**

| Padrão da pegadinha | Exemplo na A3 | Como se defender |
|---|---|---|
| Trocar **menor** por **maior** | Q1-I: "maior número de variáveis" | Releia: a PCA quer o **menor** número de componentes |
| Trocar **fortes** por **fracos** | Q1-III | PCA captura o que **mais varia** |
| Trocar **sensível** por **insensível** | Q2-2 | A PCA **depende da escala**; por isso padronizamos |
| Trocar **antes** por **depois** | Q4-2 | Padronizar exige média e desvio **antes** |
| Trocar **multivariada** por **univariada** | Q2-4 | PCA só faz sentido com **várias** variáveis |
| Trocar **correlacionados** por **não correlacionados** | Q3-I | Os componentes são **não correlacionados** |

**A Questão 2 explicada com calma:** a 2ª afirmação é a que mais confunde porque usa a palavra "posicionamento" no lugar de "dimensionamento", e porque soa como vantagem. O que o livro diz é que a PCA **tem sensibilidade ao dimensionamento (escala)** das variáveis originais. Em português simples: se uma coluna tem números muito maiores que as outras (renda em milhares × idade em dezenas), ela domina o resultado. Isso **não é vantagem, é um cuidado**, e é o motivo de padronizar antes (seção 3.9.0). Por isso a afirmação "é insensível" é **falsa**.

**Observação sobre o enunciado:** "posicionamento relativo" não é um termo usado pelo capítulo. Em sentido literal (ordem das colunas na planilha), a PCA de fato não depende dela, o que torna a frase ambígua. Porém, a resposta que a plataforma espera segue o texto do livro (sensibilidade à escala), e a nota obtida confirma que o item é falso. Vale registrar como inconsistência do enunciado.

**Material do professor não acessado:** vídeos e links (QR codes) da Dica do Professor sobre as "duas categorias de outliers" e o "mapa de outliers", sobre a história da PCA, e as leituras do "Saiba mais". Se você assistir e quiser registrar, envie como observação.


### 4.6 Prática no VS Code: pacote `aula03_vscode/` *(complementação)*

Pacote testado para executar a atividade (outliers + PCA) no VS Code:

| Arquivo | Conteúdo |
|---|---|
| `HOWTO_AULA_03_OUTLIERS_PCA_VSCODE.md` | Passo a passo (instalação, ambiente virtual, execução, interpretação, problemas comuns, exercícios) |
| `aula03_outliers_pca.py` | Script em 11 células `# %%`: box-plot, IQR, Mahalanobis, tratamento, PCA na mão e com scikit-learn, efeito de outliers, Pipeline supervisionado, reconstrução |
| `pca_exemplo_imoveis.py` | Exemplo curto e fictício (10 imóveis) usado na seção 3.9.0 |
| `requirements.txt` | numpy, pandas, scipy, scikit-learn, matplotlib, seaborn |
| `saidas_exemplo/` | Gráficos gerados na execução de teste |

**Dataset:** Wine (scikit-learn), em vez do Boston do capítulo, por não depender de internet e por a base Boston ter sido removida do scikit-learn (versão 1.2).

**Resultados reais da execução de teste:**

| Tema | Resultado |
|---|---|
| Outliers pelo IQR (1,5×) | 17 de 178 linhas (9,6%); nenhum extremo (3×) |
| Mahalanobis (corte 24,74) | 12 (clássica) e 51 (robusta, inclui as 12) |
| PCA (padronizada) | PC1 = 36,2%; PC1+PC2 = 55,4%; 95% exige 10 componentes; Kaiser sugere 3 |
| Sem padronizar | PC1 = 99,8% (domina a `proline`) |
| 3 linhas erradas injetadas | PC1 cai de 36,2% para 32,2%; remover as linhas restaura o resultado |
| Regressão logística (validação cruzada) | 0,984 sem PCA; 0,968 com 2 componentes; 0,975 com 95% |
| Erro de reconstrução | Igual à soma dos autovalores descartados (ex.: 1 componente = 8,294) |

**Conclusão didática do teste:** os dados reais de vinho têm outliers **moderados** (variação natural), então o mais defensável é **manter** ou limitar; e a PCA **não melhorou** a acurácia, servindo mais para comprimir, decorrelacionar e visualizar.

---

## 5. Minhas Observações e Dúvidas

**Dúvida da Dani:** "Vamos usar Pandas, NumPy e Scikit-learn: seriam todos esses?"
**Resposta:** não são só esses. O capítulo usa também **Seaborn** (box-plot) e **Matplotlib**. O Scikit-learn aparece apenas na distância de Mahalanobis (`MinCovDet`). Veja a tabela da seção 4.1.

**Inconsistências e pontos de atenção encontrados no material** *(complementação, para estudo crítico; não atribuir ao professor)*:
1. **"Método de Tukey":** o capítulo descreve Tukey pela distribuição de amplitude estudentizada (comparação de médias aos pares, o teste HSD de Tukey). Já a regra das cercas de 1,5 × IQR usada no box-plot também é atribuída a Tukey, mas é outra técnica. São duas coisas diferentes com o mesmo nome. Para detectar outliers na prática, usa-se a regra das cercas.
2. **Fórmula de Mahalanobis:** no PDF aparece um sinal de menos entre (xᵢ − x̄)ᵗ e C⁻¹(xᵢ − x̄). A forma correta é o **produto**, como na seção 3.7. Provável erro de editoração.
3. **"Três pontos" no box-plot:** o texto fala em três pontos entre 10 e 12, mas a saída lista **cinco** observações (351 a 355). Há valores repetidos (10,7103 e 10,5857 duas vezes), então os marcadores se sobrepõem no gráfico.
4. **Dataset:** `boston_df` não é carregado no capítulo. Além disso, `load_boston` foi removido do Scikit-learn na versão 1.2; para reproduzir, é preciso obter a base por outra fonte ou usar outro dataset.
5. **`assume_centered=True`** no `MinCovDet` indica que os dados já estão centralizados (o livro descreve como "sem centralizar os dados"). Os valores em `dist_` são distâncias ao **quadrado** (MD²), coerente com a comparação com qui-quadrado.

---

## 6. Referências e Conexões com Outros Conteúdos

**Livros-base:**
- SOARES, J. *Análise de componentes principais*. In: *Aprendizado de máquina*. SAGAH.
- MIRANDA, L. B. A. de. *Tratando outliers em Pandas e Numpy*. In: *Preparação e análise exploratória de dados*. SAGAH.

**Referências do capítulo de PCA:**
- JAADI, Z. A step-by-step explanation of Principal Component Analysis (PCA). *Builtin*, 2021.
- KONG, X.; HU, C.; DUAN, Z. *Principal component analysis network and algorithms*. Springer, 2017.
- MUELLER, J. P.; MASSARON, L. *Machine learning for dummies*. Wiley, 2016.
- NOBI, A.; TUHIN, K. H.; LEE, J. W. Application of Principal Component Analysis on Temporal Evolution of COVID-19. *PLOS ONE*, v. 16, n. 12, e0260899, 2021.
- PAUL, L. C.; SUMAN, A. A.; SULTAN, N. *Methodological analysis of Principal Component Analysis (PCA) method*. IJCEM, 2013.
- TALEBI, S. Principal Component Analysis (PCA). *Towards Data Science*, 2021.
- VASCONCELOS, S. *Análise de Componentes Principais (PCA)*. [S. l.], [200-?].

**Referências do capítulo de outliers:**
- AGGARWAL, C. C. *Outlier analysis*. Springer, 2015.
- BEYER, H. Book review: Tukey, J. W. Exploratory data analysis. *Biometrical Journal*, v. 23, n. 4, p. 413–414, 1981.
- FREEMAN, J. Book selection: Outliers in statistical data (3rd edition). *Journal of the Operational Research Society*, v. 46, p. 1034–1035, 1995.
- MCLACHLAN, G. Mahalanobis distance. *Resonance*, v. 4, p. 20–26, 1999.

**Leituras do "Saiba mais" (sugestões do professor, não acessadas):** "Outlier: o ponto fora da curva"; "Identificando e tratando outliers nos dados com Python"; "Outliers: o que são e como tratá-los em uma análise de dados?"; dissertação de PCA em carcaças de cordeiros pantaneiros; dissertação de PCA em data warehouses; vídeo "Análise multivariada: componentes principais" (PCA no R).

**Conexões com a disciplina anterior (Aquisição e Preparação de Dados — 262GGR6046A):**
- Outliers: Aula 4 (AED) já tratava remoção, investigação e transformação, e a regra "fraude = insight; comportamento = distorção". Aqui entram o método (IQR/Mahalanobis) e o código.
- Padronização (Z-score): é pré-requisito da PCA (passo 2). Detalhes na Aula 3 da disciplina anterior.
- RobustScaler (mediana e IQR): alternativa para bases com muitos outliers, sem precisar removê-los.

**Conexões internas à disciplina:**
- **Aula 1:** introduziu redução de dimensionalidade e ML não supervisionado. A PCA é a técnica concreta de redução.
- **Aula 2:** análise fatorial como técnica de interdependência e k-means. PCA e FA são comparadas na seção 3.1. Uma prática comum é aplicar PCA antes do agrupamento, para reduzir dimensões; outliers também distorcem os centroides do k-means.
- **Aula 2 (visualização):** o heatmap de correlação ajuda a identificar variáveis redundantes, candidatas à redução por PCA.
- **Aula 2 (análise de correspondência):** é a alternativa à PCA para variáveis categóricas (seção 3.9.7).
- **Disciplina de Aprendizado Supervisionado:** a PCA aparece como pré-processamento; ver seção 3.9.8 (vazamento de dados, `Pipeline`, quando não ajuda).
