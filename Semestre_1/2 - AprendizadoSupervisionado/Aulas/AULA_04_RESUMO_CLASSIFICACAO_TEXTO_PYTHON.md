# AULA 4 — CLASSIFICAÇÃO DE TEXTOS: UTILIZANDO PYTHON PARA CONSTRUIR E TREINAR MODELOS DE MACHINE LEARNING

## Disciplina: Aprendizado de Máquina Supervisionado — Graduação em IA (FMU)

---

## 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Supervisionado (262GGR4728A)
**Aula:** 4 — Classificação de textos — Utilizando Python para construir e treinar modelos de machine learning
**Fonte:** *Processamento de Linguagem Natural* — Juliano Vieira Martins, SAGAH (Soluções Educacionais Integradas)

### Objetivos de aprendizagem (conforme o capítulo)
- Descrever processos de manipulação de dados para utilizar classificadores de texto.
- Analisar o classificador Naïve Bayes.
- Aplicar o classificador Naïve Bayes em um estudo prático.

**Observação de continuidade:** esta aula é a continuação direta da Aula 3 (mesmo livro, autor diferente — Michel Bernardo Fernandes da Silva na Aula 3, Juliano Vieira Martins nesta). A Aula 3 tratou os conceitos de PLN, classificação e pré-processamento (tokenização, stopwords, pontuação) em nível teórico; esta aula aplica tudo isso em **código Python real**, do zero até um classificador funcionando.

---

## 2. Resumo e Contextualização

A classificação de texto é definida como o processo de **atribuir rótulos/etiquetas de categorias ao texto** de acordo com seu conteúdo — uma das tarefas fundamentais do PLN, com aplicações em análise de sentimentos, rotulagem de tópicos, detecção de spam, de intenção e de idioma. Exemplos de contexto: textos curtos (tweets, chamadas de notícias, SMS) e textos longos (análises de clientes, artigos de mídia, contratos legais).

Motivação de negócio: dados em texto (e-mails, chats, páginas web, mídias sociais, tickets de suporte, pesquisas) são abundantes e potencialmente valiosos, mas difíceis de explorar por serem **não estruturados**. A classificação de texto estrutura esses dados de forma rápida e econômica, visando melhorar a tomada de decisão e automatizar processos.

O capítulo segue três grandes blocos:
1. **Obtenção e preparação dos dados**
2. **Análise do classificador Naïve Bayes** (teoria/matemática)
3. **Aplicação do classificador em um estudo prático** (código completo, com o dataset SMS Spam Collection)

---

## 3. Conceitos Fundamentais e Explicações

### 3.1 Obtenção dos dados

Premissa central: um classificador só é útil se os dados de treinamento forem **precisos e representativos**. Um modelo treinado com dados pouco representativos do objetivo gera resultados ruins (JURAFSKY; MARTIN, 2019).

**Pergunta-guia para obter dados:** "para qual objetivo de classificação são os dados?" — a resposta orienta onde buscá-los.

- **Fontes internas:** sistemas de atendimento ao cliente, formulários de satisfação etc., geralmente exportáveis em **CSV** (comma-separated values) ou **TSV** (tab-separated values).
- **Fontes externas:** ferramentas de *web scraping*, **APIs** (application programming interface — software intermediário que permite comunicação entre dois aplicativos) ou **conjuntos de dados públicos** (*public datasets*).

**Datasets públicos citados no capítulo:**

| Dataset | Tarefa | Tamanho aproximado |
|---|---|---|
| Reuters news dataset | Classificação de tópicos | ~20 mil artigos |
| 20 Newsgroups | Classificação de tópicos | ~20 mil documentos |
| Amazon Product Reviews | Análise de sentimentos | ~143 milhões de avaliações |
| IMDB reviews | Análise de sentimentos | ~25 mil críticas de filmes |
| Twitter Airline Sentiment | Análise de sentimentos | ~15 mil tweets |
| Spambase | Detecção de spam | ~4,6 mil e-mails rotulados |
| SMS Spam Collection | Detecção de spam | ~5,5 mil SMS rotuladas (dataset usado no capítulo) |

