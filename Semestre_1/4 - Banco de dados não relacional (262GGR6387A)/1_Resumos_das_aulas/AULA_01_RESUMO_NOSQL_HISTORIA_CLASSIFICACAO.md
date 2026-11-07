# AULA 01 — NoSQL: História, Classificação, BASE e Aplicabilidade

## 1. Identificação e objetivos

| Item | Informação |
|------|------------|
| **Disciplina** | Banco de Dados Não Relacional (262GGR6387A) |
| **Curso** | Graduação em Inteligência Artificial — FMU |
| **Aula / Unidade** | Aula 01 (Unidade 1) |
| **Tema** | Origem, evolução, tipos, modelo BASE e aplicabilidade dos bancos NoSQL |
| **Material acadêmico** | Infográfico "História dos bancos de dados não relacionais"; capítulos *História dos bancos de dados não relacionais* e *Classificação dos bancos de dados não relacionais* (BORDIN, M. — *Banco de Dados Não Relacional*, SAGAH); capítulo *Analisar e compreender a utilização do banco de dados NoSQL* (CAMPOS, J. B. — *Administração de Banco de Dados*, SAGAH); Infográficos de classificação e de tipos; Dicas do Professor; Saiba mais |

### Objetivos de aprendizagem (da Unidade)
- Descrever a origem, a evolução e os principais conceitos dos bancos NoSQL.
- Identificar os principais tipos e características dos bancos não relacionais.
- Explicar os princípios do modelo de consistência **BASE**.
- Diferenciar os modelos relacional (SQL) e não relacional (NoSQL).
- Demonstrar a aplicabilidade dos diferentes tipos de bancos NoSQL.

---

## 2. Resumo e contextualização

O crescimento da Internet, dos dispositivos móveis e das aplicações digitais fez explodir o **volume** de dados e, também, a sua **variedade** (formatos menos estruturados e mais distribuídos). Os bancos relacionais, até então dominantes, passaram a ter limitações para aplicações que exigem **grande volume, alta escalabilidade e formatos diversos**.

Os bancos **NoSQL** surgiram como resposta. A ideia central da aula é um **trade-off**: para escalar horizontalmente e ser flexível, abre-se mão de algumas garantias do modelo relacional (como o ACID forte e os joins elaborados). Daí decorrem três blocos conceituais que organizam a aula:

1. **Por que surgiram** (limitações do relacional + escala da Internet).
2. **Como funcionam** (CAP, consistência eventual, sharding, layouts de armazenamento, BASE).
3. **Qual usar** (tipos: chave/valor, documentos, grafos, colunares — e onde cada um é aplicado).

---

## 3. Conceitos fundamentais e explicações

### 3.1 Ponto de partida: o modelo relacional (referência para a comparação)

- Modelo desenvolvido por **Codd em 1970**; usa **SQL**; é o mais usado no mercado.
- **ACID** (Pritchett, 2008):

| Propriedade | Significado |
|-------------|-------------|
| **A**tomicidade | A transação executa completamente ou não executa |
| **C**onsistência | A transação leva a um estado válido; em falha, volta ao último estado válido |
| **I**solamento | Uma transação em andamento não é interferida por outras |
| **D**urabilidade | Os dados permanecem corretos mesmo se o sistema falhar ou reiniciar |

- **Integridade referencial:** chave estrangeira referencia chave primária de outra tabela (o registro referenciado existe).
- **Normalização:** evita duplicação, divide os dados em tabelas por tipo de elemento.

**Limitações apontadas (Leavitt, 2010):**
- Não foram construídos para aplicações **distribuídas**.
- **Joins** custam caro em requisitos de hardware.
- Modelo de dados limitado: pouca flexibilidade quando a estrutura **não é totalmente conhecida**.
- Escalar **horizontalmente** é difícil; a escalabilidade **vertical** (mais hardware) é tecnicamente simples, porém a mais **cara**, podendo gerar *lock-in* em hardware proprietário.

### 3.2 O que é NoSQL e origem do termo

