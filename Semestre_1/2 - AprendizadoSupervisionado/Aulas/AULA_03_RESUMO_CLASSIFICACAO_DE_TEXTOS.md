# AULA 3 — CLASSIFICAÇÃO DE TEXTOS: INTRODUÇÃO AO APRENDIZADO SUPERVISIONADO

## Disciplina: Aprendizado de Máquina Supervisionado — Graduação em IA (FMU)

---

## 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Supervisionado (262GGR4728A)
**Aula:** 3 — Classificação de textos — introdução ao aprendizado supervisionado
**Fonte:** *Processamento de Linguagem Natural* — Michel Bernardo Fernandes da Silva, SAGAH (Soluções Educacionais Integradas), capítulo "Classificação de textos — introdução ao aprendizado supervisionado"

### Objetivos de aprendizagem (conforme o capítulo)
- Definir a área de *machine learning*.
- Descrever exemplos de aplicações de *machine learning* para classificação de textos.
- Identificar os elementos que compõem as soluções de classificação de textos.

---

## 2. Resumo e Contextualização

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

## 3. Conceitos Fundamentais e Explicações

### 3.1 Classificações de aprendizado de máquina

A classificação mais frequente divide o AM em **supervisionado, não supervisionado e por reforço**.

| | **Aprendizado supervisionado** | **Aprendizado não supervisionado** | **Aprendizado por reforço** |
|---|---|---|---|
| **O que é** | Existe um conjunto pré-definido de **pares entrada/saída**; as entradas são atributos dos objetos a reconhecer. O treinamento usa esses dados e o programa precisa tomar decisões precisas quando recebe novos dados. | O programa busca **padrões e relações** em um conjunto de dados, recebendo **somente os dados de entrada**; os padrões de saída são aprendidos pelo próprio sistema. | O agente de aprendizagem adquire conhecimento sobre seu processo a partir do **reforço ou da recompensa**; também contempla o subproblema de entender como o ambiente funciona. |
| **Quando utilizar** † | Quando há dados **já rotulados** e o objetivo é prever o rótulo (ou valor) de novos dados. | Quando **não há rótulos prévios** e o objetivo é descobrir estrutura nos dados (ex.: agrupar por semelhança). | Quando um agente **interage com um ambiente** e aprende a partir de recompensas/penalidades, e não de exemplos rotulados. |
| **Exemplos** | Posts do Facebook ou tweets marcados como positivos, neutros e negativos para criar um classificador de **análise de sentimento**. Técnicas: redes neurais artificiais com treinamento supervisionado, árvores de decisão. | **Agrupamento automático de e-mails** recebidos por um funcionário, por temas semelhantes, sem conhecimento prévio sobre os dados de entrada. | Uma **multa de trânsito** indica ao agente que seu comportamento foi inadequado. |

> † **Linha "Quando utilizar":** o capítulo **não traz um critério explícito** de "quando utilizar" cada tipo. O conteúdo dessa linha foi **derivado das definições do próprio capítulo** (presença/ausência de rótulos, presença de recompensa). Tratar como síntese de estudo, não como citação do livro.

**Observação do capítulo:** em geral, um sistema de aprendizado dispõe de um conjunto de dados de treinamento **classificados manualmente**, com base nos quais aprende a classificar esses dados e **novos dados ainda não observados** (característica do supervisionado).

### 3.2 Técnicas citadas

- **Supervisionado:** redes neurais artificiais com treinamento supervisionado; árvores de decisão (*decision tree*).
- **Aprendizagem profunda (*deep learning*):** categoria de algoritmos de ML que usa **redes neurais artificiais** para gerar modelos; bem-sucedida em reconhecimento de imagem; as redes são inspiradas nas redes neurais biológicas (rede de nós interconectados) e usadas, em geral, quando o volume de entrada é muito grande, o que torna abordagens convencionais inadequadas.

### 3.3 Árvore de decisão

- Chega à decisão por meio de uma **sequência de testes**.
- **Nó interno** = teste do valor de um atributo de entrada *Aᵢ*.
- **Ramificações** = valores possíveis do atributo (*Aᵢ = vᵢₖ*).
- **Nó folha** = valor retornado pela função.
- Os exemplos são processados a partir da **raiz**, seguindo a ramificação apropriada até alcançar uma folha.

### 3.4 Terminologia de dados (Baranauskas e Monard, 2000, e demais autores do capítulo)

| Termo | Definição no capítulo |
|---|---|
| ***Inducer*** (programa de aprendizagem) | Tem como objetivo gerar um bom **classificador** para um conjunto de instâncias já classificadas; o classificador é usado para prever o rótulo de instâncias não rotuladas. |
| **Atributo / *feature*** | Descrição ou característica de um aspecto da instância. Atributos podem ser **nominais** (ex.: cor, país de nascimento) ou **contínuos** (ex.: altura, peso — números reais). *Features* são usadas como **preditores** ou **variáveis independentes**, correspondendo às **colunas** da base. |
| **Instância** | Lista fixa de valores de atributos; descreve a entidade tratada (ex.: dados médicos sobre uma doença). |
| **Classe / rótulo** | Característica especial do aprendizado supervisionado que descreve o fenômeno de interesse, a tarefa de aprendizado e a realização de predições com base nele. |
| ***Dataset*** | Coleção de instâncias **classificadas (rotuladas)**. Os rótulos podem ser um conjunto **discreto** de classes (**classificação**) ou **valores reais** (**regressão**). |

