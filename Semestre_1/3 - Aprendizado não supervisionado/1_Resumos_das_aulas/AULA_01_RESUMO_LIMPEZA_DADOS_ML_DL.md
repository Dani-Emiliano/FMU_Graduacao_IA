# AULA 1 — QUALIDADE DE DADOS, MACHINE LEARNING E DEEP LEARNING

## APRENDIZADO DE MÁQUINA NÃO SUPERVISIONADO (262GGR6044A) — Graduação em IA, FMU

---

## 1. Identificação e Objetivos

**Disciplina:** Aprendizado de Máquina Não Supervisionado (262GGR6044A)
**Aula:** 1
**Livro-base da aula:** *Engenharia do Conhecimento e Inteligência Artificial* — Cynthia da Silva Barbosa (SAGAH)

**Objetivos de aprendizagem (do livro-base):**
- Comparar mitos e verdades sobre inteligência artificial.
- Relacionar a utilização de engenharia do conhecimento para criação de sistemas inteligentes.
- Reconhecer as principais tecnologias e ferramentas utilizadas para desenvolvimento de aplicações inteligentes e análise de dados.

> A aula em si não detalhou modelos de ML/redes neurais/deep learning em profundidade — esse aprofundamento vem do capítulo do livro-base, conforme observação da Dani na seção 5.

---

## 2. Resumo e Contextualização

A Aula 1 retoma a importância da **estruturação e qualidade dos dados** — tema que conecta diretamente com a disciplina anterior (Aquisição e Preparação de Dados) — e introduz o panorama de **Inteligência Artificial**, **Engenharia do Conhecimento**, **Machine Learning** (supervisionado e não supervisionado) e **Deep Learning**, que serão a base conceitual do restante da disciplina de Aprendizado Não Supervisionado.

A normalização de dados foi mencionada na aula, mas **não será registrada aqui** por já ter sido coberta em detalhe na disciplina anterior (Aquisição e Preparação de Dados).

---

## 3. Conceitos Fundamentais e Explicações

### 3.1 Dificuldades da Limpeza de Dados *(material acadêmico — slide da aula)*

O termo *limpeza dos dados* existe porque nem sempre os dados têm a qualidade esperada. Quatro problemas típicos:

| Tipo | Definição |
|---|---|
| **Dados ruidosos** | Apresentam valores ou erros que divergem do esperado (ex.: idade = 450) |
| **Dados inconsistentes** | Contradizem os valores de atributos do mesmo objeto — comum em etapas de integração de tabelas diferentes (ex.: mesma pessoa com idades diferentes em registros distintos) |
| **Dados redundantes** | Os valores dos atributos dos objetos se repetem |
| **Dados incompletos** | Há detecção de ausência de valores ou de parte de algum dado |

*(Exemplos ilustrados com uma tabela de Nome/Idade/Telefone contendo os quatro tipos de problema.)*

**Conexão direta:** este conteúdo é uma continuação natural do que foi visto em ETL e Análise Exploratória de Dados na disciplina anterior — os mesmos quatro problemas (ruído, inconsistência, redundância, incompletude) aparecem lá sob a ótica de tratamento de dados (missing values, outliers, conflitos semânticos/estruturais).

---

### 3.2 Inteligência Artificial: Mitos e Verdades *(livro-base)*

O conceito de IA surgiu em **1956**, com o objetivo de imitar o comportamento humano por meio de computadores.

A IA já está presente no cotidiano (Google Maps/Waze, buscadores, Netflix) e em praticamente todos os setores: indústria, vendas/marketing, saúde, segurança, ensino, robótica, ciência de dados.

**Quadro de mitos x realidade (livro):**