- Meados da década de 90: com a popularização da Internet, os relacionais não acompanharam a escala das aplicações.
- **1998 — Carlo Strozzi** cria o termo "NoSQL" para um banco relacional leve, open source, **sem SQL**.
- **2009 — Eric Evans e Johan Oskarsson** usam o termo com o sentido atual (bancos não relacionais).
- Interpretações: "não SQL" (ausência da linguagem) ou **"Not Only SQL"**. Sadalage e Fowler (2019) recomendam usar apenas "NoSQL", pois até Oracle e Postgres poderiam se enquadrar na leitura "Not Only SQL".
- **Características gerais** (Sadalage e Fowler, 2019): ausência de SQL (alguns têm linguagens parecidas); em geral **open source**; feitos para rodar em **clusters**; oferecem **variações de consistência**; **sem esquema** (novas colunas livremente).
- Uma classe heterogênea: agrupada pelo problema que resolve (grandes volumes via **escalabilidade horizontal**, tipos de dados diversos, muitas vezes sem esquema definido).

### 3.3 Linha do tempo (Bordin — Cap. 1 e Quadro 1)

| Ano | Marco | Tipo |
|-----|-------|------|
| 1965 | **MultiValue** (TRW) — um dos primeiros não relacionais; atributos com lista de valores | Multivalor |
| 1970 | Modelo relacional (Codd) — contexto | — |
| 1979 | **DBM** (AT&T; Ken Thompson) — precursor de chave/valor | Chave/valor |
| 1989 | **Lotus Notes / Domino** | Documentos |
| 1991 | **Berkeley DB** (reescrita do DBM pela SleepyCat; hoje Oracle) | Chave/valor |
| 1998 | Termo **NoSQL** (Strozzi) | — |
| 2000 | **Neo4j** | Grafos |
| 2004 | **Google BigTable** (sobre o GFS) | Colunar |
| 2005 | **CouchDB** | Documentos |
| 2007 | **Amazon Dynamo**; **MongoDB** | Chave/valor; Documentos |
| 2008 | **Cassandra** (Facebook abre o código); Voldemort; Hypertable; Accumulo | Colunar / Chave/valor |
| 2009 | **Redis**; **HBase**; Riak; termo NoSQL ganha o sentido atual | — |
| 2011 | **Apache Druid** (colunar, tempo real); **Apache Giraph** (grafos) | — |
| 2016 | **Apache Kudu** (variante do BigTable) | Colunar |

**Fato-chave:** os artigos do **BigTable (Google)** e do **Dynamo (Amazon)** impulsionaram o movimento e levaram à criação de diversos bancos NoSQL. O Google também inspirou **Hadoop/HDFS** (artigos sobre **MapReduce** e **GFS**), base do *big data*.

### 3.4 Evolução das tecnologias NoSQL

**Por que abrir mão de garantias?** Lidar com muito dado de forma estável e a baixo custo significa que integridade garantida por transações e flexibilidade em índices/consultas nem sempre serão possíveis (Tiwari, 2011). Reduzir a complexidade pode ser favorável quando certas propriedades não são necessárias (Strauch, 2011). Exemplo do material: o Google processa **20 petabytes** do BigTable via MapReduce.

**Vantagens:** escalam **horizontalmente** com hardware comum (*commodity*), permitem **sharding** com esforço bem menor e sem o custo de bancos proprietários; muitas vezes eliminam ORMs, reduzindo a **incompatibilidade de impedância** (Sadalage e Fowler, 2019).

#### Teorema CAP (Eric Brewer)
Em sistemas distribuídos só é possível garantir **duas das três** propriedades:

| Letra | Propriedade | Ideia |
|-------|-------------|-------|
| **C** | Consistency | Após uma operação, todos os leitores veem a atualização imediatamente |
| **A** | Availability | O sistema permanece disponível mesmo após falha de nós/hardware/software |
| **P** | Partition tolerance | O sistema continua operando mesmo com partições na rede (ilhas de nós); também lida com entrada/saída de nós |

| Combinação | Características | Exemplos (Bordin) | Quando faz sentido *(complementação)* |
|-----------|-----------------|-------------------|--------------------|
| **CA** | Consistente e disponível; **não** tolera partição | Vertica, Greenplum | Ambientes sem partição de rede relevante (ver ponto de atenção 5.1) |
| **CP** | Consistente e tolerante a partição; **menor disponibilidade** | BigTable, Hypertable, HBase, MongoDB | Quando o dado correto importa mais que responder sempre |
| **AP** | Sempre disponível e tolerante a partição; pode haver **inconsistência** (propriedades BASE) | Voldemort, Tokyo Cabinet, CouchDB, Riak | Quando indisponibilidade é inaceitável e dados levemente desatualizados são toleráveis |

