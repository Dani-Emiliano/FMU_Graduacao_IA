# AULA 04 — Migração de bancos relacionais para NoSQL e Motores de busca (*search engines*)

## 1. Identificação e objetivos

| Item | Informação |
|------|------------|
| **Disciplina** | Banco de Dados Não Relacional (262GGR6387A) |
| **Curso** | Graduação em Inteligência Artificial — FMU |
| **Aula / Unidade** | Aula 04 (Unidade 4) |
| **Tema** | (1) Motivos, etapas, processos e métodos de **migração** de bancos relacionais para NoSQL; (2) **motores de busca**: definição, funcionamento, tipos e a relação com NoSQL e indexação (ElasticSearch) |
| **Material acadêmico** | Apresentação da unidade; Infográfico *Migrações de bases relacionais para bases NoSQL*; capítulo *Migrações de bases relacionais para bases NoSQL* (BEZERRA, W. R. — *Banco de dados não relacional*, SAGAH); Dica do Professor e Saiba mais (migrações); Infográfico *Motores de busca (search engines)*; capítulo *Motores de busca (search engines)* (PEREIRA, M. A. — *Banco de dados não relacional*, SAGAH); Dica do Professor (Amazon A9) e Saiba mais (motores de busca) |

### Objetivos de aprendizagem (da Unidade)
- Identificar os motivos e as etapas da migração de bancos relacionais para NoSQL.
- Descrever os principais métodos de migração.
- Explicar o funcionamento dos motores de busca.
- Relacionar bancos NoSQL aos processos de indexação e recuperação de informações.

### Objetivos dos capítulos
- *Migrações:* definir os motivos da migração; especificar os passos necessários; descrever os métodos existentes.
- *Motores de busca:* definir o motor de busca e seu funcionamento; classificar os motores quanto à fonte dos dados; relacionar o uso de NoSQL com a indexação dos motores de busca.

> **Nota de contexto:** a Aula 01 mostrou *o que* é NoSQL; a Aula 02, o relacional e os índices; a Aula 03, *como* o dado é distribuído (replicação e *sharding*). A Aula 04 trata de dois problemas práticos: **como sair do relacional para o NoSQL** (migração) e **como encontrar informação em grandes volumes** (motores de busca, em que o NoSQL é a base da indexação).

---

## 2. Resumo e contextualização

O crescimento do volume e da variedade de dados exige soluções mais flexíveis e escaláveis. A unidade tem dois blocos independentes, ligados pela ideia de que o NoSQL resolve problemas que o relacional enfrenta em larga escala.

| Bloco | Pergunta que responde | Ideia central |
|-------|----------------------|---------------|
| **A. Migração** | Por que, como e com que método levar os dados de um banco relacional para um NoSQL? | A migração exige **planejamento** (organizacional e técnico), muda a **mentalidade** e o **código das aplicações**, e segue **fases** (pré-migração → fases → pós-migração) por um de **três métodos** |
| **B. Motores de busca** | Como um motor encontra e ordena resultados a partir de palavras-chave? | **Rastrear → indexar → consultar → ranquear por relevância**; o NoSQL (em especial o **ElasticSearch**, baseado em Apache Lucene, com **índice invertido**) sustenta a indexação em grande volume |

---

## 3. Conceitos fundamentais e explicações

# PARTE A — MIGRAÇÃO DE BASES RELACIONAIS PARA NoSQL

### 3.1 Motivos para migrar (Bezerra)

**Ponto de partida do material:** os bancos NoSQL **não surgiram para substituir** os relacionais, e sim para oferecer uma **alternativa** flexível, fluida, de alto desempenho e robusta. Uma empresa pode usar **os dois**, em uma **arquitetura híbrida**, para aproveitar o melhor de cada conceito.

**Por que, mesmo assim, migrar?**
- **Larga escala (Frozza *et al.*, 2018):** o relacional pode ter limitações em **alta concorrência** de leitura e escrita, em **disponibilidade** e em **velocidade de acesso/armazenamento de *big data***. Efeitos: **rigidez** na manipulação (por ser estruturado) e **lentidão** nas consultas.
- **Dados variados:** aplicações geram dados de estruturas, formatos e tamanhos diferentes. Em uma rede social, os dados são em geral **não estruturados** (textos, imagens, vídeos), e é praticamente impossível coletá-los e armazená-los em um banco tradicional.
- **Aderência à web (Machado *et al.*, 2019):** o NoSQL se ajusta melhor a ambientes web e visa superar problemas do modelo relacional.
- **Disponibilidade durante a migração (Sadalage e Fowler, 2013):** migrar entre SGBDs **relacionais** com grandes volumes é complexo, porque **manter os dados disponíveis** durante a migração é praticamente impossível (a movimentação pode **bloquear tabelas**).

**Quadro 1 do material — motivos para a migração**

| Motivo | Definição |
|--------|-----------|
| **Desenvolvimento de novas aplicações** | Construção de aplicações com base em outros modelos e estruturas de dados |
| **Atualização de aplicações existentes** | Necessidade de levar aplicações já existentes a modelos mais flexíveis de armazenamento e processamento |
| **Integração entre sistemas** | Fusão de sistemas de arquiteturas diversas, com bases de estruturas diferentes que precisam se comunicar |

### 3.2 Riscos da migração (Bezerra)

| Risco | O que é | Mitigação citada |
|-------|---------|------------------|
| **Perda de informação** | Dados perdidos durante o processo | Planejamento adequado; recuperação por *backup* |
| **Problemas de compatibilidade** | Incompatibilidade com outros sistemas operacionais ou extensões/formatos não suportados pelo NoSQL | Levantamento de requisitos **antes** da migração |
| **Falhas catastróficas** | Erros de *software* não previstos; mais tempo de inatividade do SGBD ou perda de dados | Controle do ambiente de ponta a ponta |