### 3.2 Ferramentas utilizadas

- **Google Colab (Colaboratory):** ambiente Jupyter Notebook gratuito, sem configuração, executado na nuvem; requer conta Gmail. Permite escrever/executar código, salvar/compartilhar análises e usar recursos de computação pelo navegador.
- **UC Irvine Machine Learning Repository (UCI):** repositório mantido pela UCI com mais de 490 conjuntos de dados (DUA; GRAFF, 2019); fonte do **SMS Spam Collection Data Set** usado no exemplo prático.

### 3.3 Exploração dos dados

Usa-se a biblioteca **Pandas**: o `DataFrame` é uma estrutura tabular, bidimensional, mutável em tamanho, podendo ser heterogênea, com eixos rotulados (linhas e colunas) — composto por **dados, linhas e colunas**.

No dataset SMS Spam Collection: **5.572 registros** (IDs de 0 a 5.571); coluna 0 = rótulo da classe, coluna 1 = mensagem. Distribuição das classes: **4.825 "ham"** (não-spam) e **747 "spam"**.

### 3.4 Preparação dos dados (pré-processamento)

Passos realizados, na ordem apresentada pelo capítulo:

1. **Expressões regulares (regex):** usadas para identificar/substituir padrões em texto (números, e-mails, telefones, URLs, pontuação). Implementadas em Python via pacote `re`.
2. **Padronização para minúsculas:** antes das substituições, para que, por exemplo, "Love" e "love" tenham a mesma importância.
3. **Substituições por regex** (nesta ordem, no capítulo):
   - endereços de e-mail → `emailaddress`
   - URLs → `webaddress`
   - símbolos monetários (£, $) → `moneysymb`
   - números de telefone → `phonenumbr`
   - números → `numbr`
   - remoção de pontuação
   - normalização de espaços múltiplos → um espaço
   - remoção de espaços nas bordas

   **Cuidado destacado no capítulo:** as palavras de substituição (`emailaddress`, `webaddress` etc.) precisam ser escolhidas de forma que **não colidam** com palavras que já existem naturalmente no texto — senão a frequência dessas palavras seria artificialmente inflada.

4. **Remoção de *stop words*:** palavras de "parada", comuns no idioma e de pouco valor discriminativo para a classificação (ex. em inglês: *i, me, my, myself, we, our, ours*).
5. **Stemming (radicalização):** substituir uma palavra por sua variante morfológica de base (ex.: *programs, programer, programing, programers* → *program*).

**Biblioteca usada para stopwords/stemming/tokenização:** **NLTK** (Natural Language Toolkit).

### 3.5 Extração de recursos (*features*) e vetorização

Para treinar o classificador, o texto precisa virar uma **representação numérica (vetor)**:

1. Criar um conjunto de todas as palavras do texto e contar a **frequência** de cada uma.
2. Selecionar as palavras **mais frequentes** (no exemplo: as **1.500 mais frequentes**) para formar o **vetor-modelo de features**.
3. Para cada mensagem, gerar um vetor de *features* (dicionário `{palavra: True/False}` indicando se a palavra aparece ou não na mensagem).
4. Associar cada vetor de *features* ao seu rótulo (0 = ham, 1 = spam), formando tuplas (*features*, rótulo).

**Observação importante do capítulo:** "quantidade não significa qualidade" — é preciso cuidado com quais palavras entram no vetor-modelo, pois o classificador considera até palavras que aparecem **uma única vez** em todo o texto.

**Conversão de rótulos:** usa-se `LabelEncoder` (do `sklearn.preprocessing`) para converter rótulos categóricos (ham/spam) em valores binários (0/1).

**Embaralhamento (shuffle):** as mensagens são embaralhadas (com `seed` fixa para reprodutibilidade) para que a **ordem não interfira** no treinamento.

### 3.6 O classificador Naïve Bayes — teoria

Naïve Bayes é um algoritmo de **aprendizagem de máquina supervisionado**, da família dos algoritmos **probabilísticos**, baseado na **teoria das probabilidades** e no **teorema de Bayes**. Prediz o conteúdo de um texto atribuindo-lhe um rótulo (nome de classe). Chama-se "ingênuo" (*naïve*) porque faz uma suposição simplista: trata as *features* como **independentes entre si**.

