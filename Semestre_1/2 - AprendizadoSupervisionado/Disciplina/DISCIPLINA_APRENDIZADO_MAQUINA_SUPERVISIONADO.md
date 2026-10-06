# DISCIPLINA: APRENDIZADO DE MÁQUINA SUPERVISIONADO (262GGR4728A)

## Graduação em Inteligência Artificial — FMU

**Autora:** Daniela Emiliano de Souza Chacon — RA: 2026229221
**Compilação:** Estudo estruturado com apoio de IA
**Status:** 4 aulas documentadas | 3 atividades registradas (A1, A2, A3)

---

## Índice

1. [Aula 1 — Aprendizado de Máquina (Machine Learning)](#aula-1--aprendizado-de-máquina-machine-learning)
2. [Aula 2 — Business Performance Management (BPM)](#aula-2--business-performance-management-bpm)
3. [Aula 3 — Classificação de textos: introdução ao aprendizado supervisionado](#aula-3--classificação-de-textos-introdução-ao-aprendizado-supervisionado)
4. [Aula 4 — Classificação de textos: utilizando Python para construir e treinar modelos de ML](#aula-4--classificação-de-textos-utilizando-python-para-construir-e-treinar-modelos-de-machine-learning)
   - 4.1 Material prático (código Python completo)
   - 4.2 Anexo: Laboratório guiado para VSCode
5. [Atividades e Avaliações](#atividades-e-avaliações)
6. [Desempenho Consolidado](#desempenho-consolidado)

---

## AULA 1 — APRENDIZADO DE MÁQUINA (MACHINE LEARNING)


---

### 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Supervisionado
**Aula:** 1 — Aprendizado de Máquina (Machine Learning)
**Fonte:** *Introdução a Big Data e Internet das Coisas (IoT)* — Izabelly Soares de Morais, SAGAH (Soluções Educacionais Integradas), capítulo "Aprendizado de máquina (Machine Learning)"
**Formato de avaliação:** Atividade dissertativa (não há questões objetivas nesta aula)

#### Objetivos de aprendizagem (conforme o capítulo)
- Definir aprendizado de máquina.
- Descrever algoritmos de aprendizado de máquina.
- Listar aplicações de aprendizado de máquina.

---

### 2. Resumo e Contextualização

O capítulo introduz o aprendizado de máquina (AM) como a junção entre recursos computacionais, inteligência artificial e dados, com sistemas capazes não apenas de memorizar dados, mas de observá-los e explorá-los para evoluir suas habilidades por meio da prática.

A autora situa o AM dentro de um ecossistema conceitual maior:
- **Inteligência Artificial** → fornece conhecimento às máquinas por meio de dados.
- **Aprendizado de Máquina** → técnicas computacionais para encontrar **padrões ocultos** em dados (Amaral, 2016).
- **Mineração de Dados** → aplicação desses algoritmos em grandes conjuntos de dados para extrair informação e conhecimento (distinção importante: AM busca reconhecer padrões; mineração de dados aplica esses padrões em larga escala).
- **Big Data** → fornece o volume de dados necessário para que o AM tenha "ativo suficiente".

Esta aula é conceitualmente anterior/complementar à disciplina anterior (Aquisição e Preparação de Dados): ali o foco era ETL, qualidade e normalização de dados; aqui o foco passa a ser **como esses dados tratados alimentam algoritmos que aprendem**.

---

### 3. Conceitos Fundamentais e Explicações

#### 3.1 Definição de Aprendizado de Máquina

> "Aprendizado de máquina computacional (AM) é a aplicação de técnicas computacionais com o objetivo de encontrar padrões ocultos em dados." (Amaral, 2016)

Segundo Coppin (2010), na maioria dos problemas de aprendizado a tarefa é **aprender a classificar entradas** de acordo com um conjunto finito (ou infinito) de classificações. O sistema recebe um **conjunto de dados de treinamento** já classificado manualmente e tenta aprender a partir dele como classificar tanto esses dados quanto novos dados ainda não observados.

#### 3.2 Quadro 1 — Conceitos do Aprendizado de Máquina

| Conceito | Descrição |
|---|---|
| **Treinamento** | Uso de algoritmos e inserção de dados para que a máquina adquira os conhecimentos necessários para desempenhar suas funções |
| **Indução** | Processo de busca da melhor hipótese — a melhor resposta/solução para determinada situação |
| **Regras** | Limitam as possibilidades do algoritmo de aprendizado |
| **Hipóteses** | Possíveis conclusões/respostas predeterminadas, provadas ou não ao final |

#### 3.3 Caracterização dos Dados

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

#### 3.4 Exploração dos Dados

- **Estatística descritiva** — resume quantitativamente as características mais relevantes de um conjunto de dados.
- **Dados univariados** — um mesmo atributo pode se repetir para diferentes registros; subdivididos em:
  - *Medidas de localidade* (pontos de referência, numéricos ou simbólicos)
  - *Medidas de espalhamento* (intervalo, variância, desvio padrão)
  - *Medidas de distribuição* (definidas pela média do conjunto)
- **Dados multivariados** — possuem mais de um atributo de entrada.

#### 3.5 Pré-processamento de Dados

Necessário porque dados de fontes variadas podem conter ruídos, imperfeições, duplicações etc. Técnicas citadas:

- **Eliminação manual de atributos** — remoção de atributos irrelevantes
- **Integração de dados** — identificação de objetos e seus conjuntos
- **Amostragem de dados** — representação dos dados originais
- **Dados desbalanceados** — correção via redefinição de conjunto, classificadores para diferentes classes etc.
- **Limpeza dos dados** — elimina dados incompletos, inconsistentes, redundantes e com ruído
- **Transformação dos dados** — conversões simbólico-numéricas, numérico-simbólicas, transformação de atributos
- **Redução de dimensionalidade** — via agregação, seleção de atributos, técnicas de ordenação/seleção de subconjuntos

> **Conexão com a disciplina anterior:** este bloco dialoga diretamente com a Aula 2 (ETL) e a Aula 4 (AED) de Aquisição e Preparação de Dados — os mesmos problemas (missing values, outliers, normalização) reaparecem aqui como pré-condição para o aprendizado de máquina.

#### 3.6 Tipos de Aprendizado de Máquina

- **Supervisionado** — objetivo estabelecido; dividido em problemas de **regressão** e **classificação**.
- **Não supervisionado** — objetivo não bem definido; busca compreender os dados para realizar **agrupamento**.
- **Por reforço** — saídas não bem definidas; respostas só podem ser aferidas após execuções.
- **Semissupervisionado** (mencionado à parte) — usado quando há pouca quantidade de dados rotulados; dados não rotulados complementam o conjunto de treinamento.

#### 3.7 Hierarquia do Aprendizado Indutivo (Figura 2, Carvalho et al., 2011, p. 6)

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

#### 3.8 Algoritmo, Hipótese e Viés

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

### 4. Exemplos, Aplicações e Material Prático

#### 4.1 Quadro 2 — Algoritmos de Aprendizado de Máquina

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

#### 4.2 Figura 1 — Diferentes Vieses de Representação (exemplo do capítulo)

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

#### 4.3 Aplicações Citadas no Capítulo

- **Varejo on-line** (Google Cloud, 2017) — algoritmos processam dados de navegação para prever comportamento de compra e personalizar ofertas em escala.
- **Energia** — previsão de carga e preço, planejamento de expansão, redistribuição de alimentadores, agendamento de geradores, minimização de perdas, proteção de sistemas.
- **Saúde** — mapeamento de características comuns em epidemias; uso de idade, sexo, histórico de doenças para diagnóstico.
- **Prevenção de incêndios florestais** (Cortez e Morais, 2007 apud Carvalho et al., 2011) — comparação de 5 algoritmos (árvores de decisão, florestas aleatórias, SVM, regressão múltipla, redes neurais); melhor resultado com **SVM** usando 4 atributos meteorológicos (temperatura, umidade relativa, precipitação, velocidade do vento).

---

### 5. Minhas Observações e Dúvidas

*(Espaço reservado — nenhuma observação registrada até o momento para esta aula. A avaliação será dissertativa, conforme indicado.)*

---

### 6. Referências e Conexões com Outros Conteúdos

#### Referência principal
MORAIS, Izabelly Soares de. **Introdução a Big Data e Internet das Coisas (IoT)** — capítulo "Aprendizado de máquina (Machine Learning)". SAGAH.

#### Referências citadas no capítulo
- AMARAL, F. *Introdução à ciência de dados: mineração de dados e big data*. Rio de Janeiro: Alta Books, 2016.
- CARVALHO, A. C. P. L. F. et al. *Inteligência artificial: uma abordagem de aprendizagem de máquina*. Rio de Janeiro: LTC, 2011.
- COPPIN, B. *Inteligência artificial*. Rio de Janeiro: LTC, 2010.
- DIAS, M. F. R.; PASCUTTI, P. G.; SILVA, M. L. *Aprendizado de máquina e suas aplicações em bioinformática*. Revista Semioses, v. 10, n. 1, 2016.
- FERREIRA JÚNIOR, M. M. *Modelos computacionais baseados em aprendizado de máquina para classificação e agrupamento de variedade de tucumã*. Dissertação (Mestrado) — UFAM, Itacoatiara, 2015.
- GOOGLE CLOUD. *Guia sobre análise de dados e aprendizado de máquina para CIO*. 2017.
- SILVA, M. C. R. *Aprendizagem de máquina em apoio ao diagnóstico em ortopedia*. Dissertação (Mestrado) — PUC-Campinas, 2016.

#### Leituras recomendadas (citadas no capítulo)
- MITCHELL, T. M. *Machine learning*. New York: McGraw-Hill, 1997.
- ROSA, J. L. G. *Fundamentos da inteligência artificial*. Rio de Janeiro: LTC, 2011.
- SOUTO, M. C. P. et al. *Técnicas de aprendizado de máquina para problemas de biologia molecular*. CSBC, 2003.

#### Conexões com outras disciplinas da grade
- **Aquisição e Preparação de Dados (262GGR6046A):** o pré-processamento descrito aqui (limpeza, transformação, redução de dimensionalidade, dados desbalanceados) retoma diretamente os conceitos de ETL (Aula 2) e AED (Aula 4) já estudados.
- **Aprendizado de Máquina Não Supervisionado (262GGR6044A):** a Aula 1 dessa disciplina já havia introduzido a distinção supervisionado/não supervisionado; este capítulo aprofunda especificamente o lado **supervisionado** (regressão e classificação) e detalha algoritmos que ali foram apenas mencionados.

---

## AULA 2 — BUSINESS PERFORMANCE MANAGEMENT (BPM)


---

### 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Supervisionado
**Aula:** 2 — Business Performance Management (BPM)
**Fonte:** *Introdução à Inteligência de Negócios* — Aline Zanin, SAGAH (Soluções Educacionais Integradas), capítulo "Business performance management (BPM)"

#### Objetivos de aprendizagem (conforme o capítulo)
- Explicar os conceitos de estratégia, plano e monitoramento.
- Aplicar medidas de desempenho.
- Analisar metodologias de BPM.

**Observação de contexto:** esta aula muda de eixo em relação à Aula 1 (que tratou de Machine Learning propriamente dito) — o foco passa a ser gestão e inteligência de negócios (BI), um domínio de apoio à decisão que frequentemente fornece o contexto/dados para os modelos de aprendizado de máquina.

---

### 2. Resumo e Contextualização

**BPM (business performance management)**, ou gerenciamento do desempenho do negócio, é uma ferramenta de suporte à tomada de decisão. Ele abrange um conjunto de processos, metodologias, métricas e aplicações criadas para medir o desempenho geral de uma empresa, ajudando gestores a converter estratégias em planos e objetivos, e depois monitorar o desempenho em relação a esses objetivos.

O capítulo situa o BPM dentro de um conjunto maior de ferramentas com o mesmo propósito, mas nomes diferentes conforme a empresa criadora: **corporate performance management (CPM)** e **enterprise performance management (EPM)**.

> **BPM Standard Group** define BPM como "uma estrutura destinada a organizar, automatizar e analisar as metodologias de negócios, bem como as métricas, os processos e os sistemas, visando a induzir o desempenho geral da empresa" (TURBAN *et al.*, 2009).

Pontos importantes de definição:
- O BPM **faz parte** das estratégias de *business intelligence* (BI), mas não se limita a isso.
- O BPM **não é** uma tecnologia ou *software* de ERP (*enterprise resources planning*).
- Segundo Chicaleski (2008), o BPM "pode ser definido como a união de componentes, como orçamento, planejamento, [BI], integração de dados, previsões e simulações".

---

### 3. Conceitos Fundamentais e Explicações

#### 3.1 Ciclo do BPM (Figura 1, Turban et al., 2009, p. 195)

O ciclo é dividido em dois grandes eixos:
- **Eixo da estratégia** → estratégias e planos
- **Eixo da execução** → monitoramento, ação e ajustes

Conectados ao centro por **dados integrados**.

```
                    ESTRATÉGIA
        1. Fazer estratégias    2. Plano
     (planos estratégicos,     (planos, orçamentos,
      mapas estratégicos)       cenários, projetos)
                    ↕
              Dados integrados
                    ↕
     (ofertas e ações          (alertas, relatórios/
      de agentes, previsões     análise, painéis)
      e métodos)
        4. Agir e ajustar      3. Monitorar
                    EXECUÇÃO
```

**1. Estratégias** — respondem a "para onde queremos ir no futuro?". Geralmente formalizadas em um **planejamento estratégico** (mapa de ações para atingir objetivos em um período). Estratégias podem apresentar **lacunas** (gaps entre o planejado e o executado), causadas por 4 fatores principais:

| Causa da lacuna | Descrição |
|---|---|
| **Visão** | Poucos funcionários conhecem a estratégia/visão da empresa, dificultando decisões alinhadas |
| **Pessoas** | Remuneração motiva a curto prazo, mas não alinha o colaborador à visão da empresa |
| **Gerenciamento** | Gestores nem sempre identificam os problemas principais, dispersando esforços |
| **Recursos** | Equipes superestimam o orçamento disponível e não conseguem executar a estratégia |

**2. Planos** — respondem a "como chegaremos até lá?". O plano operacional converte estratégia em metas, táticas, recursos e resultados esperados. Pode ser:
- **Centrado em táticas** — práticas para atender aos objetivos do planejamento estratégico.
- **Centrado em orçamentos** — ações planejadas visando ao lucro final.

**3. Monitoramento** — garante que o plano operacional ocorre conforme esperado. Desafio principal: definir **o quê** e **como** monitorar de forma que agregue valor.

**4. Agir e ajustar** — sem plano de ação/ajuste, estratégia, plano e monitoramento perdem utilidade. Toda divergência identificada no monitoramento deve gerar ação imediata.

#### 3.2 Medidas de Desempenho — Quadro 1 (conceitos básicos)

| Conceito | Definição | Exemplo |
|---|---|---|
| **Métrica** | Marcação de um fator monitorado; ponto de registro/controle | Altura — 1,80 m; faturamento — 2 milhões |
| **Medida** | Quantidade de registros de um valor/desempenho, por acumulação | 30 clientes por dia (média); 200 mil *likes* até hoje (total) |
| **Indicador** | Fator qualitativo/quantitativo que expressa realização ou mudança; pode agregar várias medidas | 30% a mais de clientes no último ano; 10 graus de diferença entre cidades |

**Relação entre os três (Figura 2, Lawrence, 2019):**
Métrica = **marcação** (registra um valor) → Medida = **acúmulo** → Indicador = **variação** em comparação com outros cenários.

#### 3.3 Sistema de Medida de Desempenho

Conjunto de estratégias de medição de desempenho. Características de um bom sistema:
- Concentra-se em fatores cruciais.
- Mistura passado, presente e futuro.
- Equilibra necessidades de acionistas, funcionários, parceiros, fornecedores e demais interessados.
- Tem metas baseadas em pesquisa e realidade, não arbitrárias.

> Segundo Simons (2002, *apud* Turban *et al.*, 2009, p. 206): sistemas de medida de desempenho "auxiliam os gerentes a rastrear as implementações de estratégia de negócios comparando os resultados reais com metas estratégicas e objetivos [...] geralmente engloba métodos sistemáticos de união de metas de negócios com relatórios de retorno periódicos que indicam progresso contra metas."

**3 etapas para criar um sistema de medida de desempenho:**
1. **Definição e detalhamento de indicadores** — etapa mais importante; define quais indicadores serão monitorados.
2. **Implementação de um sistema de informação** — envolve 3 níveis:
   - *Interface do usuário* (navegador, planilhas, ERP)
   - *Tecnologias capacitadoras* (ex.: *dashboards* de BI)
   - *Bancos de dados* (estruturados ou repositórios de planilhas)
3. **Uso e revisão do sistema** — melhorias e adequações contínuas à realidade da empresa.

#### 3.4 Metodologias de BPM

##### Balanced Scorecard (BSC)

Modelo de sistema de gestão baseado em um *cockpit* de indicadores que orienta a condução da empresa a partir de múltiplas perspectivas.

**2 premissas básicas:**
1. Indicadores financeiros isoladamente não explicam sucesso/fracasso.
2. Gestores precisam de informação em tempo adequado.

**4 perspectivas do BSC** (Figura 3, Turban et al., 2009, p. 211):

| Perspectiva | Pergunta-chave |
|---|---|
| **Financeira** | Para ter sucesso financeiro, como deveríamos aparecer para nossos acionistas? |
| **Cliente** | Para alcançar nossa visão, como deveríamos aparecer para nossos clientes? |
| **Processos internos de negócios** | Para satisfazer acionistas e clientes, em que processos devemos nos superar? |
| **Aprendizado e crescimento** | Para alcançar nossa visão, como sustentamos nossa capacidade de mudar e melhorar? |

Todas as 4 perspectivas giram em torno do centro: **visão e estratégia** da empresa. Cada perspectiva usa uma matriz com 4 colunas: **Objetivos, Medidas, Metas, Iniciativas**.

**Exemplo do capítulo:**
- Objetivo: aumentar as vendas.
- Medidas: comparação matemática das vendas com o mesmo período do ano anterior.
- Meta: ser a empresa que mais vende no segmento X no ano 2022.
- Iniciativas: aumentar divulgação da marca; vender produtos da marca Y.

O ponto focal do BSC é o **equilíbrio**: financeiro x não financeiro, interno x externo, quantitativo x qualitativo, curto x longo prazo.

##### Six Sigma

Estratégia de gestão **quantitativa** (usa estatística) e **estruturada** (metodologia específica), focada na melhoria de processos já existentes.

**3 objetivos principais:**
1. Redução de custos.
2. Otimização de produtos e processos.
3. Incentivo à satisfação do cliente.

Fornece meios para medir/monitorar processos-chave ligados à lucratividade e acelerar melhoria de desempenho (TURBAN *et al.*, 2019). Foco principal: satisfação do cliente via redução de defeitos.

**Duas metodologias, cada uma com 5 fases (Periard, 2012):**

**DMADV** (para *novos* processos/produtos):
1. *Define goals* — definir objetivos alinhados a cliente e gestão.
2. *Measure and identify* — mensurar características críticas para a qualidade.
3. *Analyze* — desenvolver e projetar alternativas.
4. *Design details* — projetar detalhes e otimizar (fase mais longa, exige muitos testes).
5. *Verify the design* — executar pilotos, implementar produção, entregar ao proprietário do processo.

**DMAIC** (para *melhorar* processos existentes):
1. *Define the problem* — a partir de opiniões de clientes e objetivos da empresa.
2. *Measure key aspects* — aspectos principais do projeto atual.
3. *Analyze the data* — relação causa e efeito.
4. *Improve the process* — melhorar/otimizar com base na análise.
5. *Control* — assegurar correção de desvios futuros.

**BSC x Six Sigma:** a escolha depende da afinidade da equipe e do foco desejado. Six Sigma foca em resultados/cliente e exige base organizacional sólida; BSC identifica oportunidades de melhoria alinhadas aos objetivos estratégicos (VASQUES, 2019).

---

### 4. Exemplos, Aplicações e Material Prático

- **Exemplo de matriz BSC** (perspectiva financeira): Objetivo "aumentar vendas" → Medida "comparação com mesmo período do ano anterior" → Meta "ser líder no segmento X em 2022" → Iniciativas "aumentar divulgação da marca, vender produtos da marca Y".
- **Aplicação de Six Sigma citada no capítulo:** monitoramento de gastos com luz, diárias de viagem, telefone etc.
- Links complementares citados no capítulo (não verificados nesta sessão): vídeo sobre BSC e vídeo sobre Six Sigma (Canal Instituto Montanari; Canal Grupo Voitto).

---

### 5. Minhas Observações e Dúvidas

*(Espaço reservado — nenhuma observação registrada até o momento para esta aula.)*

---

### 6. Referências e Conexões com Outros Conteúdos

#### Referência principal
ZANIN, Aline. **Introdução à Inteligência de Negócios** — capítulo "Business performance management (BPM)". SAGAH.

#### Referências citadas no capítulo
- CHICALESKI, P. M. D. *O que é business performance management?* 2008.
- LAWRENCE, C. *Qual a diferença entre métrica, medida e indicador?* 2019.
- PERIARD, G. *Seis sigma: o que é e como funciona.* 2012.
- SIMONS, R. *Performance measurement and control systems for implementing strategy.* Upper Saddle River, NJ: Prentice Hall, 2002.
- TURBAN, E. *et al. Business intelligence: um enfoque gerencial para a inteligência do negócio.* Porto Alegre: Bookman, 2009.
- VASQUES, R. C. *Balanced Scorecard (BSC), CMMI e Six Sigma, como construir altos níveis de maturidade e desempenho.*

#### Conexões com outras disciplinas/aulas
- **Aula 1 (Aprendizado de Máquina):** troca de eixo — de um conteúdo técnico/algorítmico (ML) para um conteúdo de gestão/BI. O BPM é o tipo de contexto de negócio que consome os resultados de modelos de AM (ex.: um indicador do BSC pode ser alimentado por uma predição de ML).
- **Aquisição e Preparação de Dados:** o conceito de "dados integrados" no centro do ciclo do BPM dialoga com o ETL já estudado (extração/integração de dados de múltiplas fontes para consolidar indicadores).

---

## AULA 3 — CLASSIFICAÇÃO DE TEXTOS: INTRODUÇÃO AO APRENDIZADO SUPERVISIONADO


---

### 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Supervisionado (262GGR4728A)
**Aula:** 3 — Classificação de textos — introdução ao aprendizado supervisionado
**Fonte:** *Processamento de Linguagem Natural* — Michel Bernardo Fernandes da Silva, SAGAH (Soluções Educacionais Integradas), capítulo "Classificação de textos — introdução ao aprendizado supervisionado"

#### Objetivos de aprendizagem (conforme o capítulo)
- Definir a área de *machine learning*.
- Descrever exemplos de aplicações de *machine learning* para classificação de textos.
- Identificar os elementos que compõem as soluções de classificação de textos.

---

### 2. Resumo e Contextualização

O capítulo apresenta o *machine learning* (aprendizado de máquina) e seus tipos, mostra aplicações na **classificação de textos** (empresas comerciais, governo, Direito, Ciências Sociais, Medicina) e detalha os **elementos e etapas** de uma solução de classificação de textos (o *pipeline*).

Definições-base usadas no capítulo:
- **SAS Institute (2019):** aprendizado de máquina é "um método de análise de dados que possibilita criar modelos analíticos automaticamente".
- **Russell e Norvig (2013, p. 5):** a Inteligência Artificial é o estudo de agentes que recebem percepções do ambiente e executam ações; o *machine learning* é uma vertente específica da IA que treina máquinas para aprender com dados.

Premissa central: sistemas podem **aprender com dados, identificar padrões e tomar decisões com mínima interferência humana**.

Segundo Russell e Norvig (2013), o projeto de um elemento de aprendizagem é influenciado por três questões:
1. os componentes do elemento de desempenho que devem ser aprendidos;
2. a representação a ser utilizada para os componentes;
3. a realimentação (*feedback*) disponibilizada para aprender esses componentes.

**Posição na disciplina:** a Aula 1 apresentou o AM de forma geral; a Aula 3 aprofunda o lado **supervisionado** aplicado a **texto** (PLN), conectando os tipos de aprendizado, o vocabulário de dados (atributo, instância, rótulo, dataset) e o pipeline de uma solução real.

---

### 3. Conceitos Fundamentais e Explicações

#### 3.1 Classificações de aprendizado de máquina

A classificação mais frequente divide o AM em **supervisionado, não supervisionado e por reforço**.

| | **Aprendizado supervisionado** | **Aprendizado não supervisionado** | **Aprendizado por reforço** |
|---|---|---|---|
| **O que é** | Existe um conjunto pré-definido de **pares entrada/saída**; as entradas são atributos dos objetos a reconhecer. O treinamento usa esses dados e o programa precisa tomar decisões precisas quando recebe novos dados. | O programa busca **padrões e relações** em um conjunto de dados, recebendo **somente os dados de entrada**; os padrões de saída são aprendidos pelo próprio sistema. | O agente de aprendizagem adquire conhecimento sobre seu processo a partir do **reforço ou da recompensa**; também contempla o subproblema de entender como o ambiente funciona. |
| **Quando utilizar** † | Quando há dados **já rotulados** e o objetivo é prever o rótulo (ou valor) de novos dados. | Quando **não há rótulos prévios** e o objetivo é descobrir estrutura nos dados (ex.: agrupar por semelhança). | Quando um agente **interage com um ambiente** e aprende a partir de recompensas/penalidades, e não de exemplos rotulados. |
| **Exemplos** | Posts do Facebook ou tweets marcados como positivos, neutros e negativos para criar um classificador de **análise de sentimento**. Técnicas: redes neurais artificiais com treinamento supervisionado, árvores de decisão. | **Agrupamento automático de e-mails** recebidos por um funcionário, por temas semelhantes, sem conhecimento prévio sobre os dados de entrada. | Uma **multa de trânsito** indica ao agente que seu comportamento foi inadequado. |

> † **Linha "Quando utilizar":** o capítulo **não traz um critério explícito** de "quando utilizar" cada tipo. O conteúdo dessa linha foi **derivado das definições do próprio capítulo** (presença/ausência de rótulos, presença de recompensa). Tratar como síntese de estudo, não como citação do livro.

**Observação do capítulo:** em geral, um sistema de aprendizado dispõe de um conjunto de dados de treinamento **classificados manualmente**, com base nos quais aprende a classificar esses dados e **novos dados ainda não observados** (característica do supervisionado).

#### 3.2 Técnicas citadas

- **Supervisionado:** redes neurais artificiais com treinamento supervisionado; árvores de decisão (*decision tree*).
- **Aprendizagem profunda (*deep learning*):** categoria de algoritmos de ML que usa **redes neurais artificiais** para gerar modelos; bem-sucedida em reconhecimento de imagem; as redes são inspiradas nas redes neurais biológicas (rede de nós interconectados) e usadas, em geral, quando o volume de entrada é muito grande, o que torna abordagens convencionais inadequadas.

#### 3.3 Árvore de decisão

- Chega à decisão por meio de uma **sequência de testes**.
- **Nó interno** = teste do valor de um atributo de entrada *Aᵢ*.
- **Ramificações** = valores possíveis do atributo (*Aᵢ = vᵢₖ*).
- **Nó folha** = valor retornado pela função.
- Os exemplos são processados a partir da **raiz**, seguindo a ramificação apropriada até alcançar uma folha.

#### 3.4 Terminologia de dados (Baranauskas e Monard, 2000, e demais autores do capítulo)

| Termo | Definição no capítulo |
|---|---|
| ***Inducer*** (programa de aprendizagem) | Tem como objetivo gerar um bom **classificador** para um conjunto de instâncias já classificadas; o classificador é usado para prever o rótulo de instâncias não rotuladas. |
| **Atributo / *feature*** | Descrição ou característica de um aspecto da instância. Atributos podem ser **nominais** (ex.: cor, país de nascimento) ou **contínuos** (ex.: altura, peso — números reais). *Features* são usadas como **preditores** ou **variáveis independentes**, correspondendo às **colunas** da base. |
| **Instância** | Lista fixa de valores de atributos; descreve a entidade tratada (ex.: dados médicos sobre uma doença). |
| **Classe / rótulo** | Característica especial do aprendizado supervisionado que descreve o fenômeno de interesse, a tarefa de aprendizado e a realização de predições com base nele. |
| ***Dataset*** | Coleção de instâncias **classificadas (rotuladas)**. Os rótulos podem ser um conjunto **discreto** de classes (**classificação**) ou **valores reais** (**regressão**). |

Dado um conjunto de instâncias de treino, o programa gera um classificador que, para uma nova instância, poderá prever com precisão o rótulo dela.

#### 3.5 Aplicações de ML para classificação de textos

Contexto: as primeiras técnicas de classificação de texto foram usadas majoritariamente em **sistemas de recuperação da informação**. Hoje há aplicações em Medicina, Ciências Sociais, Psicologia, Engenharia e Direito. A maioria das tarefas de **PLN** com ML é tratada como **problema de classificação** (associar uma etiqueta a cada palavra do texto), com aprendizado induzido por um ***corpus* de treino** com exemplos corretamente classificados. O conhecimento adquirido é representado por **probabilidades contextuais** ou **regras de transformação**.

| Aplicação | Descrição no capítulo |
|---|---|
| **Recuperação de informações** | Localizar dados em documentos não estruturados que atendem a uma necessidade de informação; baseia-se em criar estruturas de índices. Ex.: Google (consulta e tradução entre idiomas). |
| ***Chatbots*** | Robôs de atendimento em *chats* de sites/mídias sociais; precisam ser carregados de **intenções** e integrados a bases de dados; o contexto de operação faz parte da etapa de treino. Um chatbot baseado em PLN interpreta a mensagem e não segue um fluxo-padrão fixo. |
| **Filtragem de informações** | Seleção da informação relevante e retirada da irrelevante. Ex.: identificar *spam*; detector de ***fake news*** (usa características de escrita, como palavras e classes gramaticais mais frequentes; o texto deve ter pelo menos 100 palavras, pois o sistema foi treinado para isso). |
| **Análise de sentimentos (mineração de opiniões)** | Identifica o conteúdo de opinião e determina sentimento/atitude/percepção sobre produto, serviço, marca ou assunto; normalmente polarizada em **positivo, negativo e neutro**. |
| **Sistemas de recomendação** | Sugerem itens com base no perfil de interesse do usuário e na descrição do item (ex.: *streaming*: o que assistimos, notas dadas, o que pessoas com mesmos interesses assistiram, informações do filme, horário, plataforma). |
| **Sumarização de documentos** | Resume documentos, podendo empregar palavras e frases inexistentes no original (ex.: determinar o assunto de um e-mail). |
| **Marketing e mídias sociais** | Empresas usam mineração de opiniões (Facebook, Twitter, Reclame Aqui) para aumentar vendas e lucros; há ferramentas de monitoramento em tempo real, também aplicáveis em instâncias governamentais. |
| **Ciências sociais** | Entender comportamento humano por mineração da linguagem (notas informais, SMS, WhatsApp, mídias sociais); foco na **frequência de palavras** ou em características do dicionário ***linguistic inquiry word count* (LIWC)**. |
| **Saúde** | Informação médica é em geral desestruturada, com termos ambíguos e erros; aplicações: codificação da **CID** (Classificação Internacional de Doenças), desenvolvimento do ***MeSH*** (*Medical Subject Headings*, da National Library of Medicine) e **ontologia genética** (*gene ontology*, GO). |

#### 3.6 Elementos da solução: o *pipeline* de classificação de texto

Segundo Kowsari *et al.* (2019), a maioria dos sistemas de classificação de texto se decompõe em **quatro fases**:

1. **Extração de recursos** (*features*)
2. **Redução de dimensão** (etapa **opcional** do pipeline)
3. **Seleção do classificador**
4. **Avaliação**

```
Texto bruto → Extração de features → [Redução dimensional] → Classificação (modelo de aprendizado) → Avaliação
                                       (opcional)                                                  • predição da base de teste
                                                                                                   • avaliação do modelo
```
*(Figura 3 do capítulo, adaptada de Kowsari et al., 2019)*

- **Entrada:** conjunto de texto bruto, na forma D = {X₁, X₂, ..., X_N}, onde cada Xᵢ é um documento ou segmento de texto com *s* sentenças, cada sentença com palavras *w_s* de letras *l_w*. Cada ponto é rotulado com um valor de classe de um conjunto de *k* valores discretos.
- **Extração de recursos:** converte texto **desestruturado** em um **espaço de características estruturadas**, necessário para a modelagem matemática do classificador. Antes, os dados passam por tratamento para omitir caracteres e palavras desnecessários.
- **Redução de dimensão:** justificada porque conjuntos de textos têm muitas palavras únicas, o que pode tornar o pré-processamento lento e custoso em memória.
- **Seleção do classificador:** "o passo mais significativo na categorização" — exige compreensão conceitual de cada algoritmo. Citados: **Naive Bayes, Rocchio, *Ensemble* do tipo *Bagging*, *Boosting*, regressão logística**.
- **Avaliação:** divide-se em **previsão do conjunto de teste** e **avaliação do modelo**; é fundamental entender o desempenho do modelo.

**Níveis de escopo** da classificação de texto:
- **Documento** — categorias relevantes para o documento completo;
- **Parágrafo** — para um único parágrafo ou parte do documento;
- **Sentença** — categorias de sentenças únicas ou parte de um parágrafo;
- **Frase** — categorias de frases dentro de uma sentença.

#### 3.7 Superfície de decisão e algoritmos

- **Hiperplano de separação:** forma clássica de gerar uma superfície de decisão; pode ser perpendicular ou não ao eixo (Figura 4: (a) hiperplano perpendicular, (b) não perpendicular).
- **KNN (*K-Nearest Neighbors*, k-ésimo vizinho mais próximo):** usado quando as classes **não** podem ser separadas por forma geométrica. Define-se um número *k* de vizinhos; o novo exemplo recebe a **classe mais presente entre os *k* vizinhos mais próximos** (Figura 5: três classes, cinco vizinhos).
- **Naive Bayes:** classificador **probabilístico** muito usado em ML, baseado no teorema de Bayes (Thomas Bayes, 1702–1761); segundo o capítulo, "desconsidera a correlação entre as variáveis".

#### 3.8 Expressões regulares (conceito citado antes do pré-processamento)

No capítulo, as **expressões regulares (RE)** aparecem como "um conceito importante nesse contexto", **antes** do subtítulo "Pré-processamento e limpeza do texto". O texto **não as apresenta como uma etapa do pré-processamento**.

- Notação padronizada para caracterizar cadeias de caracteres (*strings*), aplicável a qualquer sequência de caracteres alfanuméricos (letras, números, espaços, pontuações, tabulações). O espaço é um caractere como os demais.
- Uma expressão regular de pesquisa precisa de um **padrão** a pesquisar e de um ***corpus*** (conjunto de textos escritos e registros orais de uma língua, usado como base de pesquisa e análise).
- Um **autômato de estados finitos** é a estrutura matemática usada para implementar expressões regulares, uma das ferramentas mais significativas da linguística computacional.

#### 3.9 Pré-processamento e limpeza do texto

Motivo: conjuntos de dados contêm palavras desnecessárias, erros ortográficos e gírias; em algoritmos estatísticos/probabilísticos, ruído e características desnecessárias prejudicam o desempenho (Jurafsky e Martin, [2020]).

| Técnica | Descrição |
|---|---|
| **Tokenização** | Quebra fluxos de texto em palavras, frases, símbolos ou outros elementos significativos chamados ***tokens***. |
| **Remoção de *stopwords*** | Remove palavras sem informação relevante para classificação (ex.: "um/uma", "sobre", "acima", "através", "depois", "novamente", "para"). |
| **Remoção de pontuação e caracteres especiais** | Importantes para a compreensão humana, mas podem atrapalhar o algoritmo. |
| **Padronização de maiúsculas/minúsculas** | Transformar tudo em minúsculas é abordagem comum, mas pode gerar problemas: o pronome "ti" e a sigla "TI" (Tecnologia de Informação) passam a ter a mesma representação. |
| **Correção de erros de digitação (*typos*)** | Etapa **opcional**; comum em textos de mídias sociais (Twitter, Facebook). |

---

### 4. Exemplos, Aplicações e Material Prático

#### 4.1 Árvore de decisão — esperar ou não por uma mesa (Figura 1; Russell e Norvig, 2013, p. 812)
Objetivo: aprender uma função para o predicado **VaiEsperar**. Exemplo do capítulo: uma situação com *Clientes = Cheio* e *EsperaEstimada = 0-10* é classificada como **positiva** (esperaremos por uma mesa). Atributos usados na árvore: Clientes, EsperaEstimada, Alternativa, Reserva, Sex/Sáb, Bar, Faminto, Chovendo.

#### 4.2 Tokenização
Frase: *"Depois de ir ao parque, ela decidiu fazer compras no mercado."*
*Tokens:* {"Depois" "de" "ir" "ao" "parque" "ela" "decidiu" "fazer" "compras" "no" "mercado"}

#### 4.3 Processamento básico de um texto (Figura 6; adaptada de Travizan Neto, 2017)
`"O carro."` → (remoção de *stopwords*) → `" carro."` → (remoção de pontuação) → `" carro"`

#### 4.4 Análise de sentimento aplicada a programas do Governo Federal (Figura 2; Oliveira *et al.*, 2019, p. 245–246)
Foram avaliados *tweets* sobre Bolsa Família, Minha Casa Minha Vida, Mais Médicos e Pronatec. Categorias de polaridade: positivo, negativo, neutro e **falso-positivo** (tweet irônico que parece positivo, mas não é).

| Programa | Positivo | Neutro | Negativo |
|---|---|---|---|
| Pronatec | 69% | 16% | 15% |
| Minha Casa, Minha Vida | 49% | 12% | 39% |
| Mais Médicos | 41% | 5% | 54% |
| Bolsa Família | 35% | 7% | 58% |

#### 4.5 Exemplo histórico (quadro "Saiba mais")
Nos primeiros sistemas de tradução automática (década de 1950, russo→inglês), a frase *"The spirit is willing, but the flesh is weak"* voltou como *"The vodka is good, but the meat is rotten"* — ilustra as limitações iniciais da tradução automática. (Um projeto da CIA investiu milhões de dólares em um software de tradução russo→inglês.)

**Material prático em código:** o capítulo não apresenta código. Não foi criado arquivo prático complementar para esta aula.

---

### 5. Minhas Observações e Dúvidas

*(Espaço reservado — nenhuma observação registrada até o momento para esta aula.)*

#### Pontos de atenção no texto-base (identificados na análise; não são observações da aluna)
1. **Referência de figura possivelmente trocada:** o texto diz que cada ponto é rotulado com um valor de classe de *k* valores discretos "(Figura 4)", mas a Figura 4 mostra **superfícies de decisão (hiperplanos)**, não a estrutura de rótulos.
2. **Posição de uma frase:** "um sistema de aprendizado dispõe de um conjunto de dados de treinamento classificados manualmente..." aparece logo após o parágrafo do **não supervisionado**, mas descreve o **supervisionado**. Pode confundir na leitura.
3. **Fases x figura:** o texto lista **quatro fases** (incluindo redução de dimensão), mas também diz que a redução é **opcional**; a Figura 3 mostra a redução tracejada (opcional). Não é contradição, mas vale reter que o pipeline mínimo é extração → classificação → avaliação.
4. **Tipos de aprendizado:** este capítulo apresenta **três** tipos (supervisionado, não supervisionado, por reforço) e **não menciona o semissupervisionado**, que aparece no capítulo da Aula 1.
5. **Complementação (fora do capítulo):** a frase de que o Naive Bayes "desconsidera a correlação entre as variáveis" é uma simplificação; tecnicamente, ele **assume independência condicional entre as *features*** dada a classe. Registrar como nota de estudo, sem atribuir ao autor do capítulo.

---

### 6. Referências e Conexões com Outros Conteúdos

#### Referência principal
SILVA, Michel Bernardo Fernandes da. **Processamento de Linguagem Natural** — capítulo "Classificação de textos — introdução ao aprendizado supervisionado". SAGAH.

#### Referências citadas no capítulo
- BARANAUSKAS, J. A.; MONARD, M. C. *Reviewing some Machine Learning Concepts and Methods.* São Carlos: ICMC-USP, 2000. (Relatórios Técnicos do ICMC-USP, 102).
- JURAFSKY, D. S.; MARTIN, J. H. *Speech and language processing.* 3. ed. Upper Saddle River: Prentice Hall, [2020].
- KOWSARI, K. *et al.* Text Classification Algorithms: A Survey. *Information*, v. 10, n. 150, p. 1–68, 2019.
- OLIVEIRA, D. J. S. *et al.* A aplicação da técnica de análise de sentimento em mídias sociais como instrumento para as práticas da gestão social em nível governamental. *Revista de Administração Pública*, v. 53, n. 1, p. 235–251, 2019.
- RODRIGUES, N. *Ebook: Guia sobre Chatbots – Seu negócio ainda vai ter um.* Cedro Technologies, 2017.
- RUSSELL, S.; NORVIG, P. *Inteligência artificial.* 3. ed. Rio de Janeiro: Elsevier, 2013.
- SAS INSTITUTE. *Machine Learning: O que é e qual sua importância.* 2019.
- TRAVIZAN NETO, A. *Classificação de traços de personalidade através de Linguagem Natural aplicada a ambientes virtuais de aprendizagem.* TCC, UFU, 2017.

#### Conexões com outras aulas e disciplinas
- **Aula 1 (Aprendizado de Máquina):** retoma supervisionado/não supervisionado/reforço; **classificação** (rótulos discretos) e **regressão** (valores reais) aparecem nas duas aulas; KNN, Naive Bayes, árvores de decisão, regressão logística e redes neurais já haviam sido listados no Quadro 2 da Aula 1.
- **Atividade 1 (Mineração de Dados):** o capítulo usa "mineração de opiniões" e "mineração de textos" como aplicações do ML, o que dialoga com a distinção ML x mineração de dados discutida na atividade.
- **Atividade A2 / Aula de pré-processamento:** ruído, redução dimensional e limpeza de dados reaparecem aqui no contexto de texto (*stopwords*, pontuação, *typos*, redução de dimensão opcional).
- **Aquisição e Preparação de Dados:** tokenização, remoção de ruído e padronização são a versão textual da limpeza/transformação vistas em ETL e AED.
- **Aprendizado Não Supervisionado:** o exemplo de agrupamento automático de e-mails conecta diretamente com essa disciplina.

---

## AULA 4 — CLASSIFICAÇÃO DE TEXTOS: UTILIZANDO PYTHON PARA CONSTRUIR E TREINAR MODELOS DE MACHINE LEARNING


---

### 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Supervisionado (262GGR4728A)
**Aula:** 4 — Classificação de textos — Utilizando Python para construir e treinar modelos de machine learning
**Fonte:** *Processamento de Linguagem Natural* — Juliano Vieira Martins, SAGAH (Soluções Educacionais Integradas)

#### Objetivos de aprendizagem (conforme o capítulo)
- Descrever processos de manipulação de dados para utilizar classificadores de texto.
- Analisar o classificador Naïve Bayes.
- Aplicar o classificador Naïve Bayes em um estudo prático.

**Observação de continuidade:** esta aula é a continuação direta da Aula 3 (mesmo livro, autor diferente — Michel Bernardo Fernandes da Silva na Aula 3, Juliano Vieira Martins nesta). A Aula 3 tratou os conceitos de PLN, classificação e pré-processamento (tokenização, stopwords, pontuação) em nível teórico; esta aula aplica tudo isso em **código Python real**, do zero até um classificador funcionando.

---

### 2. Resumo e Contextualização

A classificação de texto é definida como o processo de **atribuir rótulos/etiquetas de categorias ao texto** de acordo com seu conteúdo — uma das tarefas fundamentais do PLN, com aplicações em análise de sentimentos, rotulagem de tópicos, detecção de spam, de intenção e de idioma. Exemplos de contexto: textos curtos (tweets, chamadas de notícias, SMS) e textos longos (análises de clientes, artigos de mídia, contratos legais).

Motivação de negócio: dados em texto (e-mails, chats, páginas web, mídias sociais, tickets de suporte, pesquisas) são abundantes e potencialmente valiosos, mas difíceis de explorar por serem **não estruturados**. A classificação de texto estrutura esses dados de forma rápida e econômica, visando melhorar a tomada de decisão e automatizar processos.

O capítulo segue três grandes blocos:
1. **Obtenção e preparação dos dados**
2. **Análise do classificador Naïve Bayes** (teoria/matemática)
3. **Aplicação do classificador em um estudo prático** (código completo, com o dataset SMS Spam Collection)

---

### 3. Conceitos Fundamentais e Explicações

#### 3.1 Obtenção dos dados

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

#### 3.2 Ferramentas utilizadas

- **Google Colab (Colaboratory):** ambiente Jupyter Notebook gratuito, sem configuração, executado na nuvem; requer conta Gmail. Permite escrever/executar código, salvar/compartilhar análises e usar recursos de computação pelo navegador.
- **UC Irvine Machine Learning Repository (UCI):** repositório mantido pela UCI com mais de 490 conjuntos de dados (DUA; GRAFF, 2019); fonte do **SMS Spam Collection Data Set** usado no exemplo prático.

#### 3.3 Exploração dos dados

Usa-se a biblioteca **Pandas**: o `DataFrame` é uma estrutura tabular, bidimensional, mutável em tamanho, podendo ser heterogênea, com eixos rotulados (linhas e colunas) — composto por **dados, linhas e colunas**.

No dataset SMS Spam Collection: **5.572 registros** (IDs de 0 a 5.571); coluna 0 = rótulo da classe, coluna 1 = mensagem. Distribuição das classes: **4.825 "ham"** (não-spam) e **747 "spam"**.

#### 3.4 Preparação dos dados (pré-processamento)

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

#### 3.5 Extração de recursos (*features*) e vetorização

Para treinar o classificador, o texto precisa virar uma **representação numérica (vetor)**:

1. Criar um conjunto de todas as palavras do texto e contar a **frequência** de cada uma.
2. Selecionar as palavras **mais frequentes** (no exemplo: as **1.500 mais frequentes**) para formar o **vetor-modelo de features**.
3. Para cada mensagem, gerar um vetor de *features* (dicionário `{palavra: True/False}` indicando se a palavra aparece ou não na mensagem).
4. Associar cada vetor de *features* ao seu rótulo (0 = ham, 1 = spam), formando tuplas (*features*, rótulo).

**Observação importante do capítulo:** "quantidade não significa qualidade" — é preciso cuidado com quais palavras entram no vetor-modelo, pois o classificador considera até palavras que aparecem **uma única vez** em todo o texto.

**Conversão de rótulos:** usa-se `LabelEncoder` (do `sklearn.preprocessing`) para converter rótulos categóricos (ham/spam) em valores binários (0/1).

**Embaralhamento (shuffle):** as mensagens são embaralhadas (com `seed` fixa para reprodutibilidade) para que a **ordem não interfira** no treinamento.

#### 3.6 O classificador Naïve Bayes — teoria

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

#### 3.7 Exemplo matemático do capítulo (Quadros 1 e 2)

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

#### 3.8 Treinamento e teste do modelo (metodologia)

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

#### 3.9 Avaliação do modelo

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

#### 3.10 Ajuste de hiperparâmetros

Classificadores em geral têm vários parâmetros ajustáveis (*hiperparâmetros*). Testar manualmente todas as combinações é inviável (exemplo do capítulo: 2 parâmetros, um com 100 valores possíveis e outro booleano → **200 combinações**).

**Duas técnicas de busca:**

| Técnica | Como funciona | Quando usar |
|---|---|---|
| ***Grid Search*** | Testa **exaustivamente** todas as combinações possíveis | Dataset relativamente pequeno, muitos parâmetros a ajustar → resultados mais precisos |
| ***Random Search*** | Testa combinações **aleatórias** dos valores | Datasets grandes e muitas dimensões de ajuste → custo computacional do Grid Search fica muito alto |

Ferramenta: `GridSearchCV` (de `sklearn.model_selection`), que otimiza por **validação cruzada**.

#### 3.11 Naïve Bayes: prós e contras (síntese do capítulo)

**A favor:**
- Bom desempenho na predição da classe correta, mesmo sendo "ingênuo".
- Funciona bem em situações reais (classificação de documentos, filtragem de spam).
- Rápido na execução; tem bom desempenho mesmo com poucos dados.
- Relativamente simples de configurar para aplicações rotineiras.

**Contra:**
- A suposição de independência entre *features* limita a exploração de interações reais entre os dados (ainda que, na prática, isso não costume prejudicar tarefas de classificação de texto).
- Se uma variável do conjunto de teste **nunca foi vista** no treino, o modelo atribui probabilidade **0** e não consegue prever com precisão (o próprio Laplace Smoothing, aplicado no treino, mitiga esse problema).

---

### 4. Exemplos, Aplicações e Material Prático

O código completo deste capítulo (obtenção dos dados, regex, NLTK, vetorização, treinamento, avaliação e ajuste de hiperparâmetros) foi organizado em arquivo complementar, pronto para compilação em Jupyter Notebook:

➡️ **`AULA_04_CLASSIFICACAO_TEXTO_PYTHON_PRATICO.md`**

---

### 5. Minhas Observações e Dúvidas

*(Espaço reservado — nenhuma observação registrada até o momento para esta aula.)*

#### Pontos de atenção no texto-base (identificados na análise; não são observações da aluna)
1. **Pequena inconsistência de nomenclatura no Quadro 2:** a tabela traz "P(palavra|não-spam)" na coluna, mas o texto corrido logo acima usa "não_spam" (com *underscore*). Mesmo conceito, grafias diferentes dentro do próprio capítulo.
2. **Trecho de código com erro tipográfico evidente (OCR/editoração do livro):** nas variáveis Python, o PDF mostra espaços estranhos dentro de identificadores (ex.: `pd.read _ ta ble`, `word _ tokens`, `train _ test _ split`). Isso é um artefato de formatação do PDF original (não um erro do leitor) — no arquivo prático, os nomes foram corrigidos para a sintaxe Python real (`read_table`, `word_tokens`, `train_test_split`), já que o código como está no PDF não executaria.
3. **MultinomialNB em dados booleanos:** o capítulo monta as *features* como `True`/`False` (palavra presente ou não) e depois diz que a distribuição multinomial "normalmente requer contagens de recursos inteiros". Isso é uma inconsistência técnica do capítulo: o ideal para dados binários (presença/ausência) seria o `BernoulliNB`, não o `MultinomialNB` — mas o `DictVectorizer`, ao vetorizar dicionários com `True`/`False`, converte esses valores para `1.0`/`0.0`, o que faz o `MultinomialNB` funcionar ainda que não seja a escolha teoricamente mais alinhada ao tipo de dado.

---

### 6. Referências e Conexões com Outros Conteúdos

#### Referência principal
MARTINS, Juliano Vieira. **Processamento de Linguagem Natural** — capítulo "Classificação de textos — Utilizando Python para construir e treinar modelos de machine learning". SAGAH.

#### Referências citadas no capítulo
- DUA, D.; GRAFF, C. *UCI Machine Learning Repository.* Irvine, CA: University of California, 2019.
- GOOGLE COLABORATORY. Mountain View, CA: Google, c2020.
- JURAFSKY, D. S.; MARTIN, H. *Speech and language processing: an introduction to natural language processing, computational linguistics, and speech recognition.* 3. ed. New Jersey: Prentice Hall, 2019.
- NATURAL LANGUAGE TOOLKIT. *NLTK 3.5 documentation.* 2020.
- NUMPY. c2020.
- PANDAS. *Python Data Analysis Library.* Texas: Zenodo, 2020.
- PYTHON. Wilmington: Python Software Foundation, c2020.
- SCIKIT-LEARN: *Machine learning in Python.* c2020.

#### Conexões com outras aulas e disciplinas
- **Aula 3 (Classificação de textos — introdução ao aprendizado supervisionado):** esta aula é a aplicação prática direta da teoria vista lá — tokenização, remoção de stopwords e pontuação (Aula 3, seção de pré-processamento) reaparecem aqui como código real com NLTK e regex; o Naïve Bayes citado na Aula 3 (como um dos algoritmos do pipeline) é aprofundado matematicamente aqui.
- **Aula 1 (Aprendizado de Máquina):** Naïve Bayes já constava no Quadro 2 da Aula 1 como algoritmo de classificação supervisionada; esta aula mostra sua base probabilística (teorema de Bayes) e sua implementação.
- **Atividade 1 (Mineração de Dados) / Aquisição e Preparação de Dados:** o pré-processamento com regex, stopwords e normalização dialoga diretamente com os conceitos de limpeza e transformação de dados já estudados (ETL, AED).
- **Overfitting e divisão treino/teste:** conceito novo nesta aula, mas que se conecta à discussão de qualidade de dados e generalização de modelos vista de forma mais geral na Aula 1.

---

## 4.1 Material Prático — Código Python Completo

> Código extraído e organizado a partir do capítulo "Classificação de textos — Utilizando Python para construir e treinar modelos de machine learning" (Juliano Vieira Martins, SAGAH). O PDF original apresenta espaços indevidos dentro de identificadores Python (ex.: `word _ tokens`), provavelmente um artefato de diagramação do livro — abaixo, o código foi normalizado para sintaxe Python válida (`word_tokens`), preservando integralmente a lógica e os comentários do capítulo. Organizado em células, pronto para colar em um Jupyter Notebook / Google Colab.

---

### Célula 0 — Verificar versão do Python (opcional)

```python
!python --version
```

---

### Célula 1 — Download do dataset (SMS Spam Collection, UCI)

```python
import requests  # Biblioteca HTTP
import zipfile   # Biblioteca de compressão de arquivos
import io        # Biblioteca para lidar com Entrada e saídas.

# URL do arquivo TSV
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'

# Download do arquivo TSV
r = requests.get(url)

# Instanciando o compressor ZipFile
z = zipfile.ZipFile(io.BytesIO(r.content))

# Extração (descompressão) dos dados
z.extractall()
```

O dataset baixado fica disponível em `/content/SMSSpamCollection` (ambiente Google Colab).

---

### Célula 2 — Explorar o dataset com Pandas

```python
import pandas as pd

# Carregar o dataset de mensagens para um DataFrame
df = pd.read_table('/content/SMSSpamCollection', header=None, encoding='utf-8')

# Imprimir informações úteis sobre o conjunto de dados (opcional)
print(df.info())

# Imprimir as 5 primeiras linhas do conjunto de dados (opcional)
print(df.head())

# Variável para as classes, para evitar ficar usando a notação df[0]
classes = df[0]

# Imprimir a distribuição das classes (opcional)
print(classes.value_counts())
```

**Resultado esperado (conforme o capítulo):** 5.572 registros, coluna 0 = rótulo, coluna 1 = mensagem; distribuição de 4.825 "ham" e 747 "spam".

---

### Célula 3 — Expressões regulares: identificar caracteres especiais (exemplo informativo)

```python
import re  # Biblioteca de expressões regulares

# Padrão de expressão regular para encontrar números e caracteres especiais
pattern = re.compile(r'[\d@_!#$%^&*()<>?/\|}{~:]')

# Selecionar a coluna de mensagens
text_messages = df[1]

# Selecionar as 10 primeiras linhas
messages = text_messages[0:10]

# Para cada linha na lista de mensagens
for line in messages:
    # Criar lista de palavras dividindo a frase pelos espaços em branco
    words = line.split(' ')
    # Para cada palavra na lista de palavras:
    for word in words:
        # Se algum caractere do padrão existir na palavra
        if re.search(pattern, word):
            # Imprime a palavra
            print(word)
```

> Este bloco é apenas informativo — nada é alterado no conjunto de dados aqui; serve para visualizar quais palavras contêm números, e-mails, telefones, URLs etc.

---

### Célula 4 — Limpeza do texto com regex (substituições definitivas)

```python
# Alterar todas as palavras para minúsculas
processed_lines = text_messages.str.lower()

# Lista de tuplas com os padrões e novas palavras
patterns = [
    # Substituir endereços de email por 'emailaddress'
    (r'^.+@[^\.].*\.[a-z]{2,}$', 'emailaddress'),
    # Substituir URLs por 'webaddress'
    (r'^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$', 'webaddress'),
    # Substituir símbolos monetários (Dólar e Euro) por 'moneysymb'
    (r'£|\$', 'moneysymb'),
    # Substituir números de telefone por 'phonenumbr'
    (r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$', 'phonenumbr'),
    # Substituir números por 'numbr'
    (r'\d+(\.\d+)?', 'numbr'),
    # Remover pontuação (! ?)
    (r'[^\w\d\s]', ' '),
    # Substituir dois ou mais espaços em branco por um único espaço
    (r'\s+', ' '),
    # Remover os espaços em branco à esquerda e à direita
    (r'^\s+|\s+?$', '')
]

# Substituir no texto os padrões encontrados
for pattern, newword in patterns:
    processed_lines = processed_lines.str.replace(pattern, newword)
```

**Por que essas palavras de substituição (`emailaddress`, `webaddress`...)?** Para não colidir com palavras que já existam naturalmente no texto — senão a frequência de uma palavra comum (ex.: "mail") seria inflada artificialmente.

---

### Célula 5 — Remoção de stopwords e stemming (NLTK)

```python
import nltk
nltk.download('stopwords')  # arquivo de suporte ao stopwords
nltk.download('punkt')      # arquivo de suporte à tokenização

from nltk.corpus import stopwords          # gerar lista de stopwords
from nltk.stem import PorterStemmer        # stemmizar palavras
from nltk.tokenize import word_tokenize    # tokenizar texto

# Criar uma lista das stop words
stop_words = stopwords.words('english')

# Inicializar uma instância de Porter Stemmer
ps = PorterStemmer()

# Para cada índice da lista
for i in range(len(processed_lines)):
    # Criar lista de palavras tokenizadas para cada linha
    word_tokens = word_tokenize(processed_lines[i])
    # Inicializar uma lista para receber as palavras filtradas
    filtered_sentence = []
    # Para cada palavra da lista de palavras tokenizadas:
    for word in word_tokens:
        # Se a palavra não está na lista de stop words
        if word not in stop_words:
            # Cria um stem para a palavra
            stemmed_word = ps.stem(word)
            # Adiciona na lista de palavras filtradas
            filtered_sentence.append(stemmed_word)
    # Junta as palavras da lista para substituir o texto antigo pelo novo texto processado
    processed_lines[i] = ' '.join(filtered_sentence)
```

---

### Célula 6 — Construção do vetor-modelo de features (palavras mais frequentes)

```python
# Inicializar uma lista de palavras
all_words = []

# Para cada linha da lista de linhas que foram processadas:
for line in processed_lines:
    # Criar lista de palavras tokenizadas para cada linha
    word_tokens = word_tokenize(line)
    # Para cada palavra da lista de palavras:
    for word in word_tokens:
        # Adiciona a palavra no "bag" onde estão todas as palavras
        all_words.append(word)

# Atribui a contagem de frequência para cada palavra da lista
all_words = nltk.FreqDist(all_words)

# Imprimir o número total de palavras existentes na lista (opcional)
print(f'Total de palavras: {len(all_words)}')

# Imprimir as 10 palavras mais comuns existentes na lista (opcional)
print(f'Palavras mais comuns: {all_words.most_common(10)}')

# Usar as 1500 palavras mais comuns como modelo de features
word_features = list(all_words.keys())[0:1500]

# Imprimir as 10 primeiras features (opcional)
print(f'Lista de características: {word_features[0:10]}')
```

> **Atenção (destacada no capítulo):** "quantidade não significa qualidade" — o classificador considera até palavras que aparecem uma única vez em todo o texto; o tamanho do vetor (1.500) é ajustável para melhorar o desempenho.

---

### Célula 7 — Vetorizar cada mensagem como vetor de features + rótulo binário

```python
import numpy as np
import sklearn
from sklearn.preprocessing import LabelEncoder

# Converter rótulos de classes para valores binários: 0 = ham e 1 = spam
encoder = LabelEncoder()
bin_labels = encoder.fit_transform(classes)

# Adicionar em uma lista de tuplas a mensagem e o rótulo da classe, na mesma posição
messages = list(zip(processed_lines, bin_labels))

# Definir um valor de seed para reprodutibilidade
seed = 1
np.random.seed = seed
# Embaralhar as mensagens para que a ordem não interfira no treinamento
np.random.shuffle(messages)

# Inicializar uma lista geral para os vetores de features e os respectivos rótulos
featuresets = []

# Para cada par texto e rótulo da lista de mensagens:
for text, label in messages:
    # Criar lista de palavras tokenizadas para cada linha
    word_tokens = word_tokenize(text)
    # Inicializar um dicionário (set de features)
    features = {}
    # Para cada palavra existente na lista de tokens-modelo
    for word in word_features:
        # Se a palavra existir no texto, atribui True; senão, False
        features[word] = (word in word_tokens)
    # Adiciona na lista geral como tupla (vetor de features, rótulo binarizado)
    featuresets.append((features, label))
```

---

### Célula 8 — Dividir em treino e teste

```python
from sklearn.model_selection import train_test_split

# Dividir os dados em dois conjuntos: 75% treinamento e 25% teste
training, testing = train_test_split(
    featuresets,       # dataset com as características e rótulos
    train_size=None,
    test_size=0.25,    # tamanho do conjunto de teste
    random_state=seed  # garante que as divisões geradas sejam reproduzíveis
)

# Imprimir número de instâncias no conjunto de treinamento (opcional)
print(len(training))

# Imprimir número de instâncias no conjunto de teste (opcional)
print(len(testing))

test_features, test_labels = zip(*testing)
train_features, train_labels = zip(*training)
```

**Parâmetros de `train_test_split`:**

| Parâmetro | Função |
|---|---|
| `*arrays` | Conjunto(s) de dados (listas, arrays numpy, matrizes scipy-sparse, DataFrame pandas) |
| `train_size` | `None` (padrão) / `int` (nº exato) / `float` (0,1 a 1,0) |
| `test_size` | Padrão 0,25 quando `train_size=None` |
| `random_state` | Fixa a semente para reprodutibilidade |

---

### Célula 9 — Vetorizar dicionários em matriz e treinar o Naïve Bayes

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer

# Instanciar o vetorizador de dicionários
vect = DictVectorizer(sparse=False)

# Vetorizar os dados de treinamento e teste
train_features = vect.fit_transform(train_features)
test_features = vect.fit_transform(test_features)

# Instanciar o modelo Naive Bayes
model = MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)

# Treinar o modelo com os dados de treinamento
model.fit(train_features, train_labels)

# Testar o modelo com os dados de teste
predicted = model.predict(test_features)
```

**Parâmetros de `MultinomialNB`:**

| Parâmetro | Função |
|---|---|
| `alpha` | (float, opcional, padrão=0) suavização Laplace/Lidstone (0 = sem suavização) |
| `fit_prior` | (bool) se deve aprender as probabilidades *a priori* das classes a partir dos dados |
| `class_prior` | (array) probabilidades *a priori* definidas manualmente |

---

### Célula 10 — Matriz de confusão e relatório de avaliação

```python
from sklearn.metrics import confusion_matrix

# Gera matriz de confusão a partir dos resultados preditos
confus_matrix = confusion_matrix(test_labels, predicted)

# Cria um DataFrame adicionando nomes de linhas e colunas
pd.DataFrame(
    confus_matrix,
    index=[['Real', 'Real'], ['spam', 'ham']],
    columns=[['Predito', 'Predito'], ['spam', 'ham']]
)
```

```python
from sklearn.metrics import classification_report

# Gerar relatório de avaliação de performance do modelo
report = classification_report(
    test_labels,
    predicted,
    target_names=['spam', 'ham'],
    output_dict=True
)

# Cria um DataFrame do relatório
pd.DataFrame(report).transpose()
```

**Métricas geradas:** acurácia, precisão, revocação e F1-score (fórmulas no arquivo de resumo teórico, seção 3.9).

---

### Célula 11 — Ajuste de hiperparâmetros com Grid Search

```python
from sklearn.model_selection import GridSearchCV

parameters = {
    # linspace do numpy gera uma lista entre intervalos (start, stop, length)
    'alpha': np.linspace(0.1, 1.0, 10),
    # Ligado ou desligado
    'fit_prior': [True, False],
    # Nenhum ou [probabilidade para cada classe]
    'class_prior': [None, [0.25, 0.5]]
}

# Instanciar o GridSearchCV com o estimador (model), o grid de parâmetros,
# validação cruzada com 5 folds e todos os processadores em paralelo (n_jobs=-1)
gs = GridSearchCV(model, parameters, cv=5, n_jobs=-1)

# Treinar o modelo N vezes com todas as combinações de parâmetros
gs.fit(train_features, train_labels)

# Imprimir melhor score e melhores parâmetros
print("Melhor score: ", gs.best_score_)
print("Melhores parâmetros: ", gs.best_params_)
```

> **Grid Search** testa exaustivamente todas as combinações (melhor para datasets pequenos com muitos parâmetros). **Random Search** testa combinações aleatórias (melhor para datasets grandes, onde o Grid Search ficaria caro demais computacionalmente).

---

### Bibliotecas utilizadas neste capítulo (resumo)

| Biblioteca | Papel no pipeline |
|---|---|
| `requests`, `zipfile`, `io` | Download e extração do dataset |
| `pandas` | Carregar e manipular o dataset em `DataFrame` |
| `re` | Expressões regulares para limpeza do texto |
| `nltk` | Stopwords, stemming (`PorterStemmer`) e tokenização (`word_tokenize`) |
| `numpy` | Operações numéricas, `seed`, `shuffle`, `linspace` |
| `sklearn.preprocessing.LabelEncoder` | Converter rótulos categóricos em binários |
| `sklearn.model_selection.train_test_split` | Dividir dados em treino/teste |
| `sklearn.feature_extraction.DictVectorizer` | Converter dicionários de features em matriz |
| `sklearn.naive_bayes.MultinomialNB` | Classificador Naïve Bayes multinomial |
| `sklearn.metrics.confusion_matrix`, `classification_report` | Avaliação do modelo |
| `sklearn.model_selection.GridSearchCV` | Ajuste de hiperparâmetros |

---

## 4.2 Anexo: Laboratório Guiado (VSCode)

> Este anexo guia você, passo a passo, na execução do pipeline de classificação de texto (SMS Spam Collection + Naïve Bayes) no **VSCode**, sem precisar de Jupyter/Colab. A cada passo: o que fazer, por quê, e o que conferir antes de seguir para o próximo.
>
> **Como rodar cada bloco:** crie um arquivo `sms_classifier.py` na pasta do laboratório e vá colando os blocos nele, **nesta ordem**. Depois de colar um bloco, selecione o trecho novo e aperte **Shift+Enter** — o VSCode abre um terminal Python interativo e executa só aquele trecho, mostrando o resultado na hora. Isso permite ver cada etapa funcionando antes de ir para a próxima, sem precisar rodar o arquivo inteiro de novo a cada vez. Quando quiser rodar tudo de uma vez, use o botão "Run Python File" ou `python sms_classifier.py` no terminal.

---

### Passo 0 — Preparar o ambiente

**Objetivo:** ter um ambiente Python isolado, com as bibliotecas do capítulo instaladas.

1. Crie uma pasta para o laboratório e abra-a no VSCode.
2. No terminal integrado do VSCode, crie e ative um ambiente virtual:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. Instale as bibliotecas usadas no capítulo:

```bash
pip install requests pandas nltk scikit-learn numpy
```

4. Confira se a extensão **Python** da Microsoft está instalada no VSCode e selecione o interpretador do `.venv` (canto inferior direito, ou `Ctrl+Shift+P` → "Python: Select Interpreter").

**Checkpoint:** rodar `python -c "import pandas, nltk, sklearn; print('ok')"` deve imprimir `ok` sem erro.

---

### Passo 1 — Baixar o dataset

**Objetivo:** obter o SMS Spam Collection Data Set (UCI), o mesmo usado no capítulo.

**Diferença em relação ao livro:** o capítulo usa `/content` porque está no Google Colab. No VSCode, vamos salvar na pasta local do projeto.

```python
import requests
import zipfile
import io
import os

# Pasta onde os dados ficarão salvos
os.makedirs("dados", exist_ok=True)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'

r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("dados")

print("Arquivos baixados:", os.listdir("dados"))
```

**O que conferir:** a lista impressa deve incluir `SMSSpamCollection` e `readme`. Esse é o arquivo de texto com as mensagens rotuladas.

---

### Passo 2 — Explorar o dataset com Pandas

**Objetivo:** entender o formato dos dados antes de processá-los — quantas mensagens, como estão rotuladas, qual a proporção spam/ham.

```python
import pandas as pd

df = pd.read_table("dados/SMSSpamCollection", header=None, encoding="utf-8")

print(df.info())
print(df.head())

classes = df[0]
print(classes.value_counts())
```

**O que conferir:** você deve ver **5.572 linhas**, coluna 0 = rótulo (`ham`/`spam`), coluna 1 = mensagem, e a contagem deve bater com **4.825 ham / 747 spam**. Se os números baterem, os dados estão carregados corretamente.

---

### Passo 3 — Ver o problema do ruído (opcional, só para visualizar)

**Objetivo:** visualizar, antes de limpar, que tipo de "sujeira" existe no texto (números, e-mails, pontuação). Este passo não altera nada — é só para você enxergar o motivo da limpeza que vem a seguir.

```python
import re

pattern = re.compile(r'[\d@_!#$%^&*()<>?/\|}{~:]')
text_messages = df[1]
amostra = text_messages[0:10]

for line in amostra:
    for word in line.split(' '):
        if re.search(pattern, word):
            print(word)
```

**O que conferir:** devem aparecer palavras com números, pontuação ou símbolos — essas são exatamente o tipo de ruído que o Passo 4 vai tratar.

---

### Passo 4 — Limpeza do texto com expressões regulares

**Objetivo:** padronizar o texto, substituindo e-mails, URLs, números de telefone, valores monetários e números por marcadores fixos, e remover pontuação e espaços extras — para que o classificador não trate "R$50" e "50" como coisas totalmente diferentes, por exemplo.

```python
processed_lines = text_messages.str.lower()

patterns = [
    (r'^.+@[^\.].*\.[a-z]{2,}$', 'emailaddress'),
    (r'^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$', 'webaddress'),
    (r'£|\$', 'moneysymb'),
    (r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$', 'phonenumbr'),
    (r'\d+(\.\d+)?', 'numbr'),
    (r'[^\w\d\s]', ' '),
    (r'\s+', ' '),
    (r'^\s+|\s+?$', '')
]

for pattern, newword in patterns:
    processed_lines = processed_lines.str.replace(pattern, newword, regex=True)

print(processed_lines.head())
```

> **Nota em relação ao livro:** adicionei `regex=True` explicitamente — em versões mais novas do pandas, `str.replace` exige esse parâmetro quando o padrão é uma expressão regular (no livro, de 2020, isso era o comportamento padrão).

**O que conferir:** compare `processed_lines.head()` com `df[1].head()` (o texto original) — você deve ver números virando `numbr`, tudo em minúsculas, sem pontuação.

---

### Passo 5 — Remover stopwords e aplicar stemming (NLTK)

**Objetivo:** tirar palavras sem valor discriminativo (artigos, pronomes) e reduzir palavras à sua forma-base, para que variações da mesma palavra não sejam tratadas como palavras diferentes pelo classificador.

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')  # necessário em versões recentes do NLTK

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stop_words = stopwords.words('english')
ps = PorterStemmer()

for i in range(len(processed_lines)):
    word_tokens = word_tokenize(processed_lines[i])
    filtered_sentence = []
    for word in word_tokens:
        if word not in stop_words:
            stemmed_word = ps.stem(word)
            filtered_sentence.append(stemmed_word)
    processed_lines[i] = ' '.join(filtered_sentence)

print(processed_lines.head())
```

> Este bloco segue a indexação do livro (`processed_lines[i]`) sem alteração — testei e ela funciona normalmente aqui, porque o índice da `Series` é o padrão (0, 1, 2...), que coincide com a posição. Só use `.iloc[i]` no lugar se, em algum momento, você filtrar ou reordenar `processed_lines` antes deste passo — aí o índice deixaria de coincidir com a posição.

**O que conferir:** o texto deve ficar mais enxuto — sem "the", "is", "to" etc. (stopwords em inglês, porque o dataset é em inglês).

---

### Passo 6 — Montar o vetor de features (palavras mais frequentes)

**Objetivo:** transformar texto em números. Primeiro, descobrir quais são as palavras mais frequentes em todo o dataset — elas serão as "colunas" do nosso vetor de características.

```python
all_words = []

for line in processed_lines:
    word_tokens = word_tokenize(line)
    for word in word_tokens:
        all_words.append(word)

all_words = nltk.FreqDist(all_words)

print(f'Total de palavras: {len(all_words)}')
print(f'Palavras mais comuns: {all_words.most_common(10)}')

word_features = list(all_words.keys())[0:1500]
print(f'Lista de características: {word_features[0:10]}')
```

**O que conferir:** as "palavras mais comuns" devem fazer sentido para um dataset de SMS (palavras curtas e genéricas). Se aparecer muito lixo (pontuação solta, números soltos), volte ao Passo 4/5 e confira se rodou certo.

---

### Passo 7 — Vetorizar cada mensagem e binarizar os rótulos

**Objetivo:** para cada mensagem, gerar um vetor dizendo quais das 1.500 palavras-modelo aparecem nela — e transformar "ham"/"spam" em 0/1.

```python
import numpy as np
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
bin_labels = encoder.fit_transform(classes)

messages = list(zip(processed_lines, bin_labels))

seed = 1
np.random.seed(seed)
np.random.shuffle(messages)

featuresets = []

for text, label in messages:
    word_tokens = word_tokenize(text)
    features = {}
    for word in word_features:
        features[word] = (word in word_tokens)
    featuresets.append((features, label))

print(f"Total de mensagens vetorizadas: {len(featuresets)}")
print(f"Exemplo (5 primeiras features da 1ª mensagem): "
      f"{list(featuresets[0][0].items())[:5]}, rótulo: {featuresets[0][1]}")
```

> **Nota em relação ao livro:** o código original usa `np.random.seed = seed` (atribuição, sem chamar a função) — testei, e isso tem dois problemas: não fixa a semente de fato, **e** substitui a função `np.random.seed` por um número inteiro, quebrando qualquer chamada futura a `np.random.seed(...)` no mesmo programa (gera `TypeError: 'int' object is not callable`). O correto é `np.random.seed(seed)`, como está acima.

**O que conferir:** o total deve ser 5.572 (mesmo número de mensagens do início). Cada feature deve ser `True`/`False`.

---

### Passo 8 — Dividir em treino e teste

**Objetivo:** separar uma parte dos dados para treinar o modelo e outra, nunca vista durante o treino, para avaliar se ele realmente aprendeu (e não apenas decorou).

```python
from sklearn.model_selection import train_test_split

training, testing = train_test_split(
    featuresets,
    train_size=None,
    test_size=0.25,
    random_state=seed
)

print("Treino:", len(training), "| Teste:", len(testing))

test_features, test_labels = zip(*testing)
train_features, train_labels = zip(*training)
```

**O que conferir:** treino deve ter ~75% das mensagens (≈4.179) e teste ~25% (≈1.393).

---

### Passo 9 — Treinar o classificador Naïve Bayes

**Objetivo:** converter os dicionários de features em matriz e treinar o `MultinomialNB`.

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer

vect = DictVectorizer(sparse=False)

train_features_vec = vect.fit_transform(train_features)
test_features_vec = vect.transform(test_features)

model = MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)
model.fit(train_features_vec, train_labels)

predicted = model.predict(test_features_vec)
print("Predições geradas:", len(predicted))
```

> **Correção importante em relação ao livro:** o capítulo usa `vect.fit_transform` tanto no treino quanto no teste. Isso é um erro — ao chamar `fit_transform` de novo no teste, o vetorizador **reaprende** um vocabulário novo a partir do teste, que pode não ter as mesmas colunas (nem na mesma ordem) do vocabulário de treino. O correto é `fit_transform` **só no treino**, e `transform` (sem `fit`) no teste, para garantir que os dois usem exatamente o mesmo espaço de features. É o que o código acima já faz.

**O que conferir:** nenhum erro de dimensão (`shape mismatch`) deve aparecer — se aparecer, é sinal de que `fit_transform` foi chamado duas vezes.

---

### Passo 10 — Avaliar o modelo

**Objetivo:** medir o quão bem o modelo classificou as mensagens de teste.

```python
from sklearn.metrics import confusion_matrix, classification_report

confus_matrix = confusion_matrix(test_labels, predicted)
df_confusao = pd.DataFrame(
    confus_matrix,
    index=[['Real', 'Real'], ['ham', 'spam']],
    columns=[['Predito', 'Predito'], ['ham', 'spam']]
)
print(df_confusao)

report = classification_report(
    test_labels,
    predicted,
    target_names=['ham', 'spam'],
    output_dict=True
)
print(pd.DataFrame(report).transpose())
```

> **Nota em relação ao livro:** os rótulos de linha/coluna foram ajustados para `['ham', 'spam']`, na mesma ordem que o `LabelEncoder` usa (0 = ham, 1 = spam) — o livro escreveu `['spam', 'ham']` no índice da matriz de confusão, o que inverteria a leitura das classes.

**O que conferir:** a acurácia (coluna "precision"/"recall" na linha de cada classe, ou calculada à mão com a fórmula do resumo teórico) deve ficar bem alta (tipicamente acima de 90% nesse dataset) — é um dataset relativamente "fácil" para Naïve Bayes.

---

### Passo 11 — Ajustar hiperparâmetros (opcional)

**Objetivo:** buscar automaticamente a melhor combinação de parâmetros do `MultinomialNB`, em vez de testar manualmente.

```python
from sklearn.model_selection import GridSearchCV

parameters = {
    'alpha': np.linspace(0.1, 1.0, 10),
    'fit_prior': [True, False],
    'class_prior': [None, [0.25, 0.5]]
}

gs = GridSearchCV(model, parameters, cv=5, n_jobs=-1)
gs.fit(train_features_vec, train_labels)

print("Melhor score:", gs.best_score_)
print("Melhores parâmetros:", gs.best_params_)
```

> **Nota em relação ao livro:** testei `class_prior=[0.25, 0.5]` isoladamente — o `scikit-learn` **aceita** sem erro, mesmo essa lista não somando 1 (0,25 + 0,5 = 0,75). Ele usa os valores exatamente como informados, sem normalizar. Ou seja, o código do livro roda, mas `[0.25, 0.5]` não representa probabilidades *a priori* coerentes (não é uma distribuição de probabilidade válida) — é um valor de exemplo didático, não um valor que você usaria de fato num caso real. Se quiser que o grid teste um `class_prior` que realmente some 1, troque para algo como `[0.25, 0.75]` ou `[0.5, 0.5]`.

**O que conferir:** `gs.best_score_` deve ser próximo (ou igual) à acurácia que você já tinha visto no Passo 10.

---

### Resumo das diferenças entre este laboratório e o código do livro

| # | O que o livro faz | O que foi ajustado aqui | Por quê | Testado? |
|---|---|---|---|---|
| 1 | Roda em `/content` (Colab) | Salva em `dados/` local | Você está no VSCode, não no Colab | — (ambiente) |
| 4 | `str.replace(pattern, newword)` | `str.replace(pattern, newword, regex=True)` | Pandas 3.x trata o padrão como texto literal sem esse parâmetro | ✅ confirmado |
| 5 | `processed_lines[i] = ...` | Mantido como no livro | Testei: funciona normalmente aqui, pois o índice da Series coincide com a posição | ✅ confirmado (correção anterior era desnecessária) |
| 7 | `np.random.seed = seed` | `np.random.seed(seed)` | A forma do livro não fixa a semente **e** quebra chamadas futuras a `np.random.seed(...)` | ✅ confirmado |
| 9 | `vect.fit_transform` no treino **e** no teste | `fit_transform` só no treino, `transform` no teste | Evita vocabulários diferentes entre treino e teste | ✅ confirmado |
| 10 | Índice `['spam', 'ham']` | Índice `['ham', 'spam']` | Bate com a ordem 0/1 do `LabelEncoder` (ordem alfabética) | lógica, não testado isoladamente |
| 11 | `class_prior: [None, [0.25, 0.5]]` | Mantido como no livro | Testei: o scikit-learn aceita sem erro, mesmo não somando 1 — é só um valor didático, não uma falha de código | ✅ confirmado (correção anterior era desnecessária) |

Duas das sete notas da primeira versão deste laboratório eram suposições minhas que não se confirmaram ao testar — mantive a tabela mostrando isso, em vez de simplesmente apagar o erro, porque isso é informação real sobre o quanto validar antes de afirmar importa mais do que parecer completo.

Essas são correções técnicas para o código **rodar corretamente** no seu ambiente — não mudam os conceitos do capítulo, só a implementação.

---

## Atividades e Avaliações

### Atividade 1 — Mineração de Dados (dissertativa)

**Enunciado:** Analise a afirmativa a seguir e explique a relação entre os conceitos de aprendizagem de máquina e mineração de dados: *"O aprendizado de máquina tem como foco a predição, com base em características já conhecidas, enquanto a mineração de dados extrai informação dos conjuntos de dados."*

**Método:** o documento segue em 3 seções (Aprendizado de Máquina, Mineração de Dados, Análise Estruturada), concluindo com a relação entre o conteúdo apresentado e a afirmativa.

**Aprendizado de Máquinas**

A Inteligência Artificial (IA) é um campo de estudo que possui importantes marcos históricos, entre eles o trabalho de McCulloch e Pitts (1943) e a publicação de Turing (1950). Nesse campo existem diversas áreas e subáreas, sendo o Aprendizado de Máquina (Machine Learning) uma delas.

O aprendizado de máquina pode ser dividido em diferentes modalidades, entre elas o aprendizado supervisionado, que abrange tarefas de classificação e regressão; o não supervisionado, que inclui tarefas como agrupamento; e o aprendizado por reforço.

O aprendizado supervisionado aprende a partir de uma base de conhecimento existente com dados rotulados, e estes dados e atributos são utilizados para realizar previsões ou classificações sobre novos dados.

No aprendizado não supervisionado, os algoritmos analisam os dados sem rótulos previamente definidos, buscando identificar estruturas e similaridades entre os objetos.

**Mineração de Dados**

Data Mining (mineração de dados) é o processo de explorar um conjunto de dados para descobrir informações, relações, regularidades e padrões que não são evidentes pela simples observação dos registros.

A mineração de dados tem como objeto de análise os conjuntos de dados e busca identificar padrões, relações e regularidades que possam gerar informações relevantes. A interpretação e a avaliação desses resultados contribuem para transformá-los em conhecimento útil ao contexto analisado.

**Análise Estruturada**

Para trazer a discussão desta atividade, dividimos a afirmativa em 3 blocos:

* Bloco 1: O aprendizado de máquina tem como foco a predição,
* Bloco 2: com base em características já conhecidas,
* Bloco 3: enquanto a mineração de dados extrai informação dos conjuntos de dados.

**Bloco 1**

A predição é de fato um dos focos de machine learning: utilizar os dados conhecidos para prever um comportamento posterior. Contudo, o aprendizado de máquina também é utilizado para entender o comportamento passado. Utilizando uma análise simples baseada em idade, nome, série e nota, temos uma análise de predição ao responder se o aluno vai ou não repetir de ano. De forma análoga, podemos também olhar para o passado — não no sentido de explicar a causa, mas de identificar que um aluno de 17 anos no segundo ano do ensino médio foge do padrão esperado para aquela série.

Consolidação: a predição é resultado de machine learning, mas a identificação de padrões fora do esperado no passado também é — o algoritmo não está respondendo "por quê", está respondendo "isso é normal ou não é".

**Bloco 2**

O aprendizado supervisionado trabalha com um conjunto de dados já rotulados, e para este podemos sim considerar a afirmativa: "com base em características já conhecidas".

No aprendizado não supervisionado, os dados podem conter atributos conhecidos, mas o algoritmo procura identificar estruturas e relações sem depender de rótulos previamente definidos. Assim, o aprendizado de máquina pode descobrir relações que ainda não eram conhecidas pelo analista.

O ponto neste bloco é que não necessariamente a característica já conhecida vai acontecer de forma antecipada à IA.

**Bloco 3**

A mineração de dados busca extrair informações relevantes de conjuntos de dados por meio da identificação de padrões, relações e regularidades. Entretanto, seu objetivo não se limita à extração de informações previamente conhecidas. A análise também pode revelar padrões que ainda não haviam sido identificados. Para que esses resultados contribuam para a geração de conhecimento, é necessário interpretá-los e avaliá-los de acordo com o contexto e o problema analisado.

**Análise Consolidada**

Além dos pontos informados acima, é importante realçar o relacionamento entre o aprendizado de máquinas e o data mining. Ambos podem existir sem o outro. Existe data mining sem uma análise de aprendizado de máquinas e também existe o aprendizado de máquinas sem existir o data mining. Porém ambos são complementares, e quando tratarmos de problemas complexos, a utilização conjunta deles pode ser de grande valia (FAYYAD; PIATETSKY-SHAPIRO; SMYTH, 1996).

> **Referência usada na Atividade 1:** FAYYAD, U.; PIATETSKY-SHAPIRO, G.; SMYTH, P. From Data Mining to Knowledge Discovery in Databases. *AI Magazine*, v. 17, n. 3, p. 37–54, 1996.

---

### Atividade 2 — Quiz: Pré-processamento e Mineração de Dados (A2)

**Formato:** 10 questões objetivas (LevelUp/Plataforma A). **Resultado final: 9/10** (após revisão — primeira tentativa: 6/10).

| # | Tema | Resposta correta | Observação |
|---|---|---|---|
| 1 | Tarefas de pré-processamento | A — limpeza, integração, redução, transformação, discretização | "Mineração" e "coleta" não são tarefas de pré-processamento |
| 2 | Metodologias de redução dimensional | B — SVD e PCA | PCR é técnica de regressão, não de redução dimensional |
| 3 | Normalização min-max (lista X = [2,2,4,6,9,3,9,12]) | B — 3 elementos > 0,5 | Cálculo: (x−2)/10; valores 0,7 / 0,7 / 1,0 ficam acima de 0,5 |
| 4 | Visualização de dados numéricos em categóricos | C — histograma | Representação clássica de discretização |
| 5 | Código R para converter para maiúsculas | B — com atribuição (`assassinatos <- ... mutate(...)`) | Sem atribuição, a transformação não é persistida |
| 6 | Dados qualitativos x quantitativos | A | Definição direta, sem ressalvas que misturam os dois conceitos |
| 7 | Classificação dos atributos de uma tabela (ID, Nome, Gênero, País, Data, Salário) | **D** | ID = Categórico ordinal (nesta disciplina, diferente da escala nominal de RG/CPF vista na Aula 1) |
| 8 | Empecilhos de dados brutos ao aprendizado | B — ruídos, dados duplicados e, principalmente, valores ausentes | Resposta mais completa; "apenas outliers" (A) é incompleta |
| 9 | *Missing values*: dropping x filling | C — dropping remove linha / filling preenche (média ou valores próximos) | Bate com "descartar registro" da Aula 4 de AED (disciplina anterior) |
| 10 | Técnicas de transformação de dados | A — normalizações, agregações, construção de atributo e discretização | Seleção de subconjunto, amostragem e PCA são técnicas de *redução*, não de transformação |

**Observação sobre a Q7:** a resposta correta desta disciplina trata um identificador sequencial (ID) como **categórico ordinal**, o que diverge da escala **nominal** usada como exemplo de RG/CPF no capítulo da Aula 1 (Izabelly Soares de Morais). Vale ter essa nuance registrada para provas futuras sobre tipos de dados nesta disciplina.

---

### Atividade 3 — Pré-processamento de texto (PLN): tokenização e limpeza (A3)

**Objetivo da PLN:** Identificar etapas executadas pela aluna em cada aula.

**Frase:** Daniela leu o livro para depois faser o trabalho.

**Etapa 1: Tokenização**

`["Daniela", "leu", "o", "livro", "para", "depois", "faser", "o", "trabalho", "."]`

**Etapa 2: Limpeza**

* Remoção de stopwords (removidos: "o", "para", "depois", "o"):
  `["Daniela", "leu", "livro", "faser", "trabalho", "."]`
* Remoção de pontuação (removido o "."):
  `["Daniela", "leu", "livro", "faser", "trabalho"]`
* Opcional incluída: correção de erros de digitação ("faser" → "fazer"):
  `["Daniela", "leu", "livro", "fazer", "trabalho"]`
* Padronização em minúsculas ("Daniela" → "daniela"):
  `["daniela", "leu", "livro", "fazer", "trabalho"]`

**Texto final após o pré-processamento:**

`daniela leu livro fazer trabalho`

**Nota:** "depois" foi removido, conforme exemplo no capítulo. Para este objetivo em específico, a ordem das atividades não importa. O objetivo é identificar as etapas e não sequenciá-las.

---


## Desempenho Consolidado

| Atividade | Tema | Nota / Resultado |
|---|---|---|
| Atividade 1 | Mineração de Dados (dissertativa) | Entregue — ver análise completa acima |
| Atividade 2 (A2) | Pré-processamento e Mineração de Dados (quiz, 10 questões) | 9/10 (revisado de 6/10) |
| Atividade 3 (A3) | Pré-processamento de texto — tokenização e limpeza | Entregue — PDF gerado com cabeçalho/rodapé FMU |

---

## Arquivos Relacionados (neste repositório / outputs)

1. `AULA_01_RESUMO_APRENDIZADO_DE_MAQUINA.md`
2. `AULA_02_RESUMO_BPM.md`
3. `AULA_03_RESUMO_CLASSIFICACAO_DE_TEXTOS.md`
4. `AULA_04_RESUMO_CLASSIFICACAO_TEXTO_PYTHON.md`
5. `AULA_04_CLASSIFICACAO_TEXTO_PYTHON_PRATICO.md`
6. `AULA_04_LABORATORIO_VSCODE.md`
7. `Aprendizadosupervisionado_atividade3.md` / `.pdf`
8. `Atividade1_Mineracao_de_Dados.pdf`
9. `DISCIPLINA_APRENDIZADO_MAQUINA_SUPERVISIONADO.md` — **este arquivo**

---

## Como Usar Este Documento

1. **Revisão rápida:** leia as seções de cada aula.
2. **Estudo aprofundado:** acesse os arquivos `.md` individuais de cada aula, se precisar do contexto isolado.
3. **Implementação prática:** use o código Python da Aula 4 (seção 4.1) e o laboratório guiado (seção 4.2) direto no VSCode.
4. **Revisão de provas:** a seção "Atividades e Avaliações" reúne o que já foi entregue e corrigido.

---

## Próximos Passos Sugeridos

1. Aguardar e documentar novas aulas da disciplina, conforme forem liberadas.
2. Quando todas as aulas estiverem concluídas, gerar a versão em **HTML (apostila do curso)**, conforme planejado.
3. Revisar a nuance de taxonomia de tipos de dados (Atividade 2, questão 7) antes de provas futuras sobre o tema.

---

**Última atualização:** outubro de 2026