**Impacto nas aplicações:** em uma migração (relacional → NoSQL, "e vice-versa"), as aplicações (*web*, *mobile*, *desktop*) precisam ter o **código-fonte alterado**, tanto na **forma de comunicação** com o novo SGBD quanto na **forma de gravar e ler** os dados.

### 3.3 Os maiores desafios da migração (Infográfico)

| Desafio | Natureza | O que diz o infográfico | O que fazer |
|---------|----------|-------------------------|-------------|
| **Mentalidade relacional** | Humano | NoSQL armazena de forma diferente; muitos desenvolvedores aplicam conceitos relacionais no NoSQL e geram falhas e erros | Focar em **como a aplicação interage com os dados**, não em linhas ou muitas tabelas |
| **Relacionamentos existem no NoSQL** | Humano/técnico | Muitos acreditam que as entidades perdem seus relacionamentos; "em partes" é verdade, mas em bancos **orientados a documentos** podem existir relacionamentos, inclusive de forma mais simples, **como no RavenDB** | Aprender a modelar relacionamentos no modelo do banco de destino |
| ***Stored procedures* não existem** | Técnico | Não há procedimentos armazenados em NoSQL | **Mover a lógica para a aplicação**, e não para o banco; rever a lógica dos sistemas |
| ***Triggers* não existem** | Técnico | Gatilhos também não existem; o RavenDB tem recurso parecido, as ***Subscriptions*** (assinaturas), que permitem monitorar alterações em qualquer documento | Tratar na aplicação ou usar recurso equivalente do banco escolhido |

Conclusão do infográfico: os desafios podem ser superados se o **planejamento ocorrer antes da migração**.

### 3.4 Passos para uma migração assertiva (Bezerra)

**Ideia de base (Pulgatti, 2017):** o NoSQL não tem esquema definido; a **semântica** (significado) dos dados fica a cargo do **desenvolvedor**, e não do SGBD. O programador deve organizar os dados no destino para que sejam **interpretados da mesma forma** que no relacional. Esses passos devem ser considerados **antes** de iniciar a mudança.

**A) Ponto de vista organizacional (Quadro 2)**

| Passo | Definição |
|-------|-----------|
| **Orçamento** | Recursos financeiros dedicados à migração, inclusive para contratar mão de obra especializada |
| **Estratégia** | Levantamento de requisitos (prioridades) e planejamento do **cronograma** |
| **Usuários** | Participação ativa dos usuários finais: definem e esclarecem regras de negócio, ampliam a visão sobre quais dados priorizar e revelam o que esperam (desempenho? flexibilidade? capacidade de armazenamento?) |

**B) Ponto de vista técnico**

| Passo | O que fazer |
|-------|-------------|
| **Auditoria** | Auditar o banco de origem para achar dados **obsoletos** ou campos **não usados** que podem ser ignorados; verificar se a **capacidade** do destino atende à expectativa |
| ***Backup*** | Copiar **antes** de iniciar a migração ou de manipulações agressivas; permite restaurar em caso de falha |
| **Validação dos dados** | Verificar a **integridade** na origem e no destino durante e após a migração |
| **Testes** | Medir a **performance** do novo SGBD **após** a migração; só ao fim dos testes desativar o banco anterior |
| **Mapeamento de tipos de dados** | Conhecer os tipos envolvidos; verificar **metadados** na origem; converter para tipo correspondente no destino. Se não houver equivalente, converter na origem, converter durante a migração ou, junto com a equipe de desenvolvimento, **excluir** o dado se for pouco relevante |
| **Caracteres** | Cuidar da codificação: caractere incompatível causa erro ou perda de dados e pode inviabilizar a conclusão |
| **Modelagem de dados** | No relacional, a regra simples é o **relacionamento entre entidades**; no NoSQL **não há padrão único** (depende do tipo de banco). Em bancos orientados a documentos (MongoDB, CouchDB): formato semiestruturado **JSON** ou **BSON** (JSON binário); **documento** = arquivo JSON; **coleção** = conjunto de documentos; documentos têm **atributos** com valores. Em uma migração, **tabela (relacional) → coleção (NoSQL)** |
| **Falhas na migração** | Prever desconexão de rede ou problemas de gravação nos servidores; controlar o ambiente de ponta a ponta |

> **Fique atento (do material):** outros tipos de NoSQL também são usados em migrações (chave/valor, colunas, grafos, entre outros) e a modelagem deve respeitar a estrutura de cada um (ver **Aula 01 §3.6**).

### 3.5 Etapas e processos da migração (Quadros 3 e 4)

**Quadro 3 — etapas**

| Fase | Descrição |
|------|-----------|
| **Pré-migração** | Fase preparatória, no SGBD de origem; organiza todas as informações sobre os dados a migrar |
| **Fases 1 a 5** | Processos executados conforme o projeto; podem ser **mais** (> 5) ou **menos** (< 5) fases, e os processos variam de projeto para projeto |
| **Pós-migração** | Fase final: dados já transferidos ao NoSQL; os dados do destino são **comparados** aos da origem para verificar a integridade |

**Quadro 4 — processos (glossário da migração)**

| Item | Definição |
|------|-----------|
| **Origem** | SGBD relacional de onde os dados saem |
| **Destino** | SGBD NoSQL para onde os dados vão |
| **EI (extração inicial)** | Extração inicial dos dados da base relacional (origem) |
| **Arquivos** | Dados extraídos da origem **já no formato aceito** pelo NoSQL |
| **Coletor (C1)** | Comunicação entre os servidores de origem e destino, monitorada pelo *software* de migração |
| **EO (extração *on-line*)** | Extração das **operações de manipulação e definição de dados** ocorridas na origem e envio ao destino |
| **RI (replicação inicial)** | Replica no destino as informações extraídas pelo EI |
| **RO (replicação *on-line*)** | Replica as informações extraídas pelo EO, mantendo-se *on-line* enquanto ocorre a sincronização |
| **Exportação para CSV** | Gravação e envio dos dados em CSV (*comma separated values*) da origem ao destino (etapa ***off-line***) |
| **Importação do CSV** | Leitura do CSV no servidor de destino (etapa ***off-line***) |