| Mito | Realidade |
|---|---|
| A IA substituirá o trabalho de desenvolvedores | A IA muda funções existentes e cria novas posições |
| Tomará decisões e fará diagnósticos médicos de altíssima complexidade | O profissional de saúde ainda decide; a IA acelera o processo |
| Controlará pessoas | É usada para automatização e produtividade |
| Não compreenderá as necessidades do cliente | Melhora o relacionamento (ex.: chatbots) |
| Dificilmente identificará pessoas | Identificação facial e reconhecimento de voz são aplicações fortes |
| Não preverá tendências futuras | Realiza previsões com base em pesquisas e análises |

**Classificação da IA (Mussa, 2020):**
- **IA genérica/forte:** máquinas realizariam todas as tarefas humanas, incluindo pensar e autoaprimorar-se — hipótese de singularidade. Ainda não comprovada; exemplo citado (Deep Blue x Kasparov, 1997) é IA estreita disfarçada de "forte".
- **IA estreita/fraca:** realiza tarefas específicas (tradução, reconhecimento facial, filtro de spam). É a base deste capítulo e da maioria das aplicações reais (Google, Amazon, Facebook, Alibaba, Waze, Uber).

---

### 3.3 Engenharia do Conhecimento *(livro-base)*

Originalmente, consistia em criar **sistemas especialistas** transferindo o conhecimento de profissionais especialistas — abordagem que se mostrou limitada (raciocínio humano é incerto e varia de profissional para profissional).

Evoluiu para uma abordagem de **modelagem computacional**, dando origem aos **sistemas de conhecimento** (sistemas especialistas + sistemas baseados em conhecimento), que são a base da IA.

**Hierarquia (Figura 1 do livro):**
```
Inteligência Artificial
 └─ Sistemas Inteligentes
     └─ Sistemas Baseados em Conhecimento
         └─ Sistemas Especialistas
```

**Características dos sistemas inteligentes:**
- Utilizam conhecimento para realizar atividades ou solucionar problemas.
- Realizam associações para lidar com problemas complexos.
- Armazenam e recuperam grandes volumes de informação para apoiar decisões.

**Atividades típicas da engenharia do conhecimento:** interpretação/análise de dados, classificação, monitoramento de sistemas, planejamento, previsão, projeto.

---

### 3.4 Machine Learning *(livro-base)*

Objetivo: compreender a estrutura dos dados e adaptá-los a modelos conhecidos, facilitando interpretação, análise e predição via algoritmos. Característica central: **aprender com os dados fornecidos**.

#### Supervisionado
Possui resultado esperado conhecido durante o treinamento.
- **Classificação:** classifica o novo dado com base em critérios aprendidos no treino (ex.: tumor benigno/maligno).
- **Regressão:** gera uma função que descreve como uma variável se comporta em relação a outras (ex.: estimar idade de uma pessoa).

#### Não supervisionado
Computadores aprendem padrões, conceitos e dados **não rotulados**, sem supervisão — identificam semelhanças com base em padrões/repetições.
- **Agrupamento (clustering):** dados agrupados por similaridade (ex.: agrupar clientes por preferência).
- **Associação:** procura padrões relacionados entre atributos (ex.: produtos vendidos em conjunto).
- **Sumarização:** busca descrição simples e compacta de um conjunto de dados (ex.: sumarizar notícias).
- Também usado em **detecção de anomalias** (peças defeituosas, fraude).

> Esta é a categoria central da disciplina atual (Aprendizado de Máquina Não Supervisionado).

#### Aprendizagem por reforço
Baseada em punição de ações negativas e recompensa por ações positivas. A máquina testa caminhos, avalia o resultado e ajusta estratégia quando insatisfatório. Usada em algoritmos financeiros/de investimento.

---

### 3.5 Deep Learning e Redes Neurais Artificiais (RNA) *(livro-base + slide da aula — ponto que a Dani identificou como pouco aprofundado na aula)*

**Deep Learning** é a parte avançada do Machine Learning, técnica para extração automatizada de padrões de grandes volumes de dados, modelando-os em alto nível de abstração (Schmidhuber, 2015). Usa **Redes Neurais Artificiais (RNAs)** como base — RNAs imitam o funcionamento dos neurônios do sistema nervoso.