**PACELC (complemento):** em caso de **P**artição escolhe-se entre **A** e **C** (como no CAP); **E**lse (sistema funcionando normalmente) escolhe-se entre **L**atência e **C**onsistência (Golab, 2018). O próprio CAP é criticado (Kleppmann, 2015); Brewer (2012) reconhece que o modelo é mais flexível do que parece.

#### Consistência eventual
- Se não houver novas atualizações em um dado, **todas as leituras eventualmente retornarão o mesmo valor**.
- Admite ler dado inconsistente, mas garante convergência no futuro. Vantagem: sistemas de larga escala que seguem operando com falhas (parte dos usuários vê dado desatualizado por um tempo).
- Propagação geralmente **assíncrona**. Para saber qual é a escrita mais nova: *timestamp/relógio* + regra **last write wins** (exige relógios sincronizados) ou **Vector Clocks**.
- Problema: o cliente pode não ver a própria atualização. Soluções: **RYOW** (*Read Your Own Writes*) ou **consistência de sessão** (cliente associado a um único servidor).

#### Vector Clocks e protocolos Gossip
- **Vector Clocks:** controlam a dependência entre eventos causais de processos diferentes, **sem relógios sincronizados**.
- **Gossip (epidêmicos):** propagam estado entre nós; entregam só consistência eventual (cluster com *n* nós leva O(log n) rodadas), mas dão escalabilidade e evitam **SPoF** (ponto único de falha). Alternativa: **antientropia**.

#### Sharding e hash consistente
- Escalabilidade horizontal = clusterização + réplicas + **sharding** (dividir o conjunto de dados entre computadores do cluster; cada um cuida de uma parcela). Cache em memória ajuda, mas tem limites.
- Mapeamento simples: `partition = hash(o) mod n` (o = objeto, n = nº de nós). **Problema:** nós aparecem/desaparecem (falha de servidor, rede, banco), tornando dados indisponíveis.
- **Hash consistente:** cada nó recebe um **intervalo** do hash num **anel**; se um nó sai, outros assumem seu intervalo; se entra, recebe parte de outro. Clientes calculam onde o dado está **sem servidor de metadados** (diferente do GFS).
- **Nós virtuais:** cada nó real tem 1+ nós virtuais (conforme capacidade de hardware) → melhora o balanceamento.
- **Fator de replicação (r):** *r* nós físicos ficam responsáveis por cada objeto → resolve a indisponibilidade na saída de um nó.
- Entrada/saída de nós dependem de comunicação entre os nós (anúncio de chegada; detecção periódica de saída).

#### Armazenamento de dados (layouts — Tiwari, 2011)

| Layout | Como serializa | Favorece | Custo |
|--------|----------------|----------|-------|
| **Baseado em linhas** | Linhas inteiras ao fim da tabela | Acesso a vários campos de um registro numa única operação de I/O | — |
| **Colunar** | Por colunas | Operações sobre colunas (análise de dados) | Desempenho "sofrível" em operações sobre linhas |
| **Colunar com grupos de localidade** | Colunas agrupadas quando acessadas juntas | Acesso conjunto de colunas relacionadas | — |
| **Árvores LSM** (Log-Structured Merge) | Usa memória e disco de forma eficiente: dados em **Memtables**, **commit-logs** em disco, descarga periódica em **SSTables** | Leitura e escrita eficientes, com alto desempenho e segurança | — |

**Consultas:** variam de simples *lookups* de chave primária (chave/valor) a técnicas **scatter/gather** (consulta enviada a vários nós; resultados processados e devolvidos). Exemplo: **MapReduce** (Google, 2004) — função `map` nos nós + `reduce` para o resultado final. É o modelo que deu início ao movimento *big data* (Hadoop e Spark são frameworks atuais).

### 3.5 Modelo BASE × ACID

Para garantir **disponibilidade** em sistema particionado surgiram os princípios **BASE** (alternativa ao ACID).

- **Basically Available** (basic available): o sistema está sempre funcionando (suporte parcial a falhas, sem falha completa).
- **Soft state:** o estado pode mudar com o tempo, mesmo sem novas entradas.
- **Eventual consistency:** nem sempre consistente, mas **eventualmente** chegará a um estado conhecido.