### 3.6 Métodos de migração (Bezerra, com base em Oliveira, 2017)

Existem dois tipos de método, ***on-line*** e ***off-line***, com variações. O capítulo detalha **três**:

**Método 1 — Migração *on-line* com sincronização contínua (Quadro 5)**
A aplicação **permanece conectada ao SGBD de origem, com sincronia total**, durante a transferência. Só é conectada à nova estrutura **quando a migração termina**. Exige conhecimento avançado de programação (os mecanismos de conexão mudam de um SGBD para outro). Quando necessário, pode haver desconexão para testes.

| Etapa | O que acontece |
|-------|----------------|
| Pré-migração | Aplicação e dados no banco relacional |
| Fase 1 | Aplicação em execução; **EI** dos dados |
| Fase 2 | Aplicação em execução; **RI** no servidor de destino |
| Fase 3 | Aplicação em execução; **EO** dos dados |
| Fase 4 | Aplicação em execução; **RO** dos dados |
| Pós-migração | Aplicação e dados no banco NoSQL |

**Método 2 — Migração *off-line* por meio de uma ferramenta (Quadro 6)**
A aplicação **não está em execução**; a transferência é controlada por um *software* de migração. **Exemplo do material:** **Oracle GoldenGate**, que faz **replicação heterogênea**: entre SGBDs de versões diferentes, sistemas operacionais distintos e até estruturas diferentes (como NoSQL). A Figura 2 do material mostra origens (Oracle, MySQL, SQL Server, IBM DB2, Informix, SAP Sybase, Tandem, JMS, Cassandra) e destinos (DBMS, nuvem, Big Data, NoSQL — como Kafka, MongoDB, ElasticSearch, HBase — e *streams*).

| Pré-migração | Fase 1 | Fase 2 | Pós-migração |
|--------------|--------|--------|--------------|
| Aplicação e dados no relacional | **EI** no servidor de origem | **RI** no servidor de destino | Aplicação e dados no NoSQL |

**Método 3 — Migração *off-line* manual por meio de *scripts* (Quadro 7)**
Processo **manual**, feito por um especialista que levanta quais dados extrair, o **formato** em que serão gravados e enviados e como será o **carregamento** no destino.

| Pré-migração | Fase 1 | Fase 2 | Pós-migração |
|--------------|--------|--------|--------------|
| Aplicação e dados no relacional | **Gerar arquivo CSV** para enviar ao destino | **Ler o arquivo CSV** no destino | Aplicação e dados no NoSQL |

**Quadro-síntese dos três métodos** *(organização de estudo a partir dos Quadros 4 a 7; a coluna "Quando usar" é complementação)*

| Critério | *On-line* com sincronização contínua | *Off-line* por ferramenta | *Off-line* manual (*scripts*/CSV) |
|----------|--------------------------------------|---------------------------|-----------------------------------|
| **Aplicação durante a migração** | Em execução, ligada à origem | Parada | Parada |
| **Processos usados** | EI → RI → EO → RO | EI → RI | Exportação CSV → Importação CSV |
| **Quem controla** | *Software* de migração (coletor C1) *(interpretação de estudo)* | *Software* de migração | Especialista (*scripts*) |
| **Nº de fases (material)** | 4 | 2 | 2 |
| **Exige** | Programação avançada | Ferramenta adequada (ex.: GoldenGate) | Conhecimento do formato e da carga |
| **Quando usar** *(complementação)* | Sistema que **não pode parar** | Origens/destinos **heterogêneos** e janela de parada aceitável | Volume pequeno ou médio, equipe com domínio técnico, parada tolerável |

**Conclusão do capítulo:** as migrações de relacional para NoSQL podem ocorrer de forma leve e sem complicações **desde que haja planejamento e medidas preventivas**.

> **Conexão com a Aula 03 *(complementação)*:** EI/RI/EO/RO lembram a **replicação** (cópia inicial + acompanhamento contínuo das alterações). O método *on-line* se aproxima de replicação *on-line*; os métodos *off-line*, de replicação *off-line* (Aula 03 §3.4).

---

# PARTE B — MOTORES DE BUSCA

### 3.7 O que são e como surgiram (Pereira)

**Definição:** programas desenvolvidos para **pesquisar e localizar informações relevantes** a partir de termos inseridos pelos usuários, devolvendo uma lista dos *sites* e arquivos que mais correspondem à busca (Tarakeswar e Kavitha, 2011). Podem usar **modelos probabilísticos ou booleanos** e ter diferentes **fontes de dados** e de **indexação**.

**Linha do tempo do material**