Funcionamento: calcula a probabilidade de cada classe para um documento e produz como saída o rótulo da classe com **maior probabilidade**.

**Teorema de Bayes — elementos:**
- **c** (classe/hipótese): ex. spam / não_spam.
- **d** (documento/dados): ex. uma mensagem de SMS.
- **P(c):** probabilidade *a priori* da hipótese *c* (confiança na hipótese sem ver os dados).
- **P(d|c):** probabilidade de *d* dado *c*.
- **P(d):** probabilidade *a priori* sobre as amostras de treino *d*.
- **P(c|d):** probabilidade de *c* dado *d* (o que se quer calcular).

Como o objetivo é apenas **comparar** qual classe tem maior probabilidade, o divisor comum **P(d)** pode ser descartado nas duas comparações.

**Problema da contagem zero e Laplace Smoothing:** se uma palavra nunca aparece nos dados de treino de uma classe, a probabilidade fica zero e anula toda a multiplicação. Solução: **Laplace Smoothing** (ou *Additive Smoothing*) — soma-se **1** a toda contagem, de modo que nenhuma probabilidade seja zero. O denominador é ajustado somando a **quantidade de palavras distintas** do vocabulário.

### 3.7 Exemplo matemático do capítulo (Quadros 1 e 2)

**Quadro 1 — mensagens rotuladas e mensagem de teste:**

| # | Palavras | Classe |
|---|---|---|
| Treino 0 | Compre Viagra sem juros | SPAM |
| Treino 1 | passar mercado abastecer geladeira | NÃO-SPAM |
| Treino 2 | Viagra barato medicamento | SPAM |
| Treino 3 | Medicamento estimulador preço baixo | SPAM |
| Treino 4 | deixei prato feito geladeira | NÃO-SPAM |
| Teste 5 | Medicamento emagrecedor sem frete | ? |

Probabilidades *a priori*: **P(spam) = 3/5**; **P(não_spam) = 2/5**.

**Vocabulário com Laplace Smoothing:** 16 palavras distintas no conjunto (compre, Viagra, sem, juros, passar, mercado, abastecer, geladeira, barato, medicamento, estimulador, preço, baixo, deixei, prato, feito). Classe spam tem **11** palavras (total, com repetição); classe não-spam tem **8**.

**Quadro 2 — probabilidades de cada palavra da frase-teste, com suavização:**

| Palavra | P(palavra\|spam) | P(palavra\|não-spam) |
|---|---|---|
| medicamento | (2+1)/(11+16) = 0,111111111111111 | (0+1)/(8+16) = 0,041666666666667 |
| emagrecedor | (0+1)/(11+16) = 0,037037037037037 | (0+1)/(8+16) = 0,041666666666667 |
| sem | (0+1)/(11+16) = 0,037037037037037 | (0+1)/(8+16) = 0,041666666666667 |
| frete | (0+1)/(11+16) = 0,037037037037037 | (0+1)/(8+16) = 0,041666666666667 |

**Resultado da multiplicação das 4 probabilidades:**
- P(spam) × produto = **0,00000564502**
- P(não_spam) × produto = **0,00000301408**

**Conclusão do exemplo:** a mensagem "medicamento emagrecedor sem frete" é classificada como **SPAM**, pois teve a maior probabilidade final.

### 3.8 Treinamento e teste do modelo (metodologia)

**Divisão treino/teste** — necessária para avaliar se o modelo **generaliza** (prediz bem dados nunca vistos) ou sofreu ***overfitting*** (decorou os dados de treino, memorizando em vez de "aprender"; sintoma: alta precisão no treino, baixa no teste).

Existe ainda, eventualmente, um terceiro conjunto — **dados de desenvolvimento** —, usado enquanto se testam diferentes configurações/variações do classificador.

**`train_test_split`** (de `sklearn.model_selection`) — parâmetros principais:

| Parâmetro | Função |
|---|---|
| `*arrays` | Conjunto(s) de dados (listas, arrays numpy, matrizes scipy-sparse ou DataFrame pandas) |
| `train_size` | Tamanho do conjunto de treino: `None` (padrão), `int` (nº exato de amostras) ou `float` (0,1 a 1,0) |
| `test_size` | Tamanho do conjunto de teste; padrão 0,25 se `train_size` for `None` |
| `random_state` | Fixa a semente para tornar a divisão reproduzível |

**Classificador — `MultinomialNB`** (de `sklearn.naive_bayes`), adequado para *features* **discretas** (ex. contagem de palavras). Parâmetros:

| Parâmetro | Função |
|---|---|
| `alpha` | (float) parâmetro de suavização Laplace/Lidstone (0 = sem suavização) |
| `fit_prior` | (bool) se deve aprender as probabilidades *a priori* das classes a partir dos dados |
| `class_prior` | (array) probabilidades *a priori* definidas manualmente; se especificado, não são ajustadas pelos dados |

**Conversão de formato:** os dados em dicionário precisam virar **matriz** (lista de listas) antes de entrar no `MultinomialNB`. Usa-se `DictVectorizer` (de `sklearn.feature_extraction`).

### 3.9 Avaliação do modelo

**Tabela de contingência / Matriz de confusão (2×2, caso binário spam/ham):**

| | Predito: spam | Predito: não-spam |
|---|---|---|
| **Real: spam** | VP (verdadeiro-positivo) | FN (falso-negativo) |
| **Real: ham** | FP (falso-positivo) | VN (verdadeiro-negativo) |

**Métricas:**

| Métrica | Fórmula | O que mede |
|---|---|---|
| **Acurácia** | (VP + VN) / (VP + VN + FP + FN) | Assertividade geral do modelo, para todas as classes |
| **Precisão** | VP / (VP + FP) | Assertividade apenas para uma classe específica |
| **Revocação (*recall*)** | VP / (VP + FN) | Frequência com que os exemplos de uma classe foram corretamente encontrados |
| **F1-score** | (2 × precisão × revocação) / (precisão + revocação) | Média harmônica entre precisão e revocação; quanto maior, melhor o modelo |

Ferramentas: `confusion_matrix` e `classification_report` (ambas de `sklearn.metrics`).

### 3.10 Ajuste de hiperparâmetros

Classificadores em geral têm vários parâmetros ajustáveis (*hiperparâmetros*). Testar manualmente todas as combinações é inviável (exemplo do capítulo: 2 parâmetros, um com 100 valores possíveis e outro booleano → **200 combinações**).

**Duas técnicas de busca:**

| Técnica | Como funciona | Quando usar |
|---|---|---|
| ***Grid Search*** | Testa **exaustivamente** todas as combinações possíveis | Dataset relativamente pequeno, muitos parâmetros a ajustar → resultados mais precisos |
| ***Random Search*** | Testa combinações **aleatórias** dos valores | Datasets grandes e muitas dimensões de ajuste → custo computacional do Grid Search fica muito alto |

Ferramenta: `GridSearchCV` (de `sklearn.model_selection`), que otimiza por **validação cruzada**.

### 3.11 Naïve Bayes: prós e contras (síntese do capítulo)

**A favor:**
- Bom desempenho na predição da classe correta, mesmo sendo "ingênuo".
- Funciona bem em situações reais (classificação de documentos, filtragem de spam).
- Rápido na execução; tem bom desempenho mesmo com poucos dados.
- Relativamente simples de configurar para aplicações rotineiras.

**Contra:**
- A suposição de independência entre *features* limita a exploração de interações reais entre os dados (ainda que, na prática, isso não costume prejudicar tarefas de classificação de texto).
- Se uma variável do conjunto de teste **nunca foi vista** no treino, o modelo atribui probabilidade **0** e não consegue prever com precisão (o próprio Laplace Smoothing, aplicado no treino, mitiga esse problema).

---

## 4. Exemplos, Aplicações e Material Prático

