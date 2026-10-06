# AULA 1 — APRENDIZADO DE MÁQUINA (MACHINE LEARNING)

## Disciplina: Aprendizado de Máquina Supervisionado — Graduação em IA (FMU)

---

## 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Supervisionado
**Aula:** 1 — Aprendizado de Máquina (Machine Learning)
**Fonte:** *Introdução a Big Data e Internet das Coisas (IoT)* — Izabelly Soares de Morais, SAGAH (Soluções Educacionais Integradas), capítulo "Aprendizado de máquina (Machine Learning)"
**Formato de avaliação:** Atividade dissertativa (não há questões objetivas nesta aula)

### Objetivos de aprendizagem (conforme o capítulo)
- Definir aprendizado de máquina.
- Descrever algoritmos de aprendizado de máquina.
- Listar aplicações de aprendizado de máquina.

---

## 2. Resumo e Contextualização

O capítulo introduz o aprendizado de máquina (AM) como a junção entre recursos computacionais, inteligência artificial e dados, com sistemas capazes não apenas de memorizar dados, mas de observá-los e explorá-los para evoluir suas habilidades por meio da prática.

A autora situa o AM dentro de um ecossistema conceitual maior:
- **Inteligência Artificial** → fornece conhecimento às máquinas por meio de dados.
- **Aprendizado de Máquina** → técnicas computacionais para encontrar **padrões ocultos** em dados (Amaral, 2016).
- **Mineração de Dados** → aplicação desses algoritmos em grandes conjuntos de dados para extrair informação e conhecimento (distinção importante: AM busca reconhecer padrões; mineração de dados aplica esses padrões em larga escala).
- **Big Data** → fornece o volume de dados necessário para que o AM tenha "ativo suficiente".

Esta aula é conceitualmente anterior/complementar à disciplina anterior (Aquisição e Preparação de Dados): ali o foco era ETL, qualidade e normalização de dados; aqui o foco passa a ser **como esses dados tratados alimentam algoritmos que aprendem**.

---

## 3. Conceitos Fundamentais e Explicações

### 3.1 Definição de Aprendizado de Máquina

> "Aprendizado de máquina computacional (AM) é a aplicação de técnicas computacionais com o objetivo de encontrar padrões ocultos em dados." (Amaral, 2016)

Segundo Coppin (2010), na maioria dos problemas de aprendizado a tarefa é **aprender a classificar entradas** de acordo com um conjunto finito (ou infinito) de classificações. O sistema recebe um **conjunto de dados de treinamento** já classificado manualmente e tenta aprender a partir dele como classificar tanto esses dados quanto novos dados ainda não observados.

### 3.2 Quadro 1 — Conceitos do Aprendizado de Máquina

| Conceito | Descrição |
|---|---|
| **Treinamento** | Uso de algoritmos e inserção de dados para que a máquina adquira os conhecimentos necessários para desempenhar suas funções |
| **Indução** | Processo de busca da melhor hipótese — a melhor resposta/solução para determinada situação |
| **Regras** | Limitam as possibilidades do algoritmo de aprendizado |
| **Hipóteses** | Possíveis conclusões/respostas predeterminadas, provadas ou não ao final |

### 3.3 Caracterização dos Dados

**Tipo do dado:**
- **Quantitativo** (numérico)
- **Qualitativo**, subdividido em:
  - **Simbólico** — facilmente compreendido por humanos
  - **Categórico** — valores em conjunto finito

**Escalas (definem quais operações são possíveis com os valores de cada atributo):**

| Escala | Característica | Exemplo |
|---|---|---|
| **Nominal** | Valores com nomes diferentes, pouca informação | RG, CPF |
| **Ordinal** | Relacionada à ordem das categorias | Frio/quente |
| **Intervalar** | Números que variam dentro de um intervalo | Temperatura entre 10–15 °C |
| **Racional** | Traz mais informação sobre o atributo | Nº de vezes que um aluno cursou a disciplina |

Dados também podem ser **contínuos** (valor indefinido dentro de um intervalo) ou **discretos** (valores definidos).

### 3.4 Exploração dos Dados

- **Estatística descritiva** — resume quantitativamente as características mais relevantes de um conjunto de dados.
- **Dados univariados** — um mesmo atributo pode se repetir para diferentes registros; subdivididos em:
  - *Medidas de localidade* (pontos de referência, numéricos ou simbólicos)
  - *Medidas de espalhamento* (intervalo, variância, desvio padrão)
  - *Medidas de distribuição* (definidas pela média do conjunto)
- **Dados multivariados** — possuem mais de um atributo de entrada.

### 3.5 Pré-processamento de Dados

Necessário porque dados de fontes variadas podem conter ruídos, imperfeições, duplicações etc. Técnicas citadas:

- **Eliminação manual de atributos** — remoção de atributos irrelevantes
- **Integração de dados** — identificação de objetos e seus conjuntos
- **Amostragem de dados** — representação dos dados originais
- **Dados desbalanceados** — correção via redefinição de conjunto, classificadores para diferentes classes etc.
- **Limpeza dos dados** — elimina dados incompletos, inconsistentes, redundantes e com ruído
- **Transformação dos dados** — conversões simbólico-numéricas, numérico-simbólicas, transformação de atributos
- **Redução de dimensionalidade** — via agregação, seleção de atributos, técnicas de ordenação/seleção de subconjuntos

> **Conexão com a disciplina anterior:** este bloco dialoga diretamente com a Aula 2 (ETL) e a Aula 4 (AED) de Aquisição e Preparação de Dados — os mesmos problemas (missing values, outliers, normalização) reaparecem aqui como pré-condição para o aprendizado de máquina.

### 3.6 Tipos de Aprendizado de Máquina

- **Supervisionado** — objetivo estabelecido; dividido em problemas de **regressão** e **classificação**.
- **Não supervisionado** — objetivo não bem definido; busca compreender os dados para realizar **agrupamento**.
- **Por reforço** — saídas não bem definidas; respostas só podem ser aferidas após execuções.
- **Semissupervisionado** (mencionado à parte) — usado quando há pouca quantidade de dados rotulados; dados não rotulados complementam o conjunto de treinamento.

### 3.7 Hierarquia do Aprendizado Indutivo (Figura 2, Carvalho et al., 2011, p. 6)

```
                    Aprendizado Indutivo
                    /                  \
            Supervisionado        Não Supervisionado
            (preditivo)            (descritivo)
            /          \           /      |        \
    Classificação   Regressão  Agrupamento Associação Sumarização
```

- **Aprendizado supervisionado (preditivo):** recebe dados rotulados como entrada e usa esses dados/atributos para determinar um novo conjunto de dados desconhecidos. Passa por uma etapa de **treinamento**, na qual o classificador aprende um padrão conforme os dados de treino.
  - **Regressão** — mapeia um exemplo em um valor real (ex.: prever tempo de internação de um paciente).
  - **Classificação** — associa a descrição de um objeto a uma classe (ex.: determinar a doença de um paciente pelos sintomas).

- **Aprendizado não supervisionado (descritivo):** agrupa objetos de acordo com suas características; recebe dados do tipo {x1, x2...xn} e encontra associações entre eles.
  - **Agrupamento** — dados agrupados por similaridade.
  - **Sumarização** — busca descrição simples e compacta de um conjunto de dados.
  - **Associação** — encontra padrões frequentes de associação entre atributos.

### 3.8 Algoritmo, Hipótese e Viés

**Algoritmo** = passo a passo da resolução de um problema, traduzido em linguagem de programação.

O algoritmo de AM aprende a **induzir uma função ou hipótese** capaz de resolver um problema a partir de um **conjunto de dados de treinamento** que representa instâncias do problema.

- **Hipótese** — ideia inicial/suposição a ser comprovada ou não.
- **Atributos (ou variáveis)** — características de um objeto (ex.: nome, idade, sexo, ano escolar de um aluno).
- **Viés** — responsável por restringir as hipóteses visitadas no espaço de busca.
  - *Viés de busca* — como o algoritmo procura a melhor hipótese.
  - *Viés de representação* — forma como a hipótese é representada (redes neurais, árvores de decisão, conjunto de regras — Figura 1).
- **Tarefas de aprendizado:**
  - *Preditivas* — buscam antecipar.
  - *Descritivas* — buscam descrever um conjunto de dados.

---

## 4. Exemplos, Aplicações e Material Prático

### 4.1 Quadro 2 — Algoritmos de Aprendizado de Máquina

**Supervisionados:**

| Tipo | Algoritmo | Características |
|---|---|---|
| Regressão | Regressão linear | Recebe valores de variáveis e, por meio de equações, estima resultados aplicáveis a outras variáveis |
| Classificação | Naïve Bayes | Calcula a probabilidade de algo após as variáveis terem sido caracterizadas |
| Classificação | Máquina de Vetor de Suporte (SVM) | Constrói modelo indicando onde o objeto se enquadra, usando classificador + analisador por regressão (linear binário não probabilístico) |
| Classificação | Regressão logística | Define características semelhantes entre grupos de variáveis |
| Classificação | Árvores de decisão | Busca top-down nos dados, calculando árvores possíveis; reduzida quando muito complexa; classifica percorrendo a árvore até a folha |
| Classificação | Redes neurais artificiais | Baseadas no sistema biológico de neurônios interligados; aprendem exemplos e generalizam conceitos |
| Classificação | K-Vizinhos mais próximos (KNN) | Classifica um item comparando sua similaridade com os dados de treinamento |