**Contexto:** escalar verticalmente tem limite e gera *lock-in*; escalar horizontalmente obriga a abrir mão de garantias. Com dados particionados, é preciso garantir que a transação seja aplicada em todas as máquinas → **2PC (Two-Phase Commit)**: fase 1 pergunta se todos podem aplicar o commit; fase 2 aplica. **Desvantagem:** a disponibilidade do sistema vira o **produto** das disponibilidades individuais, reduzindo a disponibilidade total.

| ACID | BASE |
|------|------|
| Consistência forte | Consistência fraca |
| Isolamento | Foco em disponibilidade |
| Concentra-se em *commit* | Melhor esforço |
| Transações aninhadas | Respostas aproximadas |
| Disponibilidade | Mais simples e mais rápido |
| Conservador (pessimista) | Agressivo (otimista) |
| Evolução difícil | Evolução mais fácil |

*(Adaptado de Brewer, 2000.)* Definição de Oliveira (2013, citado por Campos): BASE distribui os dados em diferentes repositórios, tornando-os sempre disponíveis, **delega a consistência da transação para a aplicação**, mas garante consistência em algum momento futuro.

### 3.6 Tipos de bancos NoSQL

| Tipo | Modelo / como funciona | Pontos fortes | **Quando usar** | Exemplos |
|------|------------------------|---------------|-----------------|----------|
| **Chave/valor** | Map/dicionário: chave única → valor (binário/qualquer tipo). Interface básica: `set/put`, `get`, `delete`. Eficiência O(1). Omite joins e agregações | Altíssima escalabilidade e velocidade | Perfis, preferências, configurações, **sessões** (acesso por ID do usuário); **cache**; recomendação/anúncios em tempo real; blockchain; multimídia/objetos grandes | Dynamo, Redis, Riak, Voldemort, Tokyo Cabinet, Memcached, ArangoDB, FoundationDB |
| **Documentos** | Pares chave/valor em **documentos** (JSON, BSON, XML, YAML). Documentos diferentes na mesma coleção; índices também em **campos** do documento. Filtros, agregações, projeções | Esquema flexível | Dados com esquema variável (perfis com campos customizados), integração/migração de dados, analytics em tempo real, logging, **CMS**, catálogos, IoT, apps móveis, back-ends de jogos, visão única de dados diversos | MongoDB, CouchDB, Couchbase, CosmosDB, DocumentDB, RethinkDB, OrientDB, SimpleDB |
| **Grafos** | Teoria de grafos: entidades = **nós/vértices**; relacionamentos = **arestas** (que podem guardar informações) | Busca rápida de conexões (armazenadas, não calculadas em tempo de execução); *joins* recursivos viram **travessias** eficientes | Muitos relacionamentos: redes sociais, recomendação, **detecção de fraude**, conformidade regulatória (HIPAA, GDPR/LGPD), grafos de conhecimento, interações de genes/proteínas, cadeia de suprimentos | Neo4j, Amazon Neptune, ArangoDB, JanusGraph, OrientDB, TerminusDB |
| **Colunares** | Armazenam por **colunas**; colunas acessadas juntas formam famílias | Consultas analíticas (agregações) rápidas; reduz E/S; escala | Enormes volumes com **número variável de atributos**, séries temporais, ingestão em tempo real, features para ML | BigTable, Cassandra, HBase, Hypertable, Druid, Kudu, Scylla, ClickHouse, Accumulo |

**Fique atento (material):** a maioria dos autores trata só os quatro tipos acima, mas há quem cite também bancos de **tuplas/triplas/RDF**, **multivalor** e **orientados a objetos**. Há ainda os **multimodelo** (ArangoDB, OrientDB, FoundationDB — Quadro 1).

### 3.7 Principais bancos descritos (Bordin — Cap. 1)