| Marco | Descrição |
|-------|-----------|
| **1945** | **Memex**, dispositivo descrito por Vannevar Bush: comprimir e armazenar informação de livros e documentos e consultá-la de forma rápida. É considerado o conceito inicial do **hipertexto/*hiperlink*** (Nyce e Kahn, 1991) |
| **Anos 1960** | **Internet**: rede de computadores interconectados (auge da Guerra Fria), para facilitar a conexão entre laboratórios; popularizada no fim dos anos 80 com o uso comercial |
| **Início dos anos 90** | **WWW** (*World Wide Web*): sistema de informação global **que funciona dentro da internet**, com interface de fácil acesso baseada em *hiperlink* |
| **1990** | **Archie**, o primeiro motor de busca, ainda na internet **pré-web**: diretório de serviço (documentos, nomes e contatos); logo substituído por motores pós-web |
| **1992** | Artigo de Berners-Lee, Cailliau e Groff já menciona ferramentas de busca que facilitem o acesso além do *hiperlink* |

**Atenção ao conceito:** **internet ≠ WWW** (a web é um sistema que roda sobre a internet).

### 3.8 Como funciona um motor de busca

O processo começa **antes** de o usuário pesquisar. O infográfico resume em **seis passos**:

| # | Passo (infográfico) | Detalhe do capítulo |
|---|---------------------|---------------------|
| 1 | Mesmo antes de ser ferramenta de busca, o motor **sonda** materiais da web e os organiza em uma espécie de **biblioteca** | **Rastreadores** (*web crawlers*, aranhas, *spiders*) detectam páginas públicas, analisam conteúdo e *links* e extraem dados para catalogar e classificar. Exemplos: **Googlebot** (Google), **Yahoo! Slurp** (Yahoo!), **Msnbot** (Microsoft) |
| 2 | O usuário insere frase ou palavras na barra, com ou sem filtros | O motor analisa o significado de cada palavra, **erros de digitação** ("mangs" → "manga"), **contexto** ("manga" da blusa ou a fruta?), se a necessidade é ampla ou específica, se o resultado deve ser **local ou global**, notícias **antigas ou recentes** (modelos linguísticos e compreensão de linguagem natural) |
| 3 | Procura as **palavras-chave** nos arquivos **indexados** nessa "biblioteca" | **Indexação** = registrar as informações e criar o **índice de pesquisa**. O rastreador analisa texto, imagens, vídeos e áudios; o índice do Google tem mais de **100 milhões de gigabytes** (material, fonte [2020?]) |
| 4 | Cálculos de **proximidade** entre o buscado e os resultados criam um *ranking* por **relevância** | Princípios gerais: **localização** da palavra-chave no arquivo e **frequência** com que aparece. Mais relevantes: termo mais vezes e no **início da página, nos *links*, subtítulos e *tags*** |
| 5 | Resultados exibidos em nova página, na ordem do *ranking* | Cada motor tem **seu próprio método de pesos**; por isso o mesmo termo gera **resultados ordenados de modo diverso** |
| 6 | O usuário acessa informações relacionadas e pode **filtrar** (ano, idioma) | — |

**Outros detalhes do material**
- **Duplicados:** os itens coletados identificam conteúdo duplicado; no Google, as "cópias" são **penalizadas**, exibidas em posição e frequência menores.
- **Atualização:** o motor faz **revisitação** das páginas para achar mudanças.
- **Vários termos:** a frase "amarelo, lápis, xícara" não faz sentido, mas o motor devolve xícaras e lápis amarelos, e muitas vezes os três itens juntos (Figura 1, Google Imagens). Isso ocorre pelo operador booleano **AND implícito** nas barras de busca.

**Operadores booleanos** (Yoshioka e Haraguchi, 2005): palavras que informam como combinar termos; além do **AND**, há **OR** e **NOT** (E, OU, NÃO). Podem ser usados explicitamente na busca avançada, em **maiúsculas**, e funcionam como **filtros** que selecionam conjuntos de documentos e modificam a classificação.

**Modelos de cálculo da relevância**

| Modelo | Como funciona | Observações do material | Quando usar *(complementação)* |
|--------|---------------|-------------------------|--------------------------------|
| **Booleano** | **Correspondência exata** entre os termos e os documentos; o documento é **relevante ou irrelevante**, sem meio-termo | O mais **antigo e simples** | Consultas que exigem filtro exato (código, número de processo, termo obrigatório) |
| **Probabilístico** | Estima a **probabilidade** de o usuário achar o documento relevante, **além da correspondência de termos** | Pode ser melhorado com **inferência bayesiana** | Buscas em linguagem natural, em que se quer **ordenar por relevância** |

**Aprendizagem bayesiana (Zhao, 2018):** método para calcular a probabilidade assumida, a partir dos **registros de visita a *sites* anteriores do usuário**, inferindo qual resultado o agradaria mais; torna o sistema **personalizado**.

> **Fique atento (do material):** **consulta** × **pesquisa**. *Consulta*: só aparecem os resultados que correspondem aos termos inseridos. *Pesquisa*: pode incluir termos opcionais e devolve resultados **ordenados por relevância**.

### 3.9 Tipos de motores de busca (Pereira)

**Quanto à indexação**

| Tipo | Como indexa | Vantagem | Limitação | Exemplo do material |
|------|-------------|----------|-----------|---------------------|
| **Por rastreador** | *Bot*/*spider* rastreia e indexa novos conteúdos. Três partes: **rastreador**, **índice** e ***software* do mecanismo** | Informação **mais atualizada** (rastreio constante) | — | **Ask** |
| **Manual** | **Atividade humana**: o dono da página define endereço, título e descrição; a submissão é **revisada por editores**; também pode vir de documentos não digitais transcritos | **Qualidade** do conteúdo melhor | Alterações só aparecem quando reenviadas manualmente, o que limita resultados recentes | Motores especializados, como os de **genealogia** |
| **Híbrido** | Combina rastreador e manual | Dados atualizados **e** curados | — | **Google Search** |

**Quadro 1 do material (comparação)**

| | Rastreador | Manual | Híbrido |
|---|:---:|:---:|:---:|
| Indexação por robôs | ✔ | | ✔ |
| Indexação manual | | ✔ | ✔ |
| Dados sempre atualizados | ✔ | | ✔ |
| Dados mais confiáveis e curados | | ✔ | ✔ |

**Quanto à fonte de dados**