Dado um conjunto de instâncias de treino, o programa gera um classificador que, para uma nova instância, poderá prever com precisão o rótulo dela.

### 3.5 Aplicações de ML para classificação de textos

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

### 3.6 Elementos da solução: o *pipeline* de classificação de texto

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

### 3.7 Superfície de decisão e algoritmos

- **Hiperplano de separação:** forma clássica de gerar uma superfície de decisão; pode ser perpendicular ou não ao eixo (Figura 4: (a) hiperplano perpendicular, (b) não perpendicular).
- **KNN (*K-Nearest Neighbors*, k-ésimo vizinho mais próximo):** usado quando as classes **não** podem ser separadas por forma geométrica. Define-se um número *k* de vizinhos; o novo exemplo recebe a **classe mais presente entre os *k* vizinhos mais próximos** (Figura 5: três classes, cinco vizinhos).
- **Naive Bayes:** classificador **probabilístico** muito usado em ML, baseado no teorema de Bayes (Thomas Bayes, 1702–1761); segundo o capítulo, "desconsidera a correlação entre as variáveis".

### 3.8 Expressões regulares (conceito citado antes do pré-processamento)

No capítulo, as **expressões regulares (RE)** aparecem como "um conceito importante nesse contexto", **antes** do subtítulo "Pré-processamento e limpeza do texto". O texto **não as apresenta como uma etapa do pré-processamento**.

- Notação padronizada para caracterizar cadeias de caracteres (*strings*), aplicável a qualquer sequência de caracteres alfanuméricos (letras, números, espaços, pontuações, tabulações). O espaço é um caractere como os demais.
- Uma expressão regular de pesquisa precisa de um **padrão** a pesquisar e de um ***corpus*** (conjunto de textos escritos e registros orais de uma língua, usado como base de pesquisa e análise).
- Um **autômato de estados finitos** é a estrutura matemática usada para implementar expressões regulares, uma das ferramentas mais significativas da linguística computacional.

### 3.9 Pré-processamento e limpeza do texto

Motivo: conjuntos de dados contêm palavras desnecessárias, erros ortográficos e gírias; em algoritmos estatísticos/probabilísticos, ruído e características desnecessárias prejudicam o desempenho (Jurafsky e Martin, [2020]).

| Técnica | Descrição |
|---|---|
| **Tokenização** | Quebra fluxos de texto em palavras, frases, símbolos ou outros elementos significativos chamados ***tokens***. |
| **Remoção de *stopwords*** | Remove palavras sem informação relevante para classificação (ex.: "um/uma", "sobre", "acima", "através", "depois", "novamente", "para"). |
| **Remoção de pontuação e caracteres especiais** | Importantes para a compreensão humana, mas podem atrapalhar o algoritmo. |
| **Padronização de maiúsculas/minúsculas** | Transformar tudo em minúsculas é abordagem comum, mas pode gerar problemas: o pronome "ti" e a sigla "TI" (Tecnologia de Informação) passam a ter a mesma representação. |
| **Correção de erros de digitação (*typos*)** | Etapa **opcional**; comum em textos de mídias sociais (Twitter, Facebook). |

---

## 4. Exemplos, Aplicações e Material Prático

### 4.1 Árvore de decisão — esperar ou não por uma mesa (Figura 1; Russell e Norvig, 2013, p. 812)
Objetivo: aprender uma função para o predicado **VaiEsperar**. Exemplo do capítulo: uma situação com *Clientes = Cheio* e *EsperaEstimada = 0-10* é classificada como **positiva** (esperaremos por uma mesa). Atributos usados na árvore: Clientes, EsperaEstimada, Alternativa, Reserva, Sex/Sáb, Bar, Faminto, Chovendo.

### 4.2 Tokenização
Frase: *"Depois de ir ao parque, ela decidiu fazer compras no mercado."*
*Tokens:* {"Depois" "de" "ir" "ao" "parque" "ela" "decidiu" "fazer" "compras" "no" "mercado"}

### 4.3 Processamento básico de um texto (Figura 6; adaptada de Travizan Neto, 2017)
`"O carro."` → (remoção de *stopwords*) → `" carro."` → (remoção de pontuação) → `" carro"`

### 4.4 Análise de sentimento aplicada a programas do Governo Federal (Figura 2; Oliveira *et al.*, 2019, p. 245–246)
Foram avaliados *tweets* sobre Bolsa Família, Minha Casa Minha Vida, Mais Médicos e Pronatec. Categorias de polaridade: positivo, negativo, neutro e **falso-positivo** (tweet irônico que parece positivo, mas não é).