| Banco | Tipo | Resumo |
|-------|------|--------|
| **DBM** (AT&T, 1979) | Chave/valor | Biblioteca com número fixo de *buckets* + hashing. Origem do Berkeley DB; inspirou Tokyo/Kyoto Cabinet e **WiredTiger** (engine do MongoDB; orientado a colunas e linhas) |
| **Neo4j** | Grafos | Open source, Java, **ACID**, linguagem de consulta (citada no material como "CQL — Cypher"), HTTP ou protocolo Bolt; versões *community* e *enterprise* (backup, alta disponibilidade) |
| **Google BigTable** (2004) | Colunar | Compressão, alta performance; depende do GFS (SSTables) e MapReduce |
| **CouchDB** (2005) | Documentos | Erlang; JSON; consultas MapReduce e API HTTP; ACID **no nível do documento**, consistência eventual, replicação |
| **Amazon Dynamo** (2007) | Chave/valor | Altamente disponível; abre mão do **isolamento**; base do S3 e DynamoDB; usa **hash consistente**, **Vector Clocks**, antientropia com **Merkle tree** e filiação via **Gossip** |
| **MongoDB** (2007) | Documentos | BSON, C++, índices completos, replicação, *failover*, **auto-sharding**; transações atômicas por documento (multi-documento desde a v4.0); **não recomendado** para aplicações altamente transacionais ou que exijam SQL |
| **Cassandra** (2008) | Colunar | Distribuído, descentralizado, **sem SPoF**, peer-to-peer, multi-data center, escala linear (mil+ nós), CQL (similar a SQL). *Keyspace* ≈ database; *column family* ≈ tabela; *row key* ≈ chave primária |
| **Redis** | Chave/valor | Em memória com persistência em disco; servidor *single-threaded*, operações atômicas, maioria O(1); cache, banco ou mensageria; replicação e sharding |
| **HBase / Hypertable** | Colunar | Baseados no BigTable. HBase: Java, depende do HDFS, open source. Hypertable: C++, não open source |
| **Apache Druid** | Colunar | Escrita de grandes volumes em tempo real + indexação para consultas em tempo real |
| **Apache Kudu** | Colunar | Compatível com Hadoop; analítico; índices (lookup aleatório); modelo parecido com relacional |
| **ScyllaDB** | Colunar | Compatível com Cassandra (Thrift e CQL), C++, maior *throughput* e menor latência |

*(O Quadro 1 completo do material está na seção 7 — Anexo.)*

### 3.8 SQL × NoSQL (Campos — Tabela 1, fonte AWS)

| Aspecto | SQL (relacional) | NoSQL |
|---------|------------------|-------|
| **Modelo de dados** | Tabelas (linhas e colunas) normalizadas; *schema* rígido | Normalmente sem *schema*; chave de partição, conjuntos de colunas ou documentos semiestruturados (JSON/XML) |
| **ACID** | Compatível com ACID | Troca algumas propriedades ACID por modelo flexível que escala horizontalmente |
| **Desempenho** | Depende do subsistema de disco; exige otimizar consultas, índices e tabelas | Função do tamanho do cluster, latência de rede e aplicação |
| **Escala** | Mais fácil **vertical** (hardware mais rápido) | **Horizontal**, com clusters de hardware de baixo custo |
| **APIs** | Consultas SQL | APIs baseadas em objetos; busca por chave/colunas/documentos |
| **Ferramentas** | Rico conjunto para desenvolvimento orientado ao banco | Ferramentas para gerenciar clusters e escalabilidade; a aplicação é a interface principal com os dados |

**Características do NoSQL (Cavalcante, 2012, citado por Campos):**
- **Escalabilidade horizontal** (ausência de bloqueios; *sharding* — possível no relacional, mas manual e complexo).
- **Ausência de esquema (schema-free):** facilita escalabilidade e disponibilidade, mas **sem garantia de integridade** como no relacional.
- **Suporte nativo a replicação.**
- **API simples** (foco em recuperar dados com eficiência).
- **Consistência eventual** (base no CAP → BASE).

**Técnicas de implementação (Campos):** **Map/Reduce** · **Consistent hashing** · **MVCC** (controle de concorrência multiversão, sem locks; leitura e escrita simultâneas) · **Vector clocks**.

### 3.9 Dados, informação, conhecimento e Big Data (Campos)

- **Dado:** forma bruta, sem semântica ("Jorge"). **Informação:** dado com significado ("Jorge é aluno"). **Conhecimento:** obtido pela extração, organização e cruzamento de informações. Conhecimento é ativo intangível das empresas.
- **Modelos de dados:** hierárquico (árvore, uma raiz), em rede (extensão do hierárquico, links), **relacional** (tabelas; o mais aceito hoje), orientado a objetos (classes). **SGBD** = ferramentas para criar/alterar estrutura e manipular dados.
- **Big Data** (Alecrim, 2013): conjuntos de dados tão amplos que exigem ferramentas especiais para encontrar, analisar e aproveitar informação em tempo hábil. Problema de **volume e variedade**. O NoSQL é infraestrutura de banco de dados do Big Data; **Hadoop/MapReduce** voltados à análise (Oliveira, 2013). Campos esclarece que **não** se trata do "fim" dos relacionais — muitas empresas continuarão usando-os.