| Fonte | Como funciona | Exemplo do material | Quando usar *(complementação)* |
|-------|---------------|---------------------|--------------------------------|
| **Metadados** | A maior parte dos motores da internet usa **metadados** de arquivos e *sites*: informações **sobre** os dados, em arquivos "invisíveis", incluindo palavras-chave; a indexação ocorre sobre campos bem definidos | Figura 2: `<title>`, `<meta name="description" ...>`, `<meta name="keywords" ...>` | Busca na web aberta |
| **Federados** | **Mesma pesquisa** em **vários bancos, *sites* e repositórios**, usando a indexação **já existente em cada um**; a busca é **paralela** e os resultados são **mesclados** antes de exibir ("pesquisa federada", Melton e Buxton, 2011) | **Google Scholar** | Reunir fontes independentes sem reindexar tudo |
| **Por *desktop*** | Fonte **não relacionada à internet**: busca na **própria máquina** (arquivos, músicas, filmes, textos). Faz busca e indexação de forma **contínua**, mantendo o índice atualizado; coleta nome do arquivo, caminho, metadados e conteúdo | **Windows Search** | Achar arquivos entre centenas de pastas |

### 3.10 A importância do NoSQL para motores de busca (Pereira)

**Por quê?** NoSQL ("*not only SQL*", "não apenas SQL") não segue a linguagem estruturada, o que facilita guardar **grandes volumes** com **alta escalabilidade** e **disponibilidade** (Hiriyannaiah *et al.*, 2018). Por isso é ideal "por trás" de um motor: armazena o volume crescente de informações da indexação e facilita os resultados conforme os critérios. Exemplos citados: **Apache Lucene, Apache Solr e ElasticSearch** (McCreary e Kelly, 2014).

**Estratégias que o NoSQL usa para tornar a busca eficaz**

| Estratégia | O que é | Quando usar *(complementação)* |
|------------|---------|--------------------------------|
| **Índice de intervalo** | Indexa todos os valores de cada item em **ordem crescente** | **Palavras-chave alfabéticas** e **datas** (o material), p. ex. busca por período |
| **Índice reverso (invertido)** | Para **cada palavra** da coleção, a **lista de documentos** que a contêm | Acelerar busca de documentos por **palavra-chave** |
| **Classificação por relevância** | Calcula a probabilidade de a página corresponder ao que se procura (quantidade de palavras-chave, tipo de documento, avaliação de conteúdos etc.) | Ordenar os resultados |

**ElasticSearch (Elastic, c2020)**

| Característica | Descrição do material |
|----------------|-----------------------|
| Natureza | Motor de pesquisa **orientado a documentos**, **gratuito** e de **código aberto**, baseado no **Apache Lucene** |
| Armazenamento | Dados armazenados **centralmente**; busca rápida; cálculo de relevância com ajuste fino e analítico; fácil de ampliar |
| Usos | Busca em aplicativos e *websites*, buscas empresariais, análise e monitoramento de dados; aceita dados de **diferentes tipos e fontes** |
| Indexação | Após a análise dos dados brutos, os dados são salvos em **documentos JSON**; o **índice** é o conjunto de documentos relacionados; cada documento tem **chaves** (nomes de campos) ligadas a **valores**. A estratégia é o **índice invertido**, que torna os dados "buscáveis" praticamente em **tempo real** |
| Distribuição | Sistema distribuído: índices divididos em ***shards*** (partições), que podem ser **replicados**; maior tolerância a falhas, pois é possível recuperar índices em outras partições se a principal falhar |
| Recursos | **Facetagem** e **percolação** |
| Implantação | Serviços consolidados (**ElasticSearch Service** na AWS, no Google Cloud Platform e no Alibaba Cloud) ou *download* e instalação no próprio *hardware*/nuvem |
| Aplicações derivadas | Mais de 10; **Elastic App Search** (APIs e painéis; tolerância a erros de digitação; calibrar relevância com sinônimos; reordenar resultados; pesos distintos) e **Elastic Site Search** (busca avançada em *sites*; rastreador sem manutenção; usado por SurveyMonkey e Shopify) |

> **Saiba mais (do material) — percolação:** método de pesquisa **reverso**: em vez de devolver todos os **documentos** que correspondem ao que foi pesquisado, devolve todas as **pesquisas já armazenadas** que correspondem a um documento. Útil para notificar quando um novo documento corresponde a uma consulta registrada.

> Ver **Aula 03 §3.9–3.11** (*shards*, réplicas e *clusters*): o ElasticSearch aplica essas ideias ao índice de busca. Ver **Aula 02 §3.7** (índices): o índice invertido é outro tipo de estrutura de apoio à busca, voltado a **texto**.

---

## 4. Exemplos, aplicações e material prático

### 4.1 Casos e exemplos citados no material
- **Rede social:** dados não estruturados que o relacional tradicional não comporta bem (motivo de migração).
- **Oracle GoldenGate:** replicação heterogênea para migração *off-line* por ferramenta (origens relacionais → NoSQL, nuvem, *big data*, *streams*).
- **RavenDB:** relacionamentos entre documentos e *Subscriptions* como substituto de *triggers*.
- **MongoDB e CouchDB:** modelo de documentos JSON/BSON; tabela → coleção.
- **Busca "amarelo, lápis, xícara":** AND implícito no Google Imagens.
- **Busca "manga":** ambiguidade resolvida pelo contexto; "mangs" corrigido para "manga".
- **Google Search** (híbrido), **Ask** (rastreador), **Google Scholar** (federado), **Windows Search** (*desktop*), motores de **genealogia** (manual).
- **ElasticSearch** em SurveyMonkey e Shopify (Elastic Site Search).
- **Dica do Professor:** o motor **A9 da Amazon** é focado em **qual produto é mais atraente ao cliente**, e não apenas em quais resultados correspondem à pesquisa (descrição do próprio PDF; vídeo/QR não acessado).