| Programa | Positivo | Neutro | Negativo |
|---|---|---|---|
| Pronatec | 69% | 16% | 15% |
| Minha Casa, Minha Vida | 49% | 12% | 39% |
| Mais Médicos | 41% | 5% | 54% |
| Bolsa Família | 35% | 7% | 58% |

### 4.5 Exemplo histórico (quadro "Saiba mais")
Nos primeiros sistemas de tradução automática (década de 1950, russo→inglês), a frase *"The spirit is willing, but the flesh is weak"* voltou como *"The vodka is good, but the meat is rotten"* — ilustra as limitações iniciais da tradução automática. (Um projeto da CIA investiu milhões de dólares em um software de tradução russo→inglês.)

**Material prático em código:** o capítulo não apresenta código. Não foi criado arquivo prático complementar para esta aula.

---

## 5. Minhas Observações e Dúvidas

*(Espaço reservado — nenhuma observação registrada até o momento para esta aula.)*

### Pontos de atenção no texto-base (identificados na análise; não são observações da aluna)
1. **Referência de figura possivelmente trocada:** o texto diz que cada ponto é rotulado com um valor de classe de *k* valores discretos "(Figura 4)", mas a Figura 4 mostra **superfícies de decisão (hiperplanos)**, não a estrutura de rótulos.
2. **Posição de uma frase:** "um sistema de aprendizado dispõe de um conjunto de dados de treinamento classificados manualmente..." aparece logo após o parágrafo do **não supervisionado**, mas descreve o **supervisionado**. Pode confundir na leitura.
3. **Fases x figura:** o texto lista **quatro fases** (incluindo redução de dimensão), mas também diz que a redução é **opcional**; a Figura 3 mostra a redução tracejada (opcional). Não é contradição, mas vale reter que o pipeline mínimo é extração → classificação → avaliação.
4. **Tipos de aprendizado:** este capítulo apresenta **três** tipos (supervisionado, não supervisionado, por reforço) e **não menciona o semissupervisionado**, que aparece no capítulo da Aula 1.
5. **Complementação (fora do capítulo):** a frase de que o Naive Bayes "desconsidera a correlação entre as variáveis" é uma simplificação; tecnicamente, ele **assume independência condicional entre as *features*** dada a classe. Registrar como nota de estudo, sem atribuir ao autor do capítulo.

---

## 6. Referências e Conexões com Outros Conteúdos

### Referência principal
SILVA, Michel Bernardo Fernandes da. **Processamento de Linguagem Natural** — capítulo "Classificação de textos — introdução ao aprendizado supervisionado". SAGAH.

### Referências citadas no capítulo
- BARANAUSKAS, J. A.; MONARD, M. C. *Reviewing some Machine Learning Concepts and Methods.* São Carlos: ICMC-USP, 2000. (Relatórios Técnicos do ICMC-USP, 102).
- JURAFSKY, D. S.; MARTIN, J. H. *Speech and language processing.* 3. ed. Upper Saddle River: Prentice Hall, [2020].
- KOWSARI, K. *et al.* Text Classification Algorithms: A Survey. *Information*, v. 10, n. 150, p. 1–68, 2019.
- OLIVEIRA, D. J. S. *et al.* A aplicação da técnica de análise de sentimento em mídias sociais como instrumento para as práticas da gestão social em nível governamental. *Revista de Administração Pública*, v. 53, n. 1, p. 235–251, 2019.
- RODRIGUES, N. *Ebook: Guia sobre Chatbots – Seu negócio ainda vai ter um.* Cedro Technologies, 2017.
- RUSSELL, S.; NORVIG, P. *Inteligência artificial.* 3. ed. Rio de Janeiro: Elsevier, 2013.
- SAS INSTITUTE. *Machine Learning: O que é e qual sua importância.* 2019.
- TRAVIZAN NETO, A. *Classificação de traços de personalidade através de Linguagem Natural aplicada a ambientes virtuais de aprendizagem.* TCC, UFU, 2017.

### Conexões com outras aulas e disciplinas
- **Aula 1 (Aprendizado de Máquina):** retoma supervisionado/não supervisionado/reforço; **classificação** (rótulos discretos) e **regressão** (valores reais) aparecem nas duas aulas; KNN, Naive Bayes, árvores de decisão, regressão logística e redes neurais já haviam sido listados no Quadro 2 da Aula 1.
- **Atividade 1 (Mineração de Dados):** o capítulo usa "mineração de opiniões" e "mineração de textos" como aplicações do ML, o que dialoga com a distinção ML x mineração de dados discutida na atividade.
- **Atividade A2 / Aula de pré-processamento:** ruído, redução dimensional e limpeza de dados reaparecem aqui no contexto de texto (*stopwords*, pontuação, *typos*, redução de dimensão opcional).
- **Aquisição e Preparação de Dados:** tokenização, remoção de ruído e padronização são a versão textual da limpeza/transformação vistas em ETL e AED.
- **Aprendizado Não Supervisionado:** o exemplo de agrupamento automático de e-mails conecta diretamente com essa disciplina.

---

**Status:** Aula 3 documentada.