---

## 4. Exemplos, aplicações e material prático

### 4.1 Casos reais citados no material

| Empresa | Tecnologia | Uso (conforme o material) |
|---------|------------|---------------------------|
| **Twitter** | Redis (key-value) | Cluster com +3 mil nós, 10 TB de dados, +10 milhões de consultas/s. Serviço **Nighthawk** (cache como serviço): analytics de anúncios/vídeo, mensagens diretas, tracking de conversas em mobile. Exigiu escalabilidade vertical e horizontal, elasticidade, baixa latência e alta disponibilidade |
| **Twitter** | **FlockDB** (grafos, criado por eles) | Relacionamentos entre usuários; picos de milhões de QPS, média de 30–40 mil QPS |
| **Netflix** | Cassandra (colunar) | Metadados de mídia + histórico de visualização (séries temporais). +100 milhões de usuários, +140 milhões de horas/dia; remodelaram esquema, adicionaram compactação e cache |
| **Netflix** | Apache Druid (colunar) | Ingestão de estatísticas de dispositivos para qualidade de serviço; particionado por *timestamp*; +2 milhões de eventos/s; consultas sobre +1,5 trilhão de linhas em milissegundos |
| **Globo.com** | Cassandra | Streaming (Globosat Play, Globoplay): dados binários de vídeo servidos diretamente do banco |
| **Uber** | Cassandra | Plataforma de ML **Michelangelo** (UberEATS): acesso a *features* para predições em tempo real (tempo de entrega, ranking, autocompletar) |
| **Amazon** | Dynamo → S3, DynamoDB | Origem do modelo chave/valor altamente disponível |
| **Google** | BigTable + MapReduce | 20 PB processados via MapReduce |

### 4.2 Exemplo de modelagem (do infográfico de tipos)

- **Chave/valor:** `cliente:1 → produto1=2, produto2=3`
- **Documento (JSON):** pedido com `id`, `cliente {id, nome}` e lista de `produtos [{id, nome, quantidade}]` aninhados.
- **Grafo:** *Stanley Kubrick* —**Dirigiu**→ *O Iluminado*; *Jack Nicholson* —**Atuou**→ *O Iluminado* e *Um estranho no ninho*.
- **Colunar:** linhas `ID` com famílias de colunas e **número variável de colunas** por linha (ex.: usuário com `email, nome, tel`; outro com `email, nome, tel, tel2`; outro só com `nome`).
- Exemplo do cap. 2 (Bordin): grafo de **pessoas × lugares**, com arestas "Morou" e "Viajou".

### 4.3 Cenários de aplicação *(complementação — exemplos ilustrativos elaborados para estudo; não fazem parte do material da FMU)*

> Formato: "Imagine que você tem este problema ___, será analisado por tal metodologia ___, porque ___".

| # | Problema | Tipo/metodologia | Porque |
|---|----------|------------------|--------|
| 1 | Imagine que você tem **milhões de sessões de login simultâneas** e precisa recuperar cada uma pelo ID do usuário em milissegundos | **Chave/valor (ex.: Redis)** | Acesso por chave é O(1), tudo em memória e sem joins; adequado a sessões e cache |
| 2 | Imagine que você tem **um catálogo de produtos em que cada categoria tem atributos diferentes** (um tem "voltagem", outro "tamanho") | **Documentos (ex.: MongoDB)** | Esquema flexível: cada documento pode ter campos diferentes sem *ALTER TABLE* |
| 3 | Imagine que você tem **transações financeiras e quer detectar redes de contas suspeitas ligadas entre si** | **Grafos (ex.: Neo4j)** | Relacionamentos são armazenados; encontrar conexões vira travessia, não *join* recursivo caro |
| 4 | Imagine que você tem **bilhões de eventos de telemetria por dia, com consultas por período e por coluna** | **Colunar (ex.: Cassandra/Druid)** | Particionamento por tempo, escrita em alto volume e agregações por coluna |
| 5 | Imagine que você tem **um sistema de saldo bancário que não pode mostrar valor desatualizado** | **Prefere ACID / sistema CP** | Consistência forte vale mais que disponibilidade total; BASE (consistência eventual) seria arriscado |
| 6 | Imagine que você tem **um carrinho de compras que nunca pode ficar fora do ar, mesmo com falha de nós** | **Sistema AP / BASE (estilo Dynamo)** | Disponibilidade prioritária; divergências temporárias são reconciliadas depois (Vector Clocks, *last write wins*) |