**Como a RNA processa informação (slide da aula):**
1. Os neurônios processam dados para reconhecer padrões (ex.: reconhecimento facial, reconhecimento de fala).
2. A informação passa por camadas: a **camada de entrada** recebe os dados, as **camadas ocultas** (intermediárias) processam, a **camada de saída** produz o resultado. Cada camada é tipicamente um algoritmo simples e uniforme com uma função de ativação.
3. O Deep Learning aprende com seus erros via **Back Propagation**: o resultado da rede é comparado ao esperado (Comparador), o erro é calculado e retropropagado pela rede para ajustar os pesos.

**Exemplo funcional (livro):** porta lógica AND — a rede neural calcula a função com base em duas entradas booleanas; só é verdadeira quando ambas as entradas são verdadeiras. Serve de analogia didática para como a RNA combina entradas para gerar uma saída.

**Classificação das técnicas de Deep Learning (livro):**
- **Redes para aprendizado supervisionado:** auxiliam na classificação de padrões conforme a distribuição das classes.
- **Redes de aprendizado não supervisionado (ou de geração):** identificam relações em dados não rotulados; dados visíveis são caracterizados por distribuições estatísticas conjuntas.
- **Redes híbridas:** combinam métodos generativos e discriminativos.

**CNN (Convolutional Neural Network):** classe de rede neural voltada à análise e processamento de imagens digitais. Exemplo citado (Krizhevsky, Sutskever e Hinton, 2012): CNN com 60 milhões de parâmetros e 650 mil neurônios em 5 camadas convolucionais, treinada para classificar mais de 1 milhão de imagens do banco ImageNet.

**Aplicações de Deep Learning:** processamento/reconhecimento de imagens, identificação de doenças, desenvolvimento de medicamentos, reconhecimento facial e de fala.

**Ferramentas citadas:** Knime (código aberto, integração/análise/mineração de dados), Deeplearning4J (framework Java, voltado a negócios), Lasagne (abstrai complexidade de DL, interface em Python).

---

### 3.6 Big Data *(livro-base)*

Grande base de dados em repositórios, não necessariamente estruturados. Os **5 V's** (Barbieri, 2011):

| V | Descrição |
|---|---|
| **Volume** | Coleta por diversas fontes (redes sociais, navegadores, e-commerce) |
| **Velocidade** | Ritmo de geração de dados por celulares, sensores etc. |
| **Veracidade** | Necessidade de verificar se as informações são verdadeiras |
| **Variedade** | Dados estruturados ou não, de diferentes fontes (vídeo, áudio, e-mail) |
| **Valor** | Dados agregam valor à tomada de decisão organizacional |

**Ferramenta citada:** Hadoop (open source, processa grandes volumes em arquitetura cluster/servidores distribuídos). Exemplos de uso: Walmart e Nike para pesquisa de mercado e perfil de consumo.

**Outras tecnologias mencionadas (aplicadas à robótica/IA):**
- **Transfer learning:** reaproveita conhecimento adquirido na resolução de um problema em outro problema similar.
- **Reinforcement learning:** agentes inteligentes agem em um ambiente maximizando recompensa.
- **GAN (Generative Adversarial Network):** gera conteúdo cuja autenticidade não é evidente na avaliação.

---

### 3.7 PCA x Análise Fatorial — movido para a Aula 3

O infográfico comparando PCA e Análise Fatorial faz parte do material da Unidade 3 e está registrado em `AULA_03_RESUMO_PCA_OUTLIERS.md` (seção 3.1).

---

## 4. Exemplos, Aplicações e Material Prático

- Exemplo de dados ruidosos/inconsistentes/redundantes/incompletos: tabela Nome/Idade/Telefone (slide da aula).
- Exemplo de RNA/porta lógica AND (tabela verdade) — livro.
- Exemplo de reconhecimento facial e de fala como aplicações de camadas de neurônios — slide da aula.
- Exemplo de classificação de imagens via CNN (ImageNet, Krizhevsky et al., 2012) — livro.
- Exemplo de Big Data aplicado por Walmart e Nike — livro.
- Exemplo de detecção de fraude em cartão de crédito via ML (compra fora do padrão geográfico do cliente) — livro.