**Não supervisionados:**

| Tipo | Algoritmo | Características |
|---|---|---|
| Agrupamento | K-Means | Algoritmo particional; divide dados em K grupos (clusters) não interseccionados; cada grupo representado pelo seu centro |
| Agrupamento | Hierárquicos | Geram sequência de partições aninhadas com base em matriz de proximidade; resultado depende da ordem de entrada dos dados |
| Agrupamento | Grafos | Agrupamento via grafos de proximidade |

*Fonte: Adaptado de Ferreira Junior (2015), Silva (2016), Dias, Pascutti e Silva (2016) e Carvalho et al. (2011).*

### 4.2 Figura 1 — Diferentes Vieses de Representação (exemplo do capítulo)

```
Árvore de decisão:
              Peso
           <50    ≥50
            |       \
          Sexo     Doente
         M/  \F
    Doente  Saudável

Conjunto de regras equivalente:
- Se Peso ≥ 50 então Doente
- Se Peso < 50 e Sexo = M então Doente
- Se Peso < 50 e Sexo = F então Saudável

Redes neurais: representação por matriz de pesos numéricos
(ex.: 0,45  -0,40  0,54  0,12  0,98  0,37 ...)
```

### 4.3 Aplicações Citadas no Capítulo

- **Varejo on-line** (Google Cloud, 2017) — algoritmos processam dados de navegação para prever comportamento de compra e personalizar ofertas em escala.
- **Energia** — previsão de carga e preço, planejamento de expansão, redistribuição de alimentadores, agendamento de geradores, minimização de perdas, proteção de sistemas.
- **Saúde** — mapeamento de características comuns em epidemias; uso de idade, sexo, histórico de doenças para diagnóstico.
- **Prevenção de incêndios florestais** (Cortez e Morais, 2007 apud Carvalho et al., 2011) — comparação de 5 algoritmos (árvores de decisão, florestas aleatórias, SVM, regressão múltipla, redes neurais); melhor resultado com **SVM** usando 4 atributos meteorológicos (temperatura, umidade relativa, precipitação, velocidade do vento).

---

## 5. Minhas Observações e Dúvidas

*(Espaço reservado — nenhuma observação registrada até o momento para esta aula. A avaliação será dissertativa, conforme indicado.)*

---

## 6. Referências e Conexões com Outros Conteúdos

### Referência principal
MORAIS, Izabelly Soares de. **Introdução a Big Data e Internet das Coisas (IoT)** — capítulo "Aprendizado de máquina (Machine Learning)". SAGAH.

### Referências citadas no capítulo
- AMARAL, F. *Introdução à ciência de dados: mineração de dados e big data*. Rio de Janeiro: Alta Books, 2016.
- CARVALHO, A. C. P. L. F. et al. *Inteligência artificial: uma abordagem de aprendizagem de máquina*. Rio de Janeiro: LTC, 2011.
- COPPIN, B. *Inteligência artificial*. Rio de Janeiro: LTC, 2010.
- DIAS, M. F. R.; PASCUTTI, P. G.; SILVA, M. L. *Aprendizado de máquina e suas aplicações em bioinformática*. Revista Semioses, v. 10, n. 1, 2016.
- FERREIRA JÚNIOR, M. M. *Modelos computacionais baseados em aprendizado de máquina para classificação e agrupamento de variedade de tucumã*. Dissertação (Mestrado) — UFAM, Itacoatiara, 2015.
- GOOGLE CLOUD. *Guia sobre análise de dados e aprendizado de máquina para CIO*. 2017.
- SILVA, M. C. R. *Aprendizagem de máquina em apoio ao diagnóstico em ortopedia*. Dissertação (Mestrado) — PUC-Campinas, 2016.

### Leituras recomendadas (citadas no capítulo)
- MITCHELL, T. M. *Machine learning*. New York: McGraw-Hill, 1997.
- ROSA, J. L. G. *Fundamentos da inteligência artificial*. Rio de Janeiro: LTC, 2011.
- SOUTO, M. C. P. et al. *Técnicas de aprendizado de máquina para problemas de biologia molecular*. CSBC, 2003.

### Conexões com outras disciplinas da grade
- **Aquisição e Preparação de Dados (262GGR6046A):** o pré-processamento descrito aqui (limpeza, transformação, redução de dimensionalidade, dados desbalanceados) retoma diretamente os conceitos de ETL (Aula 2) e AED (Aula 4) já estudados.
- **Aprendizado de Máquina Não Supervisionado (262GGR6044A):** a Aula 1 dessa disciplina já havia introduzido a distinção supervisionado/não supervisionado; este capítulo aprofunda especificamente o lado **supervisionado** (regressão e classificação) e detalha algoritmos que ali foram apenas mencionados.

---

**Status:** Aula 1 documentada — aguardando avaliação dissertativa.