---

## 5. Pontos de atenção (inconsistências e limitações do material)

> Sinalizados conforme a regra de não alterar silenciosamente o conteúdo acadêmico.

1. **CAP — qual combinação tem ACID?** O Cap. 1 (Bordin) diz que sistemas **CP** "possuem as propriedades ACID" (e dá Vertica/Greenplum como CA). O Cap. 2 (Bordin) diz que sistemas **CA** possuem ACID e **AP**, BASE. Os dois textos divergem sobre CP/CA. Registrado como no material; vale confirmar com o professor.
2. **Cap. 3 (Campos):** a frase "as características dos bancos de dados *relacionais* são:" antecede a lista de características do **NoSQL** — aparente erro de redação. Também: "Constância" no lugar de "Consistência" (ACID); a **Tabela 2** está rotulada como "Comparativo entre SQL e NoSQL", mas descreve **tipos** de NoSQL; "bancos de dados de gráficos" refere-se a **grafos**.
3. **Sigla da linguagem do Neo4j:** o material escreve "CQL (Cypher Query Language / Linguagem de Consulta Contextual)". *Complementação:* na prática, a linguagem do Neo4j é conhecida como **Cypher**, e "CQL" costuma designar a linguagem do **Cassandra** (que o próprio material também chama de CQL). Mantida a grafia original; verificar na aula.
4. **Material não acessível:** os conteúdos por **QR code/link** (vídeos das *Dicas do Professor*, artigos do *Saiba mais*, audiodescrições) **não foram lidos**; por isso o conteúdo do vídeo sobre o Teorema CAP e o da Dica sobre BASE vs ACID não estão detalhados aqui. O texto do **infográfico da linha do tempo** é pequeno demais para leitura confiável: a linha do tempo da seção 3.3 foi montada com base no **texto do capítulo** e no Quadro 1.
5. **Atividade 1 (A1):** conforme sua preferência, as questões e respostas **não** foram incluídas neste arquivo.

---

## 6. Referências e conexões

### Conexões com conteúdos anteriores *(complementação)*
- **Aquisição e Preparação de Dados — Aula 1 (dados abertos/conectados):** bancos de **grafos** e de **tuplas/triplas/RDF** (citados aqui como tipos "extras") dialogam com o modelo **RDF/Linked Data** estudado lá.
- **Aquisição e Preparação de Dados — Aulas 2 e 4 (ETL e AED):** o **esquema flexível** do NoSQL muda o "T" do ETL (menos rigidez na carga, mais tratamento posterior); tipos colunar e de documentos são destinos comuns de dados semiestruturados antes da análise exploratória.
- **Machine learning:** o material cita Cassandra servindo *features* em tempo real (Uber/Michelangelo) e grafos para ML/recomendação.

### Aplicação profissional *(complementação)*
- O **CosmosDB (Microsoft/Azure)** aparece no Quadro 1 como banco de **documentos** proprietário (2010); o **DynamoDB** e o **DocumentDB** (Amazon) também — referência direta para decisões de arquitetura em nuvem.

### Referências acadêmicas (do material)
- BORDIN, M. *Banco de Dados Não Relacional*. SAGAH. Capítulos: *História dos bancos de dados não relacionais*; *Classificação dos bancos de dados não relacionais*.
- CAMPOS, J. B. *Administração de Banco de Dados*. SAGAH. Capítulo: *Analisar e compreender a utilização do banco de dados NoSQL*.
- Citadas nos capítulos (seleção): CODD (1970); PRITCHETT (2008) *Base: an acid alternative*; GILBERT; LYNCH (2012); BREWER (2000; 2012); GOLAB (2018) *Proving PACELC*; KLEPPMANN (2015); BAILIS; GHODSI (2013); DECANDIA et al. (2007) *Dynamo*; CHANG et al. (2008) *Bigtable*; STRAUCH (2011) *NoSQL databases*; SADALAGE; FOWLER (2019); TIWARI (2011); HECHT; JABLONSKI (2011); ALECRIM (2013); OLIVEIRA (2013); CAVALCANTE/KOKAY (2012); AWS — *O que é NoSQL?*.
- **Sugestões do professor (links não acessados):** *History repeats itself: sensible and nonsenSQL aspects of the NoSQL hoopla*; *A survey on NoSQL stores*; *Persisting big-data: the NoSQL landscape*; *Critérios para seleção de SGBD NoSQL*; *Mapeamentos conceituais entre os modelos relacional e NoSQL*; vídeo *Cassandra Serving Netflix @ Scale* (Vinay Chella, Netflix); entrevista com Eduardo Morelli (Infnet).