Nenhum código Python foi apresentado nesta aula (diferente da Aula 3 da disciplina anterior, que trouxe implementações de normalização com Scikit-learn).

---

## 5. Minhas Observações e Dúvidas

- **[Dani]** A parte de estruturação/limpeza dos dados (dados ruidosos, inconsistentes, redundantes, incompletos) se relaciona diretamente com a disciplina anterior (Aquisição e Preparação de Dados).
- **[Dani]** A aula apresentou modelos (ML, rede neural, deep learning) mas sem aprofundar — considerado um ponto essencial que precisa de mais detalhe. Por isso, o conteúdo da seção 3.4 e 3.5 foi trazido com base no capítulo do livro-base (*Engenharia do Conhecimento e Inteligência Artificial*).
- **[Dani]** A aula também abordou normalização de dados, mas esse conteúdo não foi registrado aqui por já ter sido coberto na disciplina anterior.

---

## 6. Referências e Conexões com Outros Conteúdos

**Livro-base desta aula:**
BARBOSA, C. da S. *Engenharia do conhecimento e inteligência artificial*. SAGAH.

**Referências citadas no capítulo:**
- ABEL, M.; FIORINI S. R. Uma revisão da engenharia do conhecimento: evolução, paradigmas e aplicações. *International Journal of Knowledge Engineering and Management*, v. 2, nº 2, p. 1–35, 2013.
- BARBIERI, C. *BI2-Business intelligence*: modelagem e qualidade. Rio de Janeiro: Elsevier, 2011.
- CLAUDINO, L. S. A. *Machine learning*. Londrina: Educacional S.A., 2019.
- KRIZHEVSKY, A.; SUTSKEVER, I.; HINTON, G. E. ImageNet classification with deep convolutional neural networks. In: INTERNATIONAL CONFERENCE ON NEURAL INFORMATION PROCESSING SYSTEMS, 25., 2012, Nevada.
- MCCULLOCH, W. S.; PITTS, W. A logical calculus of the ideas immanent in nervous activity. *Bulletin of Mathematical Biology*, v. 52, nº 1/2, p. 99–115, 1990.
- MUSSA, A. *Inteligência artificial: mitos e verdades*. São Paulo: Saint Paul, 2020. (E-book).
- NUNES, S. *Banco de dados relacional e big data*. Valinhos: Sérgio Nunes, 2016.
- REZENDE, S. O. *Sistemas inteligentes: fundamentos e aplicações*. Barueri: Manole, 2003.
- SCHMIDHUBER, J. Deep learning in neural networks: an overview. *Neural Networks*, v. 61, p. 85–117, 2015.
- SCHREIBER, G. et al. *Knowledge engineering and management: the commonkads methodology*. Cambridge: MIT Press, 2000.

**Leitura recomendada (do livro):** DAVENPORT, H. T. *Big data at work: dispelling the myths, uncovering the opportunities*. Cambridge: Harvard Business Review, 2014.

**Conexões com a disciplina anterior (Aquisição e Preparação de Dados — 262GGR6046A):**
- Dificuldades de qualidade de dados (ruído, inconsistência, redundância, incompletude) ↔ Aula 4 (AED): missing values, outliers, conflitos semânticos/estruturais no ETL.
- Normalização de dados: já detalhada na Aula 3 daquela disciplina (Min-Max, Z-Score, Escala Decimal, Robust Scaler) — não repetida aqui por decisão da Dani.

**Conexão interna à disciplina:** PCA e Análise Fatorial (redução de dimensionalidade, tratadas na Aula 3) e ML não supervisionado (agrupamento, associação, sumarização, detecção de anomalias) são pilares centrais desta disciplina e devem aparecer novamente em aulas futuras com mais profundidade técnica/prática.