O código completo deste capítulo (obtenção dos dados, regex, NLTK, vetorização, treinamento, avaliação e ajuste de hiperparâmetros) foi organizado em arquivo complementar, pronto para compilação em Jupyter Notebook:

➡️ **`AULA_04_CLASSIFICACAO_TEXTO_PYTHON_PRATICO.md`**

---

## 5. Minhas Observações e Dúvidas

*(Espaço reservado — nenhuma observação registrada até o momento para esta aula.)*

### Pontos de atenção no texto-base (identificados na análise; não são observações da aluna)
1. **Pequena inconsistência de nomenclatura no Quadro 2:** a tabela traz "P(palavra|não-spam)" na coluna, mas o texto corrido logo acima usa "não_spam" (com *underscore*). Mesmo conceito, grafias diferentes dentro do próprio capítulo.
2. **Trecho de código com erro tipográfico evidente (OCR/editoração do livro):** nas variáveis Python, o PDF mostra espaços estranhos dentro de identificadores (ex.: `pd.read _ ta ble`, `word _ tokens`, `train _ test _ split`). Isso é um artefato de formatação do PDF original (não um erro do leitor) — no arquivo prático, os nomes foram corrigidos para a sintaxe Python real (`read_table`, `word_tokens`, `train_test_split`), já que o código como está no PDF não executaria.
3. **MultinomialNB em dados booleanos:** o capítulo monta as *features* como `True`/`False` (palavra presente ou não) e depois diz que a distribuição multinomial "normalmente requer contagens de recursos inteiros". Isso é uma inconsistência técnica do capítulo: o ideal para dados binários (presença/ausência) seria o `BernoulliNB`, não o `MultinomialNB` — mas o `DictVectorizer`, ao vetorizar dicionários com `True`/`False`, converte esses valores para `1.0`/`0.0`, o que faz o `MultinomialNB` funcionar ainda que não seja a escolha teoricamente mais alinhada ao tipo de dado.

---

## 6. Referências e Conexões com Outros Conteúdos

### Referência principal
MARTINS, Juliano Vieira. **Processamento de Linguagem Natural** — capítulo "Classificação de textos — Utilizando Python para construir e treinar modelos de machine learning". SAGAH.

### Referências citadas no capítulo
- DUA, D.; GRAFF, C. *UCI Machine Learning Repository.* Irvine, CA: University of California, 2019.
- GOOGLE COLABORATORY. Mountain View, CA: Google, c2020.
- JURAFSKY, D. S.; MARTIN, H. *Speech and language processing: an introduction to natural language processing, computational linguistics, and speech recognition.* 3. ed. New Jersey: Prentice Hall, 2019.
- NATURAL LANGUAGE TOOLKIT. *NLTK 3.5 documentation.* 2020.
- NUMPY. c2020.
- PANDAS. *Python Data Analysis Library.* Texas: Zenodo, 2020.
- PYTHON. Wilmington: Python Software Foundation, c2020.
- SCIKIT-LEARN: *Machine learning in Python.* c2020.

### Conexões com outras aulas e disciplinas
- **Aula 3 (Classificação de textos — introdução ao aprendizado supervisionado):** esta aula é a aplicação prática direta da teoria vista lá — tokenização, remoção de stopwords e pontuação (Aula 3, seção de pré-processamento) reaparecem aqui como código real com NLTK e regex; o Naïve Bayes citado na Aula 3 (como um dos algoritmos do pipeline) é aprofundado matematicamente aqui.
- **Aula 1 (Aprendizado de Máquina):** Naïve Bayes já constava no Quadro 2 da Aula 1 como algoritmo de classificação supervisionada; esta aula mostra sua base probabilística (teorema de Bayes) e sua implementação.
- **Atividade 1 (Mineração de Dados) / Aquisição e Preparação de Dados:** o pré-processamento com regex, stopwords e normalização dialoga diretamente com os conceitos de limpeza e transformação de dados já estudados (ETL, AED).
- **Overfitting e divisão treino/teste:** conceito novo nesta aula, mas que se conecta à discussão de qualidade de dados e generalização de modelos vista de forma mais geral na Aula 1.

---

**Status:** Aula 4 documentada.