---

## 7. Anexo — Quadro 1: principais bancos NoSQL (Bordin, Cap. 1)

| Banco | Licença | Tipo | Ano | Criado/Mantido por |
|-------|---------|------|-----|--------------------|
| MultiValue (PICK) | Proprietário | Multivalor | 1965 | TRW |
| DBM | Proprietário | Chave/valor | 1979 | AT&T |
| Lotus Domino | Proprietário | Documentos | 1989 | Lotus |
| GDBM | Open source | Chave/valor | 1990 | GNU |
| BerkeleyDB | Open source | Chave/valor | 1991 | Sleepycat/Oracle |
| TDBM | Open source | Chave/valor | 1992 | — |
| Caché | Proprietário | Multivalor | 1997 | InterSystems |
| Metakit | Open source | Documentos | 1997 | Jean-Claude Wippler |
| Neo4j | Open source | Grafos | 2000 | Neo4j |
| db4o | Open source | Objetos | 2000 | Actian |
| Memcached | Open source | Chave/valor | 2003 | Danga Interactive |
| BigTable | Proprietário | Colunar | 2004 | Google |
| Infogrid | Open source | Grafos | 2005 | — |
| CouchDB | Open source | Documentos | 2005 | Apache |
| Tokyo Cabinet | Open source | Chave/valor | 2006 | FAL Labs |
| Dynamo | Proprietário | Chave/valor | 2007 | Amazon |
| MongoDB | Open source | Documentos | 2007 | MongoDB Inc. |
| Cassandra | Open source | Colunar | 2008 | Facebook/Apache |
| Project Voldemort | Open source | Chave/valor | 2008 | LinkedIn/Microsoft |
| Dynomite | Open source | Chave/valor | 2008 | — |
| Hypertable | Open source | Colunar | 2008 | Zevents Inc. |
| Accumulo | Open source | Colunar | 2008 | Apache |
| Terrastore | Open source | Documentos | 2009 | Sergio Bossa |
| Redis | Open source | Chave/valor | 2009 | Redis Labs |
| Riak | Open source | Chave/valor | 2009 | Basho Technologies |
| HBase | Open source | Colunar | 2009 | Apache |
| Vertexdb | Open source | Grafos | 2009 | — |
| ClickHouse | Open source | Colunar | 2009 | Yandex |
| RethinkDB | Open source | Documentos | 2009 | — |
| OrientDB | Open source | Multimodelo | 2010 | OrientDB Ltd. |
| Couchbase | Open source | Documentos | 2010 | Couchbase Inc. |
| CosmosDB | Proprietário | Documentos | 2010 | Microsoft |
| LDBM | Open source | Chave/valor | 2011 | — |
| ArangoDB | Open source | Multimodelo | 2011 | ArangoDB GmbH |
| Druid | Open source | Colunar | 2011 | Apache |
| DynamoDB | Proprietário | Chave/valor, documentos | 2012 | Amazon |
| FoundationDB | Open source | Multimodelo | 2013 | Apple |
| Scylla | Open source | Colunar | 2014 | ScyllaDB Inc. |
| Kudu | Open source | Colunar | 2016 | Cloudera/Apache |
| TerminusDB | Open source | Grafos | 2018 | — |
| Neptune | Proprietário | Grafos | 2018 | Amazon |
| DocumentDB | Proprietário | Documentos | 2019 | Amazon |

*(Observação: no Cap. 2, o texto cita o ArangoDB como exemplo de chave/valor, documentos e grafos; no Quadro 1 acima ele consta como multimodelo. Registrado como na fonte.)*