### 4.2 Exemplo de migração: tabela `pessoa` → coleção *(complementação — exemplo ilustrativo elaborado para estudo; reutiliza a tabela hipotética da Aula 02; não faz parte do material da FMU)*

**Origem (relacional):**

| id | nome | idade | endereço | estudo | sexo |
|----|------|-------|----------|--------|------|
| 1 | Carla | 41 | Rua das Flores, 120 | Superior | F |

**Destino (documento JSON em uma coleção `pessoa`):**

```json
{
  "_id": 1,
  "nome": "Carla",
  "idade": 41,
  "endereco": "Rua das Flores, 120",
  "estudo": "Superior",
  "sexo": "F"
}
```

| Conceito relacional | Equivalente no destino de documentos (segundo o material) |
|---------------------|------------------------------------------------------------|
| Tabela | **Coleção** |
| Linha | **Documento** (JSON/BSON) |
| Coluna | **Atributo** do documento |

Passos do material aplicados ao exemplo: **auditoria** (a coluna `estudo` é usada?), **backup**, **mapeamento de tipos** (inteiro → número; texto → *string*), **caracteres** (acentos em "Superior"/"endereço" e a codificação), **modelagem** (manter `endereco` embutido ou separar em outro documento?), **validação** (comparar contagem e amostras origem × destino) e **testes** de desempenho.

### 4.3 Exemplo de índice invertido *(complementação — exemplo ilustrativo elaborado para estudo)*

**Documentos:** D1 = "xícara amarelo"; D2 = "lápis amarelo"; D3 = "xícara lápis".

| Palavra | Documentos (índice invertido) |
|---------|-------------------------------|
| amarelo | D1, D2 |
| lápis | D2, D3 |
| xícara | D1, D3 |

| Consulta | Operação sobre as listas | Resultado |
|----------|--------------------------|-----------|
| `amarelo AND lápis` | {D1, D2} ∩ {D2, D3} | **D2** |
| `amarelo OR lápis` | {D1, D2} ∪ {D2, D3} | **D1, D2, D3** |
| `amarelo AND NOT xícara` | {D1, D2} − {D1, D3} | **D2** |

Sem índice, o motor teria de **ler todos os documentos** a cada busca; com ele, vai direto à lista da palavra. *(Ver Aula 02 §3.7: mesma ideia de "sumário que aponta para o dado".)*

### 4.4 Cenários de aplicação *(complementação — exemplos ilustrativos elaborados para estudo; não fazem parte do material da FMU)*

- **Imagine que você tem este problema:** um sistema de pedidos que **não pode ficar parado** e precisa migrar para um banco de documentos. **Será analisado pelo método:** migração ***on-line* com sincronização contínua**, **porque** a aplicação segue ligada à origem enquanto EI, RI, EO e RO copiam e sincronizam os dados.
- **Imagine que você tem este problema:** um cadastro pequeno, usado só em horário comercial, e a equipe pode parar o sistema no fim de semana. **Será analisado pelo método:** ***off-line* manual por *scripts* (CSV)**, **porque** o volume é pequeno, a parada é tolerável e basta exportar e importar o arquivo.
- **Imagine que você tem este problema:** dados em Oracle, SQL Server e DB2 que precisam ir para MongoDB, Kafka e ElasticSearch. **Será analisado pelo método:** ***off-line* por ferramenta** (como o GoldenGate), **porque** a replicação heterogênea cobre origens e destinos diferentes.
- **Imagine que você tem este problema:** o cálculo de comissão vive em uma ***stored procedure*** no banco relacional. **Será analisado pelo desafio:** "*stored procedures* não existem", **porque**, segundo o material, a lógica deve ser movida para a aplicação.
- **Imagine que você tem este problema:** um portal com milhões de páginas e usuários que buscam por palavras e esperam o resultado ordenado. **Será analisado pela solução:** motor de busca com **índice invertido (ElasticSearch)**, **porque** ele aponta, para cada palavra, os documentos que a contêm e calcula relevância.
- **Imagine que você tem este problema:** reunir resultados de **três bases independentes** sem reindexá-las. **Será analisado pelo tipo:** motor de busca **federado**, **porque** consulta cada base com a indexação que ela já tem e mescla os resultados.
- **Imagine que você tem este problema:** achar um contrato "dentro de centenas de pastas" do seu computador. **Será analisado pelo tipo:** motor de busca por ***desktop***, **porque** a fonte é a própria máquina e o índice é atualizado continuamente.

### 4.5 Material prático
O material da Aula 4 **não traz código** (apenas quadros, figuras e o trecho de metadados HTML da Figura 2). Por isso **não há arquivo `AULA_04_..._PRATICO.md`**. Os exemplos de 4.2 e 4.3 são ilustrações de estudo.

---

## 5. Pontos de atenção (inconsistências e limitações do material)

1. **Fases do Quadro 3 × quadros 5 a 7:** o Quadro 3 fala em "Fases 1 a 5" (podendo ser mais ou menos), mas o método *on-line* tem **4 fases** e os dois *off-line* têm **2**. O número 5 é apenas ilustrativo.
2. **Coletor (C1) sem lugar nas fases:** o Quadro 4 define o coletor como a comunicação entre origem e destino, mas ele **não aparece** nos Quadros 5 a 7. A atribuição "quem controla" na síntese 3.6 é interpretação de estudo.
3. **Quadro 6 (*off-line* por ferramenta) ambíguo:** o texto diz que a transferência é "controlada por um *software* de migração, **porém os processos são executados manualmente**". Se a ferramenta controla, o que é manual? Não fica claro. Além disso, o método usa só EI e RI, sem EO/RO, embora o texto diga que "se assemelha ao *on-line*".
4. **Método *on-line*: "conectada à nova estrutura somente ao final" × "desconexão para testes":** o capítulo não explica como a aplicação é testada contra o destino sem se desconectar da origem, nem como as **escritas feitas durante a migração** são aplicadas (o papel de EO/RO é só sugerido).
5. **"Migração relacional → relacional é praticamente impossível manter disponível" (Sadalage e Fowler):** a afirmação é forte e fica em tensão com o método *on-line*, que o próprio capítulo apresenta como forma de manter a aplicação em execução. O material não explica por que isso seria viável só no NoSQL.
6. **"Podem ocorrer de maneira leve e sem complicações" (conclusão):** contrasta com os riscos (perda de dados, falhas catastróficas) e com os desafios do infográfico. A leitura prudente é "**se** houver planejamento".
7. **"E vice-versa":** o capítulo cita a migração NoSQL → relacional uma única vez e não a desenvolve.
8. **Infográfico: "*stored procedures* e *triggers* não existem em NoSQL":** é generalização do material. *Complementação (conferir na documentação de cada SGBD):* alguns bancos NoSQL oferecem recursos semelhantes, como *triggers* no Cassandra e *scripts* no servidor (Lua) no Redis. O próprio infográfico cita as *Subscriptions* do RavenDB como equivalente a *triggers*.
9. **"Relacionamentos existem no NoSQL — em partes isso é verdade":** a frase é vaga e o único exemplo é o RavenDB. O material não mostra como os relacionamentos são representados (documentos embutidos × referências).
10. **Mapeamento de tipos:** o capítulo orienta converter ou excluir dados sem equivalente, mas não dá exemplos concretos de tipos (ex.: datas, decimais).
11. **Lucene, Solr e ElasticSearch como "NoSQL":** *Complementação (conferir):* o Lucene é uma **biblioteca** de indexação e busca, e Solr e ElasticSearch são servidores de busca construídos sobre ela. Enquadrá-los como NoSQL (orientado a documentos) é a classificação do material; na prática, o ElasticSearch é muito usado **ao lado** de outro banco, e não como único repositório.
12. **"NoSQL não segue a linguagem estruturada":** simplificação. Vários bancos NoSQL têm linguagens de consulta próprias (algumas parecidas com SQL).
13. **ElasticSearch: "maior consistência... maior tolerância a falhas" por dividir em *shards* replicados:** a tolerância a falhas vem principalmente das **réplicas**; o *sharding* divide a carga (ver Aula 03 §3.13). A frase mistura os dois conceitos.
14. **Consulta × pesquisa:** a distinção do "Fique atento" é do material; não é a definição usual (em geral "consulta" e "pesquisa" são sinônimos, e a diferença aqui parece ligada ao modo de busca do ElasticSearch/Lucene). Usar como **definição da disciplina**.
15. **Google Search como "híbrido" e Google Scholar como "federado":** os tipos se **cruzam** (indexação × fonte de dados): um mesmo motor pode ser híbrido quanto à indexação e usar metadados como fonte. Não são categorias excludentes.
16. **Informações datadas:** o índice do Google "acima de 100 milhões de gigabytes" tem fonte "[2020?]"; os *links* têm "acesso em jun. 2020"; a Dica do Professor diz que a Amazon é "a empresa mais valiosa do mundo" (afirmação de época, não verificada aqui). Tratar como contexto histórico, não como dado atual.
17. **Atribuição do capítulo de migrações:** o PDF principal e o arquivo avulso ("BD_Não_relacional") trazem o **mesmo** capítulo (Bezerra); o mesmo vale para o capítulo de motores de busca (Pereira). Não há conteúdo diferente entre as cópias.
18. **Materiais complementares não acessados:** os **QR codes** (infográficos, Dicas do Professor, Saiba mais) **não foram abertos**; usei apenas os títulos e descrições do PDF (lista na seção 6). O conteúdo interativo do livro "Recuperação de informação" (cap. 6, *Linguagens de consulta*) também não estava disponível.
19. **Atividade 4 (A4):** o PDF inclui a atividade; por padrão do projeto, ela **não** foi incorporada a este arquivo.

---

## 6. Referências e conexões

### Conexões com as Aulas 01, 02 e 03 *(complementação — conceitos explicados antes; aqui apenas ponteiros)*

| Tema desta aula | Onde foi visto | O que acrescenta agora |
|-----------------|----------------|------------------------|
| Por que o NoSQL (volume, variedade, escalabilidade) | **Aula 01 §3.2, §3.4 e §3.8** | Vira **motivo de migração** (Quadro 1) |
| Tipos de NoSQL (documentos, chave/valor, colunas, grafos) | **Aula 01 §3.6 e §3.7** | A **modelagem** na migração depende do tipo; foco em documentos (JSON/BSON, MongoDB, CouchDB) |
| Modelo relacional (tabelas, linhas, colunas) | **Aula 01 §3.1; Aula 02** | Tabela → coleção; linha → documento; coluna → atributo |
| BASE × ACID, SQL × NoSQL | **Aula 01 §3.5 e §3.8** | Explica a "mentalidade relacional" como desafio |
| Índices (B-*tree*, hash, primário/secundário) | **Aula 02 §3.7, Anexos A e B** | **Índice invertido** e **índice de intervalo** como estruturas de busca |
| Replicação (passiva/ativa; *on-line*/*off-line*; síncrona/assíncrona) | **Aula 03 §3.4–3.7** | EI/RI/EO/RO de migração têm lógica de replicação |
| *Sharding*, *shards* e réplicas; *clusters* | **Aula 03 §3.9–3.13** | O ElasticSearch divide o **índice** em *shards* replicados |
| Cassandra e MongoDB | **Aula 03 §3.14–3.16** | MongoDB é o destino citado na migração (documentos JSON/BSON) e o ElasticSearch também é orientado a documentos |

**Dependência de ideias:** motivos e riscos (3.1–3.2) → desafios e passos (3.3–3.4) → etapas e processos (3.5) → métodos (3.6). Em paralelo: busca e relevância (3.7–3.8) → tipos (3.9) → NoSQL como base da indexação (3.10).

### Aplicação profissional *(complementação)*
- **Arquitetura de dados e *cloud*:** a escolha do método de migração é função de **janela de parada, volume, heterogeneidade e orçamento**; serviços gerenciados de busca (ElasticSearch em AWS/GCP) aparecem em desenhos de arquitetura.
- **Governança:** os passos organizacionais (orçamento, estratégia, usuários) correspondem a escopo, cronograma e envolvimento de partes interessadas em um projeto de migração.
- **IA/ML:** recuperação de informação e relevância (probabilística, bayesiana, personalização) são a base de sistemas de recomendação e de busca semântica; o rastreamento e a extração de páginas aparecem em coleta de dados para modelos.

### Referências acadêmicas (do material)

**Capítulo *Migrações de bases relacionais para bases NoSQL* (Bezerra):**
- FROZZA, A. A. *et al.* DINo: uma ferramenta para importação de dados em bancos de dados NoSQL. *In*: ERBD, 14., 2018, Rio Grande. *Anais* [...]. p. 135–138.
- MACHADO, R. *et al.* Uma aplicação para migração de dados de banco relacional para MongoDB. *In*: ERES, 3., 2019, Rio do Sul. *Anais* [...]. p. 113–120.
- OLIVEIRA, F. V. *Migração de bases de dados relacionais para NoSQL*: métodos de análise. Dissertação (Mestrado) — ISCTE-IUL, Lisboa, 2017.
- ORACLE. *GoldenGate for Big Data*. Redwood City: Oracle, 2019.
- PULGATTI, L. D. *Data migration between different data models of NoSQL databases*. Dissertação (Mestrado) — UFPR, Curitiba, 2017.
- SADALAGE, P. J.; FOWLER, M. *NoSQL essencial*: um guia conciso para o mundo emergente de persistência poliglota. São Paulo: Novatec, 2013.

**Capítulo *Motores de busca (search engines)* (Pereira):**
- BERNERS-LEE, T. J.; CAILLIAU, R.; GROFF, J.-F. The world-wide web. *Computer Networks and ISDN Systems*, v. 25, n. 4-5, p. 454-459, 1992.
- BUSH, V. As we may think. *The Atlantic Monthly*, v. 176, n. 1, p. 101-108, 1945.
- COMO funciona a pesquisa Google. *In*: GOOGLE. [2020?].
- ELASTIC. *Elasticsearch*. c2020.
- EMTAGE, A.; DEUTSCH, P. Archie: an electronic directory service for the internet. *In*: USENIX CONFERENCE, 1992, Quebec. *Anais*... p. 93-110.
- HIRIYANNAIAH, S. *et al.* Semi-structured data analysis and visualisation using NoSQL. *International Journal of Big Data Intelligence*, v. 5, n. 3, p. 133-142, 2018.
- MCCREARY, D. G.; KELLY, A. M. *Making sense of NoSQL*: a guide for managers and the rest of us. Shelter Island: Manning, 2014.
- MELTON, J.; BUXTON, S. *Querying XML*: XQuery, XPath, and SQL/XML in context. Burlington: Morgan Kaufmann, 2011.
- NYCE, J. M.; KAHN, P. (Ed.). *From memex to hypertext*: Vannevar Bush and the mind's machine. Cambridge: Academic Press, 1991.
- TARAKESWAR, K.; KAVITHA, D. Search engines: a study. *Journal of Computer Applications*, v. 4, n. 1, p. 29-33, 2011.
- WINDOWS search overview. *In*: MICROSOFT. 31 may 2018.
- YOSHIOKA, M.; HARAGUCHI, M. On a combination of probabilistic and boolean IR models for WWW document retrieval. *ACM Transactions on Asian Language Information Processing*, v. 4, n. 3, p. 340-356, 2005.
- ZHAO, Y. The application of Bayesian learning in the search engine. *Wireless Personal Communications*, v. 103, n. 2, p. 1121-1131, 2018.

### Materiais complementares indicados no PDF *(links/QR codes não acessados — apenas títulos e descrições do próprio PDF)*
- **Dica do Professor (migrações):** como se preparar para a migração de um SGBD relacional para um NoSQL, entendendo as características da migração (vídeo, via QR).
- **Saiba mais (migrações):** *VDINo* — ferramenta para importação de dados de SGBD relacional (como PostgreSQL) para MongoDB, Redis ou Cassandra; *Uma aplicação para migração de dados de banco relacional para MongoDB* — aplicação **DB2Mongo** (arquitetura, levantamento de requisitos, desenvolvimento e testes); *NoSqlayer* — *framework* de migração de relacional para NoSQL (módulos de migração e mapeamento e testes).
- **Dica do Professor (motores de busca):** o motor de busca **A9** da Amazon e sua importância para o comércio eletrônico da empresa (via QR).
- **Saiba mais (motores de busca):** *Recuperação de informação — conceitos e tecnologia das máquinas de busca* (cap. 6, *Linguagens de consulta*; conteúdo interativo na plataforma); *Como a busca do Google realmente funciona* (inclui RankBrain e Knowledge Graph); *Como fazer Scrapy com Python para iniciantes* (extração de dados de páginas com rastreio web).
- **Infográficos:** *Os maiores desafios da migração para NoSQL* e *Como funcionam os mecanismos de busca* (QR codes não acessados; o conteúdo do infográfico foi lido na própria imagem do PDF).
