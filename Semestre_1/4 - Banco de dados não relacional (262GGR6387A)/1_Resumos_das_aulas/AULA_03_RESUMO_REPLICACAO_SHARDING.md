# AULA 03 — Replicação e Sharding: distribuição de dados em clusters (Cassandra e MongoDB)

## 1. Identificação e objetivos

| Item | Informação |
|------|------------|
| **Disciplina** | Banco de Dados Não Relacional (262GGR6387A) |
| **Curso** | Graduação em Inteligência Artificial — FMU |
| **Aula / Unidade** | Aula 03 (Unidade 3) |
| **Tema** | Gestão da replicação (modelos, estratégias e aplicações); *sharding* (conceito, estratégias, clusters locais e remotos, comparação com índices); *sharding* no Apache Cassandra e no MongoDB |
| **Material acadêmico** | Apresentação da unidade; Infográfico *Gestão da replicação*; capítulo *Gestão da replicação* (MENGATO JUNIOR, R. C. — *Sistemas Distribuídos*, SAGAH); Infográfico *Sharding* (BigTable); capítulo *Sharding* (BRANDÃO, D. S. — *Framework de Big Data*, SAGAH) e, reenviado depois, capítulo *Sharding* (SOARES, J. A. — *Framework de Big Data*, SAGAH; ver 3.18 e 5.25); Infográfico *Sharding no Apache Cassandra*; capítulo *Frameworks que utilizam sharding como forma de distribuição* (PEREIRA, M. A. — *Framework de Big Data*, SAGAH); Dicas do Professor; Saiba mais |

### Objetivos de aprendizagem (da Unidade)
- Conceituar *sharding* e explicar sua relação com a escalabilidade horizontal.
- Descrever o uso de *sharding* em *clusters* locais e distribuídos.
- Comparar o funcionamento do *sharding* com o uso de índices.
- Identificar como o *sharding* é aplicado em tecnologias como Apache Cassandra e MongoDB.
- Descrever o papel da replicação em sistemas distribuídos.
- Analisar estratégias e situações práticas de aplicação de modelos de replicação.

> **Nota de contexto:** a Aula 01 apresentou *o que* são os bancos NoSQL e *por que* eles abrem mão de garantias (CAP, BASE). A Aula 02 voltou ao relacional (SQL e índices). A Aula 03 mostra **como** um banco cresce além de uma máquina: copiando os dados (**replicação**) e/ou dividindo os dados (***sharding***).

---

## 2. Resumo e contextualização

Com o crescimento do volume de dados e de usuários, um único servidor deixa de dar conta de armazenamento, processamento e disponibilidade. A unidade apresenta as duas técnicas centrais de distribuição:

| Técnica | Ideia em uma frase | Resolve principalmente |
|---------|--------------------|------------------------|
| **Replicação** | **Copiar** os mesmos dados em vários computadores | Disponibilidade, tolerância a falhas, desempenho de leitura |
| ***Sharding*** (fragmentação / particionamento horizontal) | **Dividir** os dados em partes (*shards*) espalhadas por vários computadores | Escalabilidade de armazenamento e de processamento (leitura e escrita) |

Os capítulos seguem esta ordem: (1) replicação em sistemas distribuídos (modelo, estratégias passiva e ativa, aplicações); (2) *sharding* (conceito, estratégias, *clusters*, comparação com índices); (3) *sharding* na prática em **Cassandra** e **MongoDB**, incluindo a diferença entre *sharding* e replicação. As duas técnicas aparecem **combinadas** nos bancos reais — ponto que a unidade destaca no final. O capítulo de *Sharding* de Soares, reenviado depois, foi integrado em **3.18**, sem substituir o conteúdo anterior.

---

## 3. Conceitos fundamentais e explicações

### 3.1 Escalar um banco: vertical × horizontal (Brandão)
Escalabilidade é a capacidade de o sistema atender ao crescimento sem perder qualidade e com aumento de custo baixo (Ferreira, 2020); também é definida como lidar de forma transparente com um número crescente de usuários simultâneos (Veras, 2016).

| Abordagem | O que é | Limites (segundo o material) | Quando usar *(complementação)* |
|-----------|---------|------------------------------|--------------------------------|
| **Vertical** | Comprar máquinas maiores, mais rápidas e mais caras (mais RAM, disco) | Trabalhosa e cara, mesmo em nuvem; **não é infinita** | Crescimento moderado, equipe pequena, aplicação difícil de distribuir |
| **Horizontal** | Adicionar mais máquinas e **particionar/redistribuir** os dados (*sharding*) | Aumenta a **complexidade operacional**: é preciso gerenciar várias máquinas ao mesmo tempo | Volume que passa do teto de uma máquina; crescimento contínuo; custo abaixo do vertical em grande escala |

O material observa que o aumento vertical funciona em grandes empresas com aporte financeiro, mas não tanto em pequenas e médias; por isso ganham destaque técnicas e sistemas de código aberto.

> Ver **Aula 01 §3.4** (escalabilidade horizontal = clusterização + réplicas + *sharding*).

---

### 3.2 Replicação: o papel em sistemas distribuídos (Mengato Junior, com base em Coulouris *et al.*, 2013)

**Definição:** manter **cópias de dados (ou de serviços)** em diferentes computadores. O exemplo cotidiano do material é o *cache* do navegador: a página está salva em uma cópia no próprio computador.

**Vantagens citadas:**

| Vantagem | Explicação do material |
|----------|------------------------|
| **Desempenho** | O cliente não precisa ir ao servidor remoto (latência de rede maior). Vale para o *cache* do navegador e para qualquer aplicação |
| **Disponibilidade** | Principal motivo do uso: serviços visam ~100% (24×7), o que só é possível com dados replicados |
| **Tolerância a falhas** | Alguns serviços precisam de comportamento rigorosamente correto mesmo com falhas. Dado **disponível** não significa dado **correto/atualizado** |

**Requisitos e dificuldades:**
- **Transparência:** o usuário não precisa saber que existem várias cópias físicas; deve receber só o que pediu.
- **Consistência:** *consistência* = qualquer consulta, em qualquer réplica, retorna o mesmo conjunto de informações (Tanenbaum e Steen, 2008). Manter várias cópias consistentes pode gerar **problema de escalabilidade**.
- **Rigidez varia por aplicação:**
  - *Rede social:* trocar a foto de perfil não precisa chegar a todos imediatamente.
  - *Controle de tráfego aéreo:* dado correto é necessário em escalas de tempo curtas.
  - *Sistema bancário:* crédito e débito replicados **exatamente nessa ordem**; se algum servidor inverter as operações, o saldo fica diferente e prejudica o usuário.
- **Complexidade:** falta de **relógio global** entre os servidores; consenso de tempo e tempos das mensagens de sincronização.
- Replicar também **rotinas** (microsserviços), não só dados.

> Ver **Aula 01 §3.4** (CAP, consistência eventual, *vector clocks*): o material trata, aqui, do mesmo dilema entre alta disponibilidade e política rígida de consistência.

---

### 3.3 Modelo básico de arquitetura da replicação (Coulouris *et al.*, Fig. 1)

| Componente | Papel |
|-----------|-------|
| **Cliente (C)** | Faz requisições de leitura ou de atualização (escrita/alteração de objeto ou arquivo) |
| ***Front-end* (FE)** | Intermediário que se comunica com um ou mais gerenciadores de réplica, **tornando o processo transparente** ao cliente |
| **Gerenciador de réplica (GR)** | Mantém as réplicas; qualquer dispositivo que sirva os dados replicados (na prática, "servidor") |

As operações de um gerenciador sobre suas réplicas devem ser **recuperáveis e atômicas (indivisíveis)**: não podem deixar a réplica inconsistente e, havendo falha, deve ser possível desfazer.

**As cinco fases de uma requisição** (Coulouris *et al.*, 2013) — cada uma pode afetar o desempenho:

| # | Fase | O que acontece |
|---|------|----------------|
| 1 | **Requisição** | O FE dispara a requisição para um ou mais gerenciadores (pode fazer *multicast* para todos e esperar resposta de alguns) |
| 2 | **Coordenação** | Os gerenciadores verificam se a requisição deve ser aplicada e em que **ordem**: FIFO, ordem causal ou ordem total |
| 3 | **Execução** | Executa de forma que possa ser **desfeita** se houver falha posterior (em um servidor ou em todos, se houve *multicast*) |
| 4 | **Acordo** | Os gerenciadores chegam a um **consenso** sobre aceitar ou cancelar |
| 5 | **Resposta** | Um ou mais gerenciadores respondem ao FE; o FE pode pegar a **primeira resposta** e descartar as outras, ou esperar todas |

Nem toda aplicação executa todas as fases. **Exemplo do material:** aplicativo de *smartphone* com dados salvos localmente para uso sem internet — o FE não consegue falar com outros gerenciadores, "pula" para execução e resposta o mais rápido possível, e **replica depois** quando o usuário voltar a ter conexão.

---

### 3.4 Classificação das estratégias de replicação (Infográfico)

| Eixo | Opção A | Opção B |
|------|---------|---------|
| **Processo** | **Ativo:** operações realizadas em **todos** os gerenciadores de réplicas | **Passivo:** cópias **primárias e secundárias**; atualização no primário e depois replicada aos demais |
| **Fluxo** | **Síncrono:** todas as cópias atualizadas em **uma única transação**; bloqueia o usuário até todos aplicarem | **Assíncrono:** **fila** de atualizações a replicar; transação mais curta, mas fica mais difícil manter ordem e evitar atrasos |
| **Direção** | **Unidirecional:** do primário para os secundários | **Bidirecional:** operações nos dois sentidos; pode haver **mais de um servidor primário** que envia e recebe atualizações |
| **Conexão** | ***On-line*:** replica a cada operação (quase nenhum atraso) | ***Off-line*:** replica a cada intervalo de tempo / quando houver conexão com o *cluster* (comum em aplicativos de *smartphone*) |

Os quatro eixos são **independentes**: uma implementação combina uma opção de cada eixo (por exemplo, passiva + assíncrona + unidirecional + *on-line*). *(Interpretação de estudo, derivada da estrutura do infográfico.)*

---

### 3.5 Replicação passiva (*backup* primário)

Também chamada de *master/slave* (primário/secundários). É a **mais comum**. O FE conversa **apenas com o gerenciador primário**, que replica as operações para os secundários. Se o primário falha, um novo é **eleito**.

**Sequência (Fig. 2):**

| Fase | Passo |
|------|-------|
| Requisição | FE → primário (pode levar um **identificador único**) |
| Coordenação | O primário verifica, pelo identificador, se a requisição já foi feita (exige **registro histórico** das requisições atendidas) |
| Execução | O primário executa e **armazena a resposta** (garante atomicidade e permite replicar a operação) |
| Acordo | Em caso de atualização, o primário manda os secundários executarem; eles **confirmam** |
| Resposta | O primário responde ao FE, que devolve ao cliente |

**Pontos de atenção do modelo (material):**
- Se o sistema é **síncrono**, a etapa de acordo pode causar **lentidão**, dependendo do nº de secundários.
- Se o primário falha, **um** *backup* assume; se mais de um assumir, causa falha no sistema. Os *backups* remanescentes precisam concordar com o novo primário e com o **histórico de execuções**.
- Para tolerar até **F falhas**, são necessários **F + 1** gerenciadores — implantação possivelmente cara.
- **Não tolera falhas bizantinas.**
- O FE tolera falhas com facilidade: ao detectar a falha, basta buscar o novo endereço do primário.
- **Sobrecarga no primário** (todas as requisições chegam a ele). **Variação:** permitir **consultas** (que não alteram dados) nos *backups*.

> *Falhas bizantinas* (quadro "Saiba mais" do material): aquelas em que os gerenciadores não conseguem concordar com uma estratégia para falhas catastróficas no processo de replicação.

---

### 3.6 Replicação ativa

Os gerenciadores são organizados em **grupos**. O FE envia a requisição a **todos** os do grupo por ***multicast*** e cada nó processa de forma **independente**, respondendo ao FE. Se alguns falharem, **não há impacto** na operação; só há erro em caso de colapso geral.

**Sequência (Fig. 3):**

| Fase | Passo |
|------|-------|
| Requisição | FE envia via *multicast* **totalmente ordenado e confiável** a todos os gerenciadores |
| Coordenação | Um sistema de comunicação em grupo entrega a requisição a cada gerenciador **na mesma ordem** |
| Execução | Todos executam a mesma requisição de forma similar → ao final, **mesmo estado** (consistência) |
| Acordo | **Não é necessário**: a distribuição total já garante a ordem |
| Resposta | Cada gerenciador responde ao FE com o identificador da requisição (os que falharam não respondem) |

**Pontos de atenção:**
- O conceito de **falha é relativo à aplicação**: pode-se considerar falha se **um** gerenciador não responder, ou só se **todos** (ou boa parte) não responderem.
- O FE pode adotar a política de **aceitar a primeira resposta** (ganho de desempenho).
- O sucesso depende de um algoritmo de *multicast* totalmente ordenado e confiável.
- Com ao menos **2F + 1** gerenciadores, o modelo suporta até **F falhas bizantinas**. Para tolerância mais rígida, pode-se **assinar digitalmente** as respostas.

### 3.7 Passiva × ativa (síntese)

| Critério | Passiva (*backup* primário) | Ativa |
|----------|-----------------------------|-------|
| Quem recebe a requisição | Só o primário | **Todos** (via *multicast*) |
| Quem executa | O primário; depois replica | **Todos**, de forma independente |
| Fase de acordo | Sim (primário → secundários, com confirmação) | Não necessária (ordem total) |
| Falha do nó principal | Exige **eleição** de novo primário | Sem impacto enquanto restarem nós |
| Nº de gerenciadores | F + 1 para F falhas (sem bizantinas) | 2F + 1 para F falhas bizantinas |
| Ponto fraco | Sobrecarga/gargalo no primário; lentidão no acordo síncrono | Depende de *multicast* ordenado e confiável (custo de coordenação) |
| **Quando usar** *(complementação)* | Maioria dos sistemas; quando se aceita uma troca de primário e se quer simplicidade | Quando **não se pode parar** nem por um instante e se aceita pagar mais recursos |

---

### 3.8 Aplicações dos modelos de replicação

**a) Microsserviços — replicar um serviço, não dados (Fig. 4).**
- **Microsserviço:** um projeto completo com **uma única funcionalidade** (ex.: enviar *e-mail* quando um evento ocorre), reutilizável e de fácil manutenção.
- No serviço de *e-mail* **não há dados a replicar**: as informações necessárias seguem na própria requisição do FE → não há problema de consistência.
- Fluxo: clientes (celular, *desktop*, *tablet*, *notebook*) → FE → **gerenciador primário (*proxy*)** → uma das instâncias do microsserviço.
- O *proxy* tem políticas de **balanceamento de carga**; se um servidor não devolve mensagem de êxito, reatribui a requisição a outro. Como o envio de *e-mail* é **assíncrono**, o cliente não fica bloqueado.
- É uma implementação do **modelo passivo**, exceto por não manter um conjunto de dados. Se o *proxy* falhar, outro é eleito. Os gerenciadores podem ser **máquinas virtuais ou contêineres**, ligados/desligados com facilidade.

**b) Arquitetura *gossip* (fofoca) — Ladin *et al.*, 1992 (Figs. 5).**
- Os gerenciadores trocam **mensagens de "fofoca" de tempos em tempos** para propagar atualizações às réplicas. Implementa replicação, consistência e sincronização.
- Dois tipos de operação: **consulta** (cliente espera o estado da réplica) e **atualização** (nada é devolvido além do identificador; só ela modifica o estado).
- O FE manda requisições a **qualquer gerenciador disponível** (não precisa ser todos nem um primário) → escolhe um que responda em tempo razoável.
- Cada cliente tem seu próprio gerenciador ou *cluster* → separação por **geolocalização** reduz a latência.

| Fase (gossip) | Como funciona |
|---------------|---------------|
| Requisição | O FE fala com um servidor; se ele falha, procura outro. Na atualização, devolve ao cliente assim que entregue ao FE; segue em **segundo plano** |
| Resposta de atualização | O gerenciador responde assim que recebe |
| Coordenação | As mensagens de fofoca são a **única** coordenação; um gerenciador só processa quando já pode aplicar (outros nós podem precisar receber atualizações antes) |
| Execução | O gerenciador executa a requisição |
| Resposta de consulta | Só para consultas |
| Acordo | Por mensagens de fofoca, de forma **"preguiçosa"** (*lazy*): não a cada requisição, e sim ocasionalmente ou quando um servidor percebe que está desatualizado |

- Consistência **causal/mais flexível**: um cliente pode acessar dado antigo em relação a outro. O modelo **não define** como propagar atualizações (varia por aplicação).
- **Exemplo — rede social:** usuário europeu com amigos europeus → dados no *cluster* da Europa. Um usuário no Brasil que veja o perfil dele pode ver informação **desatualizada**, pois o gerenciador da região não envia fofocas com tanta frequência a outros continentes. Consultas são mais frequentes que atualizações e **a disponibilidade vem antes da consistência**.
- **TAO (*The Associations and Objects*, Facebook; Bronson *et al.*, 2013):** design *master/slave* que garante consultas atendidas dentro da região, com risco de dados obsoletos.

**c) Sistemas de arquivos distribuídos.** **GFS** (Google File System) usa replicação **passiva** (cópias primárias e secundárias); **Hadoop (HDFS)** — de acordo com o material, pode fazer várias cópias de um dado (ver ponto de atenção 5.14).

**Conclusão do capítulo:** replicação permite alta disponibilidade, tolerância a falhas e confiabilidade, mas **apenas usar replicação não garante** esses requisitos — é preciso escolher o modelo adequado à aplicação.

---

### 3.9 O que é *sharding* (Brandão e Pereira)

***Sharding*** (fragmentação/particionamento horizontal) é um padrão de arquitetura de sistemas distribuídos em que a base é dividida em dois ou mais blocos menores, os ***shards***. **Cada partição tem o mesmo esquema e as mesmas colunas, mas linhas (registros) totalmente diferentes.** Juntos, os *shards* representam o conjunto lógico inteiro.

| Conceito | Definição |
|----------|-----------|
| ***Shard* lógico** | Cada fragmento lógico dos dados |
| ***Shard* físico** | Nó de banco de dados que hospeda um ou vários *shards* lógicos |
| **Banco particionado (SDB, *Sharded DataBase*)** | União dos *shards*, gerenciados coletiva ou individualmente; parece único, e o número de *shards* e a distribuição são **transparentes** para as aplicações |
| ***Shared Nothing* (SN)** | Arquitetura "nada compartilhada": sem centralização; cada fragmento é **autônomo/independente** (não compartilha dados nem recursos de computação) |
| **Chave de fragmentação (*shard key*)** | Campo(s) usado(s) para decidir em qual *shard* cada registro fica |
| **Tabelas de referência** | Em alguns casos, replica-se uma tabela pequena em **cada** *shard* (ex.: tabela de taxas de conversão), para que as consultas tenham tudo à mão — uma forma de balanço de carga |

**Características que diferem do relacional tradicional (Brandão):**
1. **Dados desnormalizados:** guardam-se juntos dados usados juntos (ex.: perfil do usuário recuperado como um todo) — abordagem muito rápida.
2. **Dados em várias instâncias físicas:** em vez de crescer só aumentando máquinas num *datacenter*, os dados são paralelos e crescem de forma **linear**; muito mais trabalho acontece em **processamento paralelo**.
3. **Dados "pequenos":** quanto maior o conjunto de dados de um servidor, mais difícil obter retorno inteligente (muita RAM para *cache*). Isolando em fragmentos menores, é **mais provável que os dados acessados permaneçam em *cache***.

**Particionamento horizontal × vertical (material):**
- **Vertical:** **colunas inteiras** são separadas e colocadas em tabelas novas/distintas.
- **Horizontal (*sharding*):** **linhas** são distribuídas entre *shards*.
- O horizontal deve **complementar** o vertical e o funcional (Pereira).

**Co-residente × remoto (Pereira):**

| Tipo | Onde ficam os *shards* | Vantagem citada |
|------|------------------------|-----------------|
| ***Coresident*** | Na **mesma** máquina | Reduz o tamanho dos **índices individuais** e a quantidade de E/S na atualização de registros |
| **Remoto** | Em máquinas **diferentes** | Aumenta a **largura de banda** de acesso (mais RAM, mais interfaces de rede e canais de E/S de disco) |

**Onde implementar:** muitas vezes **no nível do aplicativo** (o código define em qual *shard* ler/gravar); alguns sistemas de arquivos distribuídos têm *sharding* **integrado**. Também há ferramentas de terceiros:

| Ferramenta | O que é (segundo o material) |
|------------|------------------------------|
| **Hibernate Shards** | Extensão do *Hibernate Core* para encapsular a complexidade de dados particionados horizontalmente; duas áreas: **lógica de *sharding* generalizada** (consulta/transação via API do *Hibernate Core*) e **específica do aplicativo** (regras próprias de distribuição, via interfaces) |
| **Apache Slice** | *Plug-in* que estende o **OpenJPA** (Java) para armazenamento distribuído, possivelmente heterogêneo e particionado; fica entre OpenJPA e **JDBC**; os dados são "fatiados" em ***slices*** (mesma ideia dos *shards*) |
| **WebSphere ObjectGrid (IBM)** | Armazenamento de objetos Java em memória (*cache*) para escalabilidade, resiliência e alto desempenho; pode ser banco em memória ou distribuir dados pela rede; arquitetura de segurança para autenticar e autorizar clientes |

**Vantagens do escalonamento horizontal (Pereira):** ganho de desempenho, alta disponibilidade, tolerância a falhas, segurança, **paralelização** de *backup*, restauração e sincronização inicial. Bancos que usam: Cassandra, MongoDB, HBase e o sistema de arquivos HDFS (Hadoop). O custo: **gargalo é a complexidade operacional** — gerenciar várias máquinas ao mesmo tempo; funções como pesquisa de texto e análise de dados saem beneficiadas.

---

### 3.10 Estratégias de *sharding*

O material apresenta duas listas que se sobrepõem: as **três estratégias mais comuns** (Carpenter e Hewitt, 2016 — via Pereira) e as **três opções do MongoDB** (Keep e Ingo, 2020 — via Brandão).

| Estratégia | Como funciona | Vantagem | Desvantagem / cuidado | Quando usar |
|-----------|---------------|----------|----------------------|-------------|
| **Por *hash* (por chave)** | Usa valores constantes do dado para gerar um ***hash*/*token*** que identifica o *shard* | Boa **distribuição** uniforme; ótima para **operações direcionadas** e para **ingestão de *stream* de dados e dados de eventos** | O cálculo do *hash* adiciona carga; **difícil adicionar/remover servidores** dinamicamente; consultas por faixa tendem a atingir vários *shards* | Chave de acesso pontual (buscar por ID); escrita em alto volume que precisa ser espalhada |
| **Por intervalo (faixa)** | Particiona por **intervalos da chave**; dados com chaves parecidas ficam no **mesmo *shard*** | Implementação relativamente **fácil**; boa para **consultas sequenciais/por faixa** (a consulta cai em **um** *shard*); costuma ser a estratégia **padrão** | **Desequilíbrio de carga** (intervalos podem ter quantidades diferentes de itens) | Consultas por faixa (preço, idade, data) |
| **Por diretório** | Um **serviço de pesquisa estática** (mapa) diz qual *shard* guarda quais dados; o cliente consulta o serviço antes | **Flexibilidade**: qualquer sistema/algoritmo para atribuir dados; mapeamento *shard* virtual ↔ partição física muda sem alterar o código; fácil adicionar *shards* dinâmicos | Se o sistema de busca for **corrompido**, afeta gravação e acesso (ponto único de falha) | Regras de alocação complexas ou que mudam com frequência |
| **Por zona** (MongoDB) | O desenvolvedor define **regras** que orientam onde os dados ficam | Permite, por exemplo, separar dados de **filiais** em *shards* diferentes | Exige planejamento das regras | Requisitos de localização, prioridade ou privacidade de acesso |

Outras formas citadas: baseado em **colunas** (útil em bancos orientados a coluna como o HBase), ***sharding* dinâmico** (o cliente determina onde o *shard* será armazenado) e **algorítmico** (uma função aloca os dados). Pode-se ainda fragmentar por carga de trabalho, localização, prioridade e privacidade de acesso.

**Exemplos do material:**
- *Intervalo* (Fig. 2, Brandão): idade das pessoas divide a tabela em três *shards*: 0–29, 30–59 e ≥ 60 (resultado em 4.2).
- *Intervalo* (Pereira): loja em um *shopping* dividida por **faixas de preço**; a consulta por preço vai a um único *shard*.
- *Hash* (Pereira): tabela cuja primeira coluna tem o nome completo de pessoas sem repetição → essa coluna vira chave de fragmentação transformada em *hash*.

> **"O que é *hash*"** (quadro do material): sequência de bits que representa dados por letras e números de comprimento fixo; transforma uma grande quantidade de dados em uma pequena. O capítulo inteiro, por exemplo, pode ser representado por um *hash*.

**Cuidados antes de escolher (Pereira):**

| Cuidado | Por que importa |
|---------|-----------------|
| **Escolha da chave** | Deve ser **estável, pouco volátil**, preferencialmente **invariável e exclusiva**; se muda, talvez seja preciso **mover** o fragmento (mais atualizações e movimentação de dados) |
| **Equilíbrio e redimensionamento** | *Shards* devem ter volume semelhante; como há inserções e remoções, é preciso **rebalanceamento periódico** (processo oneroso → planejar o crescimento e ter equipe capaz de reequilibrar rapidamente) |
| **Eficiência das consultas** | Consultas que acessam **um** *shard* são mais eficientes que as que juntam vários; é preciso conhecer os dados e as buscas prováveis |
| **Referências entre objetos** | Pode-se incluir a chave de fragmentação de um objeto no esquema de outro. **Exemplo:** exames de sangue de um paciente ao longo dos anos em banco dividido por ano → referenciar todos os resultados do mesmo paciente |
| **Não mudar a chave depois** | Não se pode alterar a chave de fragmento após o fragmento, nem desfazer uma coleção de fragmentos (Brandão) |

---

### 3.11 *Sharding* em *clusters* (Brandão)

**Cluster** ("aglomeração"): sistema que **une vários computadores** para funcionar como **uma única máquina** com a soma das capacidades (Gomes, 2015). Esquema (Fig. 3, Hadoop): um **nó mestre** (*master*, com um *secondary master*) e vários **nós** (*slaves*); externamente é visto como uma só máquina. Todo membro do *cluster* fragmentado deve poder se conectar a todos os demais, incluindo *shards* e servidores de configuração (atenção a rede, segurança, interfaces e *firewalls*).

**Usos de *cluster*:** sistemas distribuídos, fragmentação de dados, **supercomputadores** (algoritmos complexos com grandes volumes, comuns em projetos de IA) e **mineração de dados** (análise de agrupamento — *clustering* — como método para classificar itens em aglomerados). Em geral, melhoram desempenho e disponibilidade e são mais econômicos que computadores individuais de velocidade equivalente; surgiram da convergência de microprocessadores baratos, redes de alta velocidade e *software* de computação distribuída.

**Balanceamento de carga (*load balancing*):** direcionar cada requisição a um nó diferente para **não sobrecarregar sempre a mesma máquina**. Uso comum: servidores *web* ou *proxy* em rede local.

**Cluster local × remoto:**

| Aspecto | *Cluster* **local** | *Cluster* **remoto** |
|---------|--------------------|----------------------|
| Onde | Rede local (tipo **LAN**) | Acesso externo; conexão por meio de *clusters* na camada de transporte; inclui serviços em **nuvem** (Google, Amazon, Microsoft) |
| Segurança | Mais fácil de garantir (acesso limitado a quem está na rede local); ainda é preciso monitorar ataques vindos de **usuário local autorizado** invadindo externamente | Alvo de invasores; exige proteção reforçada |
| Custo | Infraestrutura própria | Custo diminui (energia e manutenção física terceirizadas); a equipe de TI foca nas soluções de armazenamento e transação |
| Característica | — | Módulo de *cluster* remoto: conexões **unidirecionais** usadas na **replicação** e na **pesquisa entre *clusters*** (*cross-cluster*); cada *cluster* é referenciado por nome e lista de **nós-semente**; até **três nós de *gateway*** são selecionados para conexão |

> **"Fique atento" do material:** antes dos *clusters*, **mainframes** eram usados como uma grande máquina com redundância modular; o menor custo inicial e o aumento da velocidade das redes favoreceram os *clusters*. Algumas empresas ainda usam mainframes, mas o número cai a cada ano.

**Servidor tradicional × clusterizado na nuvem (Quadro 1, Applied Innovations):**

| | Servidores *cloud* padrão | Servidores *cloud* clusterizados |
|---|--------------------------|----------------------------------|
| Nº de servidores físicos | 1 | 12–15 |
| Tipo de armazenamento | RAID-10 | SAN (*Storage Area Network*) |
| ***Failover* automático** | Não | Sim |

***Failover*:** reconfiguração automática do sistema para colocar um novo nodo em serviço quando outro falha.

**Kubernetes:** sistema que facilita a **orquestração de contêineres** (como Docker), criando *clusters* virtualizados. É transparente para o usuário em qual máquina o processo roda; pode haver mais de um nodo por máquina física ou nodos divididos pelo *cluster*. **Exemplo (Fig. 4): Google Kubernetes Engine (GKE)** — plano de controle (servidor de API, controlador de recursos, agendador, armazenamento), nós com *pods* de usuário e contêineres, e serviços da Google Cloud conectados (rede VPC, disco persistente, ***Load Balancer***, monitoramento).

***Shards* em *cluster*:** exige sistemas distribuídos com capacidade de usar *sharding*. Cada *shard* contém um **subconjunto** dos dados e pode ser implantado como um **conjunto de réplicas**. O sistema distribuído atua como **roteador de consulta** (interface entre aplicativo cliente e *cluster* fragmentado); os **servidores de configuração** guardam **metadados** e definições do *cluster*.

> **Exemplo do material — ElasticSearch:** ferramenta que usa *sharding* para distribuir dados em *cluster*. Normalmente considerado NoSQL, mas criado como **motor de busca** (como os da Google e Yahoo). A Elastic oferece Logstash e Beats (coleta, agregação e enriquecimento de dados) e o **Kibana** (explorar/visualizar/gerenciar a *stack*). No ElasticSearch ocorrem indexação, fragmentação, pesquisa e análise.

---

### 3.12 Relação entre *sharding* e índices (Brandão)

**Índice (relacional):** organiza os registros para recuperação eficiente de todos os registros que satisfazem uma condição de pesquisa nos campos-chave (Ramakrishnan e Gehrke, 2011); funciona como **ponteiro direto** para o registro, diminuindo o tempo de acesso. Pode ajudar em consultas com `WHERE` e operadores `NOT`, `AND`, `OR` (Bianchi, 2007). Tipos citados: booleano, de *hashing*, *bitmap*, de várias tabelas, **árvore B (B-*tree*)** e funcional.

**Figura 5 (índice não clusterizado B-*tree* sobre `Nome`):** raiz **A–Z** → nós intermediários **A–G**, **H–N**, **O–Z** → **folhas** com pares *Chave / RowId* (Alberto 123564, Ana 123698, Antonio 142986…). **Exemplo do material:** buscar "Maria" com `WHERE` → a consulta parte do nó mestre (raiz), que aponta ao intermediário **H–N**, onde estaria a letra **M**.

> Ver **Aula 02 §3.7** (conceito e vantagens), **§3.7.2** (agrupado, primário e secundário), **§3.7.3** (estrutura B-*tree*) e **Anexos A e B** (explicação simples do índice por nome e quadro de termos). O que há de novo nesta aula é a **comparação** com o *sharding*.

**Quadro 2 — Índices × *sharding* (Oracle, adaptado):**

| Índices | *Sharding* |
|---------|-----------|
| Melhora as consultas na maioria dos casos | Realiza o **balanceamento de carga** em servidores |
| Requer **menos estrutura** (tabela inteira em um mesmo servidor) | Usado em servidor **clusterizado** (várias máquinas interligadas em conjunto) |
| Permite acesso a dados **ordenados** sem precisar ordenar (dados já guardados de forma ordenada) | Permite replicação com ***shards* redundantes** (alguns *shards* com o mesmo dado de outro, para garantir disponibilidade) *(ver ponto de atenção 5.7)* |
| Acesso feito por um dos três tipos de campo: chave primária, chave estrangeira e *constraint unique* *(ver ponto de atenção 5.8)* | Acesso feito por ***shard keys*** (chaves de partição) |

**Desvantagens dos índices ("Fique atento"):** a tabela virtual de índices **aumenta o espaço em disco**; toda alteração no índice exige alterar a tabela de índices; em alguns casos pode **piorar** o desempenho, pois pode demorar mais procurando a partição onde está o dado do que numa consulta direta.

**Conclusão do capítulo:** índices e *sharding* melhoram o desempenho das consultas, mas é preciso pesar a **escalabilidade dos *clusters*** contra a **simplicidade do armazenamento único** não distribuído. Para *big data*, trabalhar com *clusters* é o mais indicado.

**Comparação de uso *(síntese de estudo, complementação)*:**

| Situação | Índice | *Sharding* |
|----------|--------|-----------|
| Tabela cabe em **um** servidor, mas as buscas estão lentas | **Primeira escolha** | Desnecessário (adiciona complexidade) |
| Dados e carga passam da capacidade de **um** servidor | Ajuda dentro de cada *shard*, mas não resolve o limite | **Necessário** |
| Busca pontual numa tabela enorme **já fragmentada** | Índice **dentro** de cada *shard* | Chave de fragmentação leva ao *shard* certo |

> Os dois **não competem**: o material mostra que, em bancos fragmentados (ex.: MongoDB), a chave de fragmento depende do índice de suporte (ver 3.15).

---

### 3.13 *Sharding* × replicação (Pereira)

**Diferença central:** *sharding* = particionamento em fragmentos, e os *shards* armazenam **subconjuntos** dos dados; replicação = **cópia exata dos dados inteiros**. Sem replicação há ponto de falha: se um nó do *cluster* ficar inativo, parte dos dados fica indisponível. **Só a integração** entre particionamento e replicação gera um sistema de banco eficaz.

| Replicação | Particionamento (*sharding*) |
|-----------|------------------------------|
| Armazena **cópias** dos dados em várias máquinas | Armazena **partes** dos dados em várias máquinas |
| Melhora o desempenho de **leitura**, mas é preciso repetir a escrita/gravação | Melhora o desempenho de **leitura e escrita** |
| Conjunto de réplicas: o **primário** é o único capaz de receber gravações | *Shard* primário é composto pelos conjuntos de réplicas que formam um fragmento |
| **Quando usar** *(complementação)*: disponibilidade, tolerância a falhas, leitura em escala | **Quando usar** *(complementação)*: volume ou carga de escrita acima de um servidor |

> O Quadro 1 do material traz, na fonte, duas linhas aparentemente **invertidas** ("replicação possibilita o dimensionamento" / "sharding possibilita a redundância"). A tabela acima segue o texto do próprio capítulo (replicação → tolerância a falhas; *sharding* → armazenar subconjuntos para escalar). Ver ponto de atenção 5.6.

---

### 3.14 *Sharding* no Apache Cassandra (Pereira + infográfico)

**Visão geral:** banco **distribuído** para *big data*, projetado com base no **DynamoDB** (Amazon) e no **BigTable** (Google), com alta escalabilidade e tolerância a falhas. Arquitetura **SN**: **sem controlador central** e **sem relação mestre/escravo** entre os nós — **todos são iguais** (Carpenter e Hewitt, 2016).

**Modelo de dados:** cada linha é referenciada por uma **chave primária** (chave de linha); o nº de colunas pode **variar entre linhas** (linha 1 com cinco colunas, linha 2 com três). **CQL** (*Cassandra Query Language*) é baseada em SQL (tabelas, linhas, colunas). A chave primária é composta pela **chave de partição** e, opcionalmente, por colunas de *clustering*. Cada tabela possui uma chave de partição (simples ou composta) que **determina a localidade dos dados**; ela deve criar partições de tamanho ideal para minimizar movimentação de dados no redimensionamento. Tamanho recomendado pelo material: ≤ **10 MB**, podendo chegar a 100 MB.

**Como o *sharding* funciona:**
- Cada servidor é um *shard*, com dados **replicados em outros servidores**; a estrutura usada é **chave/*hash***, chamado ***token***.
- Os objetos são atribuídos a cada *shard* em **partes iguais**, distribuídos uniformemente no *cluster*; as réplicas seguem o fator de replicação configurado.
- O balanceamento é simplificado: os **intervalos de *hash*** que definem cada *shard* deixam, em média, **igual número de linhas**.

**Partitioners (mecanismos que geram o *token*):**

| *Partitioner* | Como gera a chave | Características (segundo o material) |
|--------------|-------------------|--------------------------------------|
| **Murmur3Partitioner** (padrão) | *Hash* **MurmurHash** | Distribuição **uniforme**; pode melhorar o desempenho de 3 a 5 vezes em relação aos outros |
| **RandomPartitioner** | *Hash* **MD5** (criptográfico) | Mesma função, mas a geração das chaves **demora mais** |
| **ByteOrderedPartitioner** | **Bytes-chave em ordem léxica** | Mantém distribuição **ordenada**; **pouco utilizado** |

Os particionadores **não são compatíveis entre si**: dados particionados por um dificilmente serão convertidos corretamente para outro.

**Hash consistente (anel):** em vez de alocar chaves em "baldes" (*buckets*), o Cassandra as armazena num **anel contínuo**. Ao adicionar objetos/nós **não é preciso remapear todos os *hashes***: o *hash* simplesmente é movido para a **próxima posição**. Um grande nº de intervalos de *tokens* é distribuído igualmente entre os servidores; ao entrar um servidor, fragmentos migram lentamente → **menos movimentação de dados**. Ao iniciar o *cluster*, cada nó recebe um intervalo de *token* proporcional; pode haver até **255 *tokens* por nó**.

> **Exemplo (Fig. 2):** anel com 4 nós — nó 1: 1–35; nó 2: 36–70; nó 3: 71–105; nó 4: 106–139. Um fragmento com ***token* 127** é armazenado no **nó 4**.
> Ver **Aula 01 §3.4** (*Sharding e hash consistente*: anel, nós virtuais, fator de replicação). Aqui o material mostra a **aplicação concreta no Cassandra**.

**Passos quando um nó recebe uma leitura/gravação:**
1. Identifica os nós cujos dados têm chaves correspondentes à busca.
2. Encaminha a solicitação a esses nós e espera a resposta.
3. Se não houver retorno dentro de um **tempo limite** pré-configurado, devolve "falha na solicitação" ao cliente.
4. Se houver retorno, determina a **resposta mais recente** pelos registros de data e hora.
5. Agenda o **reparo dos dados nas réplicas**, se houver modificações.

**Replicação no Cassandra:** acontece dentro do anel; cada fragmento é replicado em **N hosts** (N = fator de replicação, configurado "por instância"); cada chave é atribuída a um **nó coordenador**, responsável pela replicação dos fragmentos do seu alcance. O material afirma que o Cassandra **elege um líder** com o **Zookeeper** e que os metadados ficam em *cache* local de cada nó (ver ponto de atenção 5.10).

**Detecção de falhas — protocolo de fofocas (*gossip*):** informações sobre se um *shard* está vivo/inativo são compartilhadas por detecção de falhas baseada em **fofocas**; cada nó recebe estado de outros nós interligados (máximo de três) e evita tentar comunicar-se com nós inacessíveis. A fofoca também informa **posição do nó, metadados e esquematização**; ocorre **a cada segundo**, com cada nó escolhendo outro **aleatoriamente** para trocar o estado de atividade.

**Arquitetura simplificada (uma máquina)** exige quatro módulos: **particionamento**, **associação de *cluster***, **detecção de falhas** e **mecanismo de armazenamento**.

**Infográfico — *Sharding* no Apache Cassandra:**

| Tema | Resumo do material |
|------|--------------------|
| Hash consistente | Usado na **replicação (3×)** e no particionamento; *hashes* organizados em **anel de *tokens*** |
| Mecanismo de busca | Dados **desnormalizados e duplicados**: várias versões de uma mesma tabela, o que facilita a consulta |
| Escalabilidade | "Quase infinita": **dobrando o nº de nós**, o sistema lida com quase o **dobro** de leituras e gravações |
| Resultado | Alta disponibilidade, rápida leitura e escrita, potencial de escalabilidade **linear** |

**Resumo de vantagens:** alta escalabilidade, alto desempenho, ampla aplicabilidade, **alta taxa de atualização com baixa latência**.

> Ver **Aula 01 §3.7** (Cassandra: peer-to-peer, sem SPoF, escala linear, CQL; *keyspace* ≈ database; *column family* ≈ tabela; *row key* ≈ chave primária) e **§3.4** (gossip).

---

### 3.15 *Sharding* no MongoDB (Pereira + Brandão)

**Visão geral:** banco **distribuído, baseado em documentos, de propósito geral** (definição dos desenvolvedores). Suporta **particionamento automático**, usando a estrutura chave/*hash*; **automatiza o balanceamento** entre *shards* e facilita **adicionar/remover máquinas**.

**Três componentes principais (Fig. 3):**

| Componente | Função |
|-----------|--------|
| ***Shards*** | **Conjuntos de réplicas** de servidores que armazenam subconjuntos dos dados |
| **Roteadores de consulta (*mongos*)** | **Interface** entre aplicativo cliente e *shards*; usam as informações dos servidores de configuração para achar o *shard* certo |
| **Servidores de configuração** | Armazenam **apenas metadados**: localização de cada dado e configurações gerais (BRADSHAW; BRAZIL; CHODOROW, 2019) |

**Funcionamento do cluster fragmentado:**
- Para cada conjunto de dados há um ***shard* primário** (com a informação **não fragmentada**); após a fragmentação surgem ***shards* secundários**, cada um com um conjunto de réplicas. Cada *cluster* com *shard* primário e conjunto de réplicas deve ter o **próprio servidor de configuração**, pois operações nele afetam desempenho e disponibilidade (ver ponto de atenção 5.12).
- Se o *cluster* do servidor de configuração **perder o primário**, os metadados ficam **somente leitura**: dá para **ler e gravar** nos *shards*, mas **migração e divisão de fragmentos** só voltam quando um novo primário for eleito.
- **Papel dos *mongos*:**
  1. **Rotear** a consulta: consultam os **metadados** de cada partição para reduzir a busca. **Exemplo (universidade, Pereira):** *shards* divididos a cada **1000 registros** em ordem crescente pelo CPF dos alunos; se o número buscado começa com 3, a busca se restringe a certos *shards*. Como os metadados mudam (redistribuição de dados), **a cada consulta os *mongos* acessam os metadados**, mesmo que a consulta já tenha sido feita antes.
  2. **Mesclar** resultados: se a busca for por **valor de mensalidade X** (campo que não é a chave), ela é executada em **todos os *shards***; cada um envia resultados aos *mongos*, que **reúnem e ordenam** (se preciso) e devolvem ao cliente **como se fosse um único banco**.
- **Estratégias:** suporta **chave/*hash*** e **intervalo**, que devem ser escolhidas **antes** da fragmentação, pois o campo da chave é **imutável**; a escolha afeta desempenho, eficiência e escalabilidade, e o **índice de suporte** da chave também influencia.

| | *Hash* | Intervalo |
|---|--------|-----------|
| Cálculo | O sistema calcula os *hashes* automaticamente → **custo de sobrecarga** | Menor sobrecarga; **estratégia padrão** |
| Localidade | Menor chance de os dados buscados estarem num **único** fragmento → busca em mais de um *shard* | Maior chance de achar tudo no **mesmo *shard*** se a busca é limitada a um intervalo |

> Ver **Aula 01 §3.7** (MongoDB: BSON, auto-*sharding*, replicação e *failover*) e **§3.4** (CAP: classificado como CP).

**Tolerância e disponibilidade:** o *cluster* fragmentado continua executando operações **parciais** de leitura e gravação mesmo com um ou mais *shards* inativos — mas os fragmentos desses *shards* **não podem ser acessados** se não houver réplicas. Com um conjunto de réplicas do servidor de configuração (**CSRS**, *Config Server Replica Set*), leituras e gravações continuam enquanto a **maioria** do conjunto estiver disponível. Por isso é importante manter o conjunto de réplicas (Boaglio, 2015).

### 3.16 Cassandra × MongoDB (síntese do material)

| Aspecto | Apache Cassandra | MongoDB |
|---------|------------------|---------|
| O que é um *shard* | **Um único servidor** | **Um conjunto de réplicas** (vários servidores) |
| Onde fica cada objeto | Armazenado em **vários *shards*** (réplicas em outros nós) | Contido em **um só *shard***, replicado várias vezes dentro dele |
| Falha de um servidor | **Outro *shard*** terá os dados | **Outra unidade do conjunto de réplicas** do próprio *shard* o substitui |
| Movimentação de dados após falha | **Maior** | **Menor** |
| Desempenho | Menos estável *(segundo o material)* | Mais estável *(segundo o material)* |
| Arquitetura | SN, **sem mestre**; todos os nós iguais | **Roteadores + servidores de configuração + *shards*** |
| Estratégia de partição | Chave/*hash* (***token***, anel, hash consistente) | Chave/*hash* ou **intervalo** (chave imutável) |
| Detecção de falhas | Protocolo de fofocas | Eleição de novo primário no conjunto de réplicas *(complementação a partir do material)* |
| **Quando usar** *(complementação)* | Escrita em altíssimo volume, muitos nós, sem ponto único de coordenação | Documentos com esquema flexível e consultas variadas, com necessidade de balanceamento automático |

**Conclusão do capítulo:** o foco do particionamento é melhorar **desempenho e escalabilidade** e, de brinde, a **disponibilidade**, a depender de como os dados são divididos **e replicados**. Se uma partição falha, o cliente não necessariamente fica sem acesso, pois os dados podem estar em outras partições. Ao estudar *sharding*, é preciso olhar as formas de **replicação** que o banco permite.

---

### 3.17 *Sharding* no BigTable (infográfico)

- **BigTable (Google):** serviço de banco de dados para *big data*, o mesmo NoSQL usado em serviços como **Gmail, Maps, Pesquisa e Analytics**.
- **Funcionamento:** no *cloud* do BigTable, uma tabela é fragmentada em **blocos, que são conjuntos de linhas contíguas** (isto é, *sharding* por **intervalo de linhas**); a fragmentação ajuda no balanceamento da carga das consultas.
- **Cluster:** a equipe define quantos **nós** existirão, compartilhando os dados (partições) e até replicando; *backups* quase em tempo real podem ser criados automaticamente.
- **Indicação de uso:** processamento de dados **não estruturados** em grande volume, relatórios e visualizações, **séries temporais** de marketing ou financeiro, gráficos.
- **Conexão com outros SGBDs:** o infográfico diz que se conecta a Cassandra, HBase e MongoDB (ver ponto de atenção 5.15).

---

### 3.18 Complemento: capítulo *Sharding* (Soares) — versão reenviada

*Este capítulo (SOARES, J. A. — *Framework de Big Data*, SAGAH; objetivos: definir *sharding*, explicar seu uso em *clusters* locais e remotos e compará-lo com índices) trata do mesmo tema de 3.9–3.13, com outra organização e outras fontes (Hussain e Hussain, 2024; Kleppmann, 2017; Fowler, 2015; Elmasri e Navathe, 2018; MongoDB, 2026; Zhou et al., 2023). Para não repetir, aqui entram **apenas os pontos novos ou que mudam a ênfase**; o que já foi explicado aparece como ponteiro.*

#### a) Fundamentos: o que o capítulo acrescenta
- ***Sharding* = particionamento horizontal** para escalar o armazenamento e o processamento entre nós. Cada registro, em geral, pertence a **um** fragmento, que pode ter **cópias** em outros servidores (tolerância a falhas). Ver 3.9.
- **Em cada modelo (Elmasri e Navathe, 2018):** no relacional, o fragmento horizontal reúne **parte das linhas** mantendo **todos os atributos**; no **vertical**, a divisão é por **colunas** e exige **atributos comuns** para reconstruir os registros; em bancos de **documentos**, distribuem-se os documentos de uma coleção.
- **Equilíbrio:** o objetivo é evitar que um único nó receba muitos registros novos e fique sobrecarregado (Fowler, 2015); depende da **regra de distribuição** e dos **padrões de acesso**.
- **Fig. 1 (pedidos por identificador do cliente):** Servidor A / *Shard* 1 → clientes **1 a 1.000**; Servidor B / *Shard* 2 → **1.001 a 2.000**; Servidor C / *Shard* 3 → **2.001 a 3.000**.
- **A chave de fragmentação não precisa ser a chave primária:** identificar um registro e definir **sua localização** são funções diferentes. A escolha deve considerar dados, consultas, relações entre tabelas e **custos de comunicação** (manter juntos os dados acessados juntos).
- **Um *shard* não é necessariamente um servidor:** um nó pode guardar **vários fragmentos** e um fragmento pode ter **réplicas** em vários nós (Kleppmann, 2017).
- **Exemplo bancário (Zhou *et al.*, 2023):** ambiente real com mais de **20 mil tabelas**, a maior com mais de **50 bilhões de registros**, particionado em um banco distribuído de **60 nós**; mostra que a chave deve considerar as consultas e o **tamanho das tabelas** para reduzir transferência entre nós.

**Exemplo dos sensores — a escolha da chave muda a leitura e a escrita:**

| Chave de distribuição | Ajuda | Custo |
|-----------------------|-------|-------|
| **Só a data** | Consultas **por período** | Novas medições se concentram no fragmento **atual**; dados antigos ficam espalhados e as gravações recentes, em um nó |
| **Data + identificador do dispositivo** | **Distribui as gravações** entre mais fragmentos | Muda a forma de localizar os dados nas consultas: reunir as medições de vários dispositivos num período pode exigir acesso a mais fragmentos |

*"Fique atento" do material:* dividir só por dia seria suficiente para distribuir as gravações simultâneas de milhares de sensores? O que mudaria se o identificador do dispositivo fizesse parte da chave? A resposta exige considerar **escrita e leitura** e as **operações mais frequentes**.

#### b) Intervalo × *hash* e o problema do *hotspot*
(Estratégias em 3.10; aqui, o ponto de vista de Soares.)

| Estratégia | Comportamento | Consequência para as consultas |
|------------|---------------|--------------------------------|
| **Intervalos** | Cada fragmento recebe uma **faixa** de valores, **mantendo a ordem** | Facilita consultas **por intervalo** |
| ***Hash*** | Uma função transforma o valor da chave no fragmento de destino; tende a **distribuir valores distintos** entre fragmentos | **Valores próximos** na chave original podem cair em servidores diferentes; uma consulta por faixa **precisa acessar vários fragmentos** (conforme a implementação) |

- ***Hotspot*:** quantidades semelhantes de registros **não** significam cargas semelhantes. Quando muitas solicitações se concentram em um fragmento, surge um ponto de sobrecarga. **O particionamento por *hash* não elimina o *hotspot*** se as operações usam a **mesma chave**, pois valores iguais continuam indo para o mesmo destino.
- **Fig. 2:** os três servidores têm **volume semelhante**, mas o Servidor A tem **carga elevada** (uma conta muito popular numa rede social), enquanto B e C ficam pouco usados. **Acrescentar máquinas pode não resolver** se as solicitações continuam indo ao mesmo fragmento.
- A distribuição pode **perder o equilíbrio** durante o funcionamento e exigir **rebalanceamento**; é preciso acompanhar o crescimento dos dados e a forma de acesso.
- **Capacidade ≠ desempenho:** o *sharding* aumenta a capacidade e permite operações independentes em paralelo, mas **não garante** que todas as consultas fiquem mais rápidas nem que o desempenho cresça na proporção do número de servidores. Consultas que acessam vários fragmentos exigem **comunicação e reunião de resultados**.

#### c) Roteamento e rebalanceamento
- **Roteamento:** encaminha leituras e gravações aos nós responsáveis; depende das **informações de localização** dos fragmentos e pode ser feito por uma **camada intermediária**, pelos **próprios nós** ou pelo **cliente**. Quando as condições da consulta não permitem identificar os fragmentos, pode ser preciso **consultar vários servidores** e reunir as respostas; a localização deve ser **atualizada sempre que a distribuição mudar**.
- **Três formas de encaminhamento (Kleppmann, 2017):** (1) roteador intermediário; (2) cliente que conhece o mapeamento dos fragmentos; (3) o nó que recebe a solicitação a envia ao responsável.
- **Rebalanceamento:** transferir fragmentos (ou parte das responsabilidades) entre nós usa rede, armazenamento e processamento e **pode afetar as operações em andamento**. Recomenda-se acompanhar a distribuição e planejar **como acrescentar capacidade e reorganizar os dados sem sobrecarregar os servidores** durante a mudança (Hussain e Hussain, 2024).

#### d) *Sharding* × replicação e quando adotar
- Ver 3.13. Soares reforça que o ***sharding* sozinho não garante** que os dados continuem acessíveis quando um servidor falha: a **disponibilidade** depende também das **réplicas**, dos procedimentos de **recuperação** e do **redirecionamento** das solicitações (Elmasri e Navathe, 2018).
- **Três objetivos distintos** (Hussain e Hussain, 2024): **escalabilidade horizontal** (acompanhar a demanda), **disponibilidade** (acesso ao serviço, inclusive diante de falhas) e **otimização de consultas** (reduzir o trabalho para executar as operações). Ampliar a capacidade não garante a continuidade do serviço após uma falha nem a eficiência de todas as consultas.
- **Quando adotar:** o *sharding* deve atender a uma necessidade real (crescimento da base, aumento da demanda, possibilidade de distribuir as operações); **uma consulta lenta, sozinha, não basta** para justificar o uso. Antes, identificar se a dificuldade está no **armazenamento**, no **processamento** ou na **concentração de acessos**; avaliar se as operações podem ocorrer em **fragmentos independentes** e estimar o custo de **reunir dados de vários servidores**.

#### e) *Clusters* locais e remotos: o que o capítulo acrescenta
(Definições e quadro em 3.11.)

| Aspecto | Local | Remoto (geograficamente distribuído) |
|---------|-------|--------------------------------------|
| Onde | Nós no **mesmo ambiente** (ex.: *datacenter*), em rede local | Nós em **localidades diferentes** |
| O que pesa | — | **Latência** e possíveis **falhas de comunicação** entre os nós |

Servidores convencionais também podem compor um *cluster*, desde que tenham recursos para a carga prevista; a organização serve ao relacional e ao NoSQL, com recursos de roteamento.

**MongoDB em *cluster* local (Fig. 3):** a aplicação fala com o roteamento ***mongos***; os ***shards*** são **conjuntos de réplicas** (cada um guarda parte dos pedidos); a **configuração** guarda os **metadados replicados** sobre a organização do *cluster* (MongoDB, 2026a). Ver 3.15.
- **Consulta que identifica os fragmentos** → vai só à parte necessária (ex.: busca pelos pedidos de **um cliente**, se a chave for o cliente). **Consulta ampla** → acessa **todos** os *shards* e reúne as respostas (***scatter/gather***), cada *shard* podendo usar índices compatíveis. A avaliação deve considerar **localização dos registros** e **comunicação** entre os componentes.
- **Relacionar dados em nós diferentes** pode exigir coordenação, transferência e redistribuição de registros. Se os dados forem distribuídos pelo **identificador do cliente**, o **histórico de um cliente** fica em um fragmento; já o **faturamento de todos os clientes** exige acesso a **vários *shards*** e soma dos resultados.

**Disponibilidade em *clusters* com líder e seguidores (Kleppmann, 2017):**
- Se um fragmento tem **apenas uma cópia**, a falha do servidor o torna inacessível.
- Em arquiteturas com **líder e seguidores**, outro nó pode assumir o papel de líder, mas o sistema precisa **detectar a falha, escolher um substituto e redirecionar as operações**; o atendimento depende dos dados disponíveis nesse nó e das garantias do sistema.
- As **réplicas** podem atender **leituras** e permitir mais operações em paralelo, mas podem ficar **temporariamente desatualizadas** quando a atualização é **assíncrona** (Fowler, 2015). Escolher entre **consistência** e **latência** conforme a aplicação (ver 3.4 e 3.2).

**Ambiente geográfico (Fig. 4):** a **Região A** tem a aplicação, o *Shard* A e a **réplica do *Shard* B**; a **Região B**, o inverso. Setas contínuas indicam o **acesso** da aplicação e setas tracejadas, a **replicação**. Concentrar os dados mais usados perto dos usuários reduz a comunicação remota, mas **não garante** acesso se todo o ambiente local falhar; por isso a localização dos *shards* e das réplicas deve ser **planejada em conjunto**, conforme as falhas que o sistema precisa suportar.

| Replicação entre regiões | O que acontece | Risco / custo |
|--------------------------|----------------|---------------|
| **Síncrona** | A confirmação pode depender da resposta da **réplica remota** | **Maior tempo de espera** |
| **Assíncrona** | O cliente recebe a confirmação **antes** de a réplica ser atualizada | Falha nesse intervalo: alterações recentes podem **não estar na cópia** usada na recuperação |

O planejamento deve definir **quanto atraso ou perda de dados** a aplicação aceita e quais garantias de recuperação são necessárias (Kleppmann, 2017). Ver 3.4 (síncrono × assíncrono).

> **Saiba mais (do material):** transações que acessam **diferentes *shards*** também precisam de comunicação e coordenação entre nós. Zhuang *et al.* (2024) estudam isso no **GeoTP**, proposta implementada sobre o **Apache ShardingSphere** para transações geograficamente distribuídas: reduzir etapas de comunicação e organizar a execução considerando a **latência**. O estudo mostra que distribuir os dados em ambiente remoto exige avaliar como o tempo de comunicação afeta as transações simultâneas.

**Integridade, *backup* e segurança**

| Tema | O que o capítulo diz |
|------|----------------------|
| **Integridade e transações** | Preservar a integridade durante o funcionamento e as mudanças (regras de validade, identificadores, relações). Uma transação que altera vários *shards* deve ter **todas as alterações aplicadas ou nenhuma mantida**; o **isolamento** controla a interação entre transações simultâneas |
| **Replicação ≠ *backup*** | A replicação ajuda a manter dados disponíveis, mas **não substitui *backups***: uma exclusão ou alteração indevida também pode ser copiada para as réplicas. *Backups* permitem recuperar dados de um momento anterior e precisam passar por **testes de restauração**; a recuperação em *clusters* fragmentados deve manter a **consistência entre os fragmentos** |
| **Segurança** | Em todo o *cluster*: **autenticação** (quem acessa) e **autorização** (operações permitidas); permissões limitadas ao necessário, abrangendo servidores de dados, roteadores e componentes de configuração; **criptografia em trânsito** e **em repouso**; restrições de rede e **registros de auditoria**; aplicar também aos **novos nós** (MongoDB, 2026c) |
| **Crescimento do ambiente** | Ao incluir nós, a carga pode perder o equilíbrio e exigir rebalanceamento; ao transferir dados é preciso **atualizar os metadados de localização**, **conferir os registros transferidos** e verificar se as consultas continuam encontrando os dados; avaliar garantias de transação e desempenho com **operações representativas e testes de carga** |

**Checklist de avaliação da arquitetura** *(organização de estudo a partir do texto)*

| Pergunta | O que verificar |
|----------|-----------------|
| Os novos *shards* atendem ao crescimento? | Capacidade de armazenamento e processamento |
| As réplicas e a recuperação retomam o serviço após as falhas previstas? | Disponibilidade e procedimentos de recuperação |
| As consultas mais frequentes acessam **poucos** fragmentos? | Escalabilidade e otimização de consultas |

#### f) *Sharding* e indexação: o que o capítulo acrescenta
(Índices em 3.12 e Aula 02 §3.7; o ponto novo é a **comparação detalhada** e a distinção **índice local × global**.)

- **Para que serve cada um:** o **índice** ajuda a **localizar os registros**; o ***sharding*** **divide os dados e distribui o trabalho**. Eles atuam em **partes diferentes** do acesso e **não são equivalentes**: criar índices não aumenta a capacidade de armazenamento de um nó, e acrescentar *shards* não garante caminhos de acesso eficientes (Kleppmann, 2017).
- **Estruturas de índice citadas:** **árvores B** (chaves ordenadas; buscas por **igualdade e por intervalo**), índices baseados em ***hash*** (associam chaves à localização; favorecem buscas por **igualdade**) e **índices secundários** (buscar por atributos diferentes da chave primária). Podem ser criados em banco centralizado ou **dentro dos fragmentos**; a escolha depende de filtros, ordenação e relacionamentos mais usados. Ver Aula 02 §3.7.

**Quadro 1 (Soares) — *sharding* × indexação**

| Aspecto | *Sharding* | Indexação |
|---------|-----------|-----------|
| **Propósito** | Distribuir registros e processamento | Organizar caminhos de acesso |
| **Organização** | Fragmentos horizontais atribuídos a nós | Chaves, referências ou dados organizados para busca |
| **Critério de projeto** | Chave de distribuição, volume e padrões de acesso | Filtros, ordenação e relacionamentos das consultas |
| **Benefício esperado** | Ampliar a capacidade e repartir operações | Reduzir o trabalho de localização de registros |
| **Custos de escrita** | Roteamento e eventual coordenação entre *shards* | Atualização dos índices afetados |
| **Administração** | Monitoramento e rebalanceamento | Espaço, criação e manutenção das estruturas |
| **Limitação** | Consultas amplas podem acessar muitos nós | Nem toda consulta se beneficia de um índice |
| **Uso combinado** | Cada fragmento pode ter índices | Índices apoiam buscas nos dados fragmentados |

- **Uso combinado (exemplo do material):** buscar os pedidos de um cliente em um período → o **identificador do cliente** leva ao fragmento correspondente e um **índice por cliente e data** facilita localizar os registros dentro dele. O sistema precisa **selecionar os *shards*** e **escolher o caminho de acesso** (MongoDB, 2026b).
- **Duas situações-problema do material:**

| Situação | Diagnóstico do material | Solução |
|----------|------------------------|---------|
| **Loja com banco centralizado e capacidade suficiente**, mas a consulta pelo **e-mail** do cliente examina a tabela inteira | O problema está em **como localizar** o cliente | Analisar um **índice sobre o e-mail**, mais adequado que *sharding* (se o custo e os recursos permitirem) |
| **Plataforma com índices adequados**, mas que acumula registros e gravações e o servidor se aproxima dos limites de armazenamento e processamento | A falta é de **capacidade** | Acrescentar índices **não resolve**; **distribuir dados e operações** entre servidores contribui para a escalabilidade horizontal |

- **Índice não garante melhora em todas as consultas:** uma consulta que retorna **grande parte dos registros** tem menos benefício que uma busca seletiva; alterações nos valores indexados exigem **atualizar o índice**, aumentam o **espaço** e o trabalho de manutenção — equilibrar **ganho de leitura × custo de escrita**.
- **Distribuição inadequada** concentra solicitações em poucos fragmentos e deixa outros ociosos; tanto a distribuição quanto os índices devem ser avaliados conforme os **gargalos** da aplicação (Zhou *et al.*, 2023).

**Índice local × índice global em dados fragmentados (Quadro 2 de Soares)**

| Aspecto | Índice **local** | Índice **global** |
|---------|------------------|-------------------|
| **Abrangência** | Registros do **próprio fragmento** | Registros de **diferentes fragmentos** |
| **Busca secundária** | Pode exigir consulta a **todos os *shards*** (*scatter/gather*) | Pode **direcionar a busca** às partições do índice |
| **Manutenção** | Vinculada aos dados do fragmento | Pode envolver **outros nós e partições** |
| **Resultado** | Atende aos registros armazenados no *shard* | Pode exigir buscar os dados completos em **outros *shards*** |
| **Atualização** | Segue os procedimentos de atualização do próprio fragmento | Pode exigir **coordenação** ou apresentar **atraso** |

- O **índice global** pode ser particionado por **critério diferente** do usado nos dados originais e **também pode ser distribuído** entre vários nós; alterar um registro pode exigir atualizar entradas em **outros nós**, e se a atualização for assíncrona o índice pode ficar **temporariamente desatualizado**.
- **"Local" refere-se à abrangência do índice**, e não à localização geográfica do servidor.
- **Diagnóstico de lentidão:** antes de concluir que os índices não funcionam, medir quanto tempo se gasta para **localizar os registros em cada *shard***, quanto para **transferir e reunir as respostas**, e se um **índice global** ajudaria (considerando o custo adicional nas gravações). Verificar quais *shards* participaram da consulta e quanto trabalho foi necessário, com observação e testes (Hussain e Hussain, 2024).
- **Desempenho ≠ disponibilidade:** índices facilitam o acesso e o *sharding* distribui dados e trabalho, mas **nenhum dos dois garante** recuperação após falhas nem proteção contra acessos indevidos; replicação, *backups*, gerenciamento de transações e controles de segurança devem acompanhar a arquitetura.

**Conclusão do capítulo:** o ***sharding*** distribui os dados e a carga e amplia a capacidade conforme a demanda cresce, mas exige planejamento da **chave de distribuição** e da organização dos *clusters*; os **índices** complementam facilitando a localização; **replicação, *backups* e controles de segurança** mantêm os dados acessíveis, íntegros e protegidos.

> Ver **Aula 04 §3.10**: o **ElasticSearch** aplica *shards* e réplicas ao **índice de busca**.

---

## 4. Exemplos, aplicações e material prático

*Esta aula não traz código nem comandos; o material é conceitual, com figuras e quadros. Por isso não foi gerado arquivo `_PRATICO`.*

### 4.1 Aplicações citadas no material

| Sistema / empresa | Técnica | Como aparece no material |
|-------------------|---------|--------------------------|
| **Cache do navegador** | Replicação | Cópia local da página: melhora desempenho |
| **Rede social (perfil e geolocalização)** | Replicação *gossip* | Consistência relaxada; usuário europeu × brasileiro |
| **TAO (Facebook)** | Replicação *master/slave* | Consultas atendidas na região; risco de dado obsoleto |
| **GFS / Hadoop (HDFS)** | Replicação (passiva no GFS) | Alta disponibilidade de grandes volumes |
| **Serviço de *e-mail* (microsserviço)** | Replicação de **serviço** + *proxy* | Balanceamento de carga; sem consistência de dados a manter |
| **Aplicativo de *smartphone* sem internet** | Replicação *off-line* | Replica quando voltar a conectar |
| **Sistema bancário** | Replicação com ordem estrita | Crédito/débito na ordem certa |
| **Controle de tráfego aéreo** | Replicação com consistência rígida | Dado correto em tempo curto |
| **Facebook, Twitter, Friendster, Flickr** | *Sharding* | "Já usam há algum tempo" |
| **BigTable (Google)** | *Sharding* por linhas contíguas | Gmail, Maps, Pesquisa, Analytics |
| **ElasticSearch (Elastic)** | *Sharding* em *cluster* | Indexação, busca e análise (Logstash, Beats, Kibana) |
| **Cassandra / MongoDB / HBase / HDFS** | *Sharding* | Bancos que usam escalonamento horizontal |
| **GKE (Google Cloud)** | *Cluster* remoto com Kubernetes | Contêineres, *load balancer* |
| **Pedidos por cliente (Soares, Fig. 1)** | *Sharding* por intervalo | Clientes 1–1.000, 1.001–2.000 e 2.001–3.000 em três servidores |
| **Sensores (Soares)** | Escolha da chave de *sharding* | Só data × data + dispositivo (3.18a) |
| **Conta popular em rede social (Soares, Fig. 2)** | *Hotspot* | Volumes iguais, carga desigual (3.18b) |
| **Banco com 60 nós (Zhou *et al.*, 2023)** | *Sharding* em banco distribuído | +20 mil tabelas; maior com +50 bilhões de registros |
| **Regiões A e B (Soares, Fig. 4)** | *Cluster* remoto com réplicas cruzadas | *Shard* A + réplica de B na região A, e vice-versa |
| **GeoTP / Apache ShardingSphere (Zhuang *et al.*, 2024)** | Transações geodistribuídas | Menos etapas de comunicação (3.18e) |

### 4.2 Resultados dos exemplos numéricos do material

| Exemplo | Regra | Resultado |
|---------|-------|-----------|
| **Fig. 2 — *sharding* por intervalo (idade)** | *Shard* 1: 0–29; *shard* 2: 30–59; *shard* 3: ≥ 60 | Maria (15) e Nathan (5) → *shard* 1; Célia (55) e Ciro (38) → *shard* 2; Cláudio (72) → *shard* 3 |
| **IDs de 1 a 1000 em 4 *shards*** | Faixas ordenadas | S1: 1–250; S2: 251–500; S3: 501–750; S4: 751–1000 |
| **Fig. 2 (Cassandra) — anel de *tokens*** | Nó 1: 1–35; nó 2: 36–70; nó 3: 71–105; nó 4: 106–139 | *Token* 127 → **nó 4** |
| **CPF por blocos de 1000 (MongoDB)** | *Shards* por faixa de CPF | Busca por número iniciado com 3 limita os *shards* consultados |
| **Busca por mensalidade X** | Campo que **não** é a chave de fragmentação | Consulta em **todos** os *shards*; *mongos* mesclam o resultado |
| **Fig. 5 — índice B-*tree* por nome** | Raiz A–Z → H–N | "Maria" (inicial M) é buscada no nó intermediário **H–N** |
| **Fig. 1 (Soares) — pedidos por cliente** | *Shard* 1: 1–1.000; *shard* 2: 1.001–2.000; *shard* 3: 2.001–3.000 | Cliente 1.500 → **servidor B / *shard* 2** *(aplicação da regra, exemplo de estudo)* |

### 4.3 Cenários de aplicação *(complementação — exemplos ilustrativos elaborados para estudo; não fazem parte do material da FMU)*

| # | Imagine que você tem este problema… | Técnica indicada | Por quê |
|---|-------------------------------------|------------------|---------|
| 1 | **Um *e-commerce* cuja leitura de catálogo ficou lenta nos horários de pico, mas o banco ainda cabe em um servidor** | **Replicação** (réplicas de leitura) + índices | Distribui leituras sem dividir os dados (ver 3.2 e 3.12) |
| 2 | **Uma plataforma de telemetria que recebe bilhões de eventos por dia e uma única máquina já não aguenta a gravação** | ***Sharding* por *hash*** | Espalha escrita uniformemente; ingestão de eventos é o caso citado para *hash* |
| 3 | **Um sistema que consulta vendas sempre por faixa de data** | ***Sharding* por intervalo** | A consulta cai em poucos *shards*; atenção ao *shard* "mais recente" que concentra a escrita (ponto de equilíbrio, 3.10) |
| 4 | **Uma rede de lojas em que os dados de cada filial devem ficar em servidores separados por exigência interna** | ***Sharding* por zona** | Regras definidas pelo desenvolvedor para separar filiais |
| 5 | **Um aplicativo de campo usado em áreas sem sinal** | Replicação ***off-line*** e assíncrona | Replica quando a conexão volta (3.4) |
| 6 | **Um sistema de pagamentos em que a ordem das operações não pode inverter** | Replicação **passiva síncrona** (primário) ou ativa com ordem total | Garante a mesma ordem; custo em latência (3.5 e 3.6) |
| 7 | **Um serviço de envio de *e-mail* que precisa escalar sem guardar dados** | Replicação de **serviço** com *proxy* | Sem estado a sincronizar (3.8a) |
| 8 | **Uma aplicação global em que usuários de cada continente acessam principalmente dados da própria região** | Replicação *gossip* por **geolocalização** | Disponibilidade e baixa latência acima da consistência imediata (3.8b) |
| 9 | **Uma plataforma de sensores em que as gravações simultâneas de milhares de dispositivos sobrecarregam o fragmento "de hoje"** | *Sharding* com chave **data + dispositivo** | Distribui as gravações; custo: consultas por período acessam mais fragmentos (3.18a) |
| 10 | **Uma loja com banco centralizado em que a busca do cliente por e-mail varre a tabela inteira, mas o servidor tem folga** | **Índice** sobre o e-mail (não *sharding*) | O problema é de **localização**, não de capacidade (3.18f) |
| 11 | **Uma rede social em que uma conta muito popular sobrecarrega um único fragmento, embora todos tenham o mesmo volume** | Rever a chave/regra de distribuição e **rebalancear** (3.18b) | *Hotspot*: *hash* sozinho não resolve se as operações usam a mesma chave; adicionar máquinas pode não ajudar |
| 12 | **Um banco fragmentado em que a busca por um atributo que não é a chave de fragmentação ficou lenta** | **Índice local** (consulta em todos os *shards*) ou **índice global** (direciona a busca) | Local = *scatter/gather*; global = busca direcionada, com custo de manutenção e possível atraso (3.18f) |

---

## 5. Pontos de atenção (inconsistências e limitações do material)

1. **Caráter do material:** a unidade junta **quatro capítulos de livros diferentes** (Mengato Junior; Brandão; Pereira; e, reenviado depois, Soares — ver 5.25). Há **termos usados de forma diferente** entre eles (por exemplo, "*shard*" e "primário/secundário") e uma contradição de datação (ver 5.2). Foram mantidas as formulações originais e sinalizadas as divergências.
2. **"Sharding é novo" × "é antigo":** Brandão afirma que *sharding* é "uma arquitetura de *big data* **relativamente nova**"; Pereira diz que o conceito e a aplicação do *sharding* "**são antigos**". As afirmações se contradizem; deve-se anotar a divergência. *(Complementação:* a ideia de particionar dados entre nós é anterior ao *big data*; o que é recente é a popularização com bancos NoSQL.)*
3. **"Os dados de cada nó não são exclusivos, sendo totalmente independentes" (Brandão):** a frase se contradiz — se são independentes e autônomos, **não** compartilham dados. Mais adiante o mesmo capítulo afirma que os fragmentos "não compartilham nenhum dos mesmos dados". Interpretação adotada: **cada *shard* tem registros distintos e é independente**.
4. **Partição vertical (Brandão):** o material diz que os dados de uma partição vertical têm "linhas e colunas distintas". *Complementação:* na partição vertical, as **linhas** são, em geral, as mesmas (ligadas pela chave) e só as **colunas** são separadas.
5. **Figura 2 do *sharding* por intervalo:** o terceiro intervalo está rotulado como "**Shard 2**: >= 60"; pelo texto ("três *shards*") e pela figura, deve ser **Shard 3**.
6. **Quadro 1 de Pereira (replicação × particionamento) com linhas aparentemente invertidas:** a tabela diz que a replicação "possibilita o **dimensionamento**" e o particionamento "possibilita a **redundância**", o que **contradiz o texto imediatamente anterior** (replicação torna o sistema tolerante a falhas; *sharding* armazena subconjuntos para escalar). Na tabela de 3.13, foi seguido o texto. Vale confirmar com o professor qual leitura será cobrada.
7. **Quadro 2 (Oracle): "*sharding* permite *shards* redundantes":** conflita com a definição do mesmo material de que os *shards* são **autônomos e não compartilham dados**. A redundância vem da **replicação** combinada ao *sharding* (ver 3.13).
8. **Quadro 2: índice acessado apenas por "chave primária, chave estrangeira e *constraint unique*":** isso **não confere** com a Aula 02, em que índices são criados também sobre colunas comuns (ex.: índice sobre `nome`, Aula 02 Anexo A, e os exemplos do capítulo de Andrade). *Complementação:* chaves primárias e `UNIQUE` criam índices automaticamente, mas **qualquer coluna** pode ser indexada.
9. **Hash × intervalo (Pereira):** a seção "*Sharding* baseado em *hash*" ilustra com **IDs de 1 a 1000 em 4 faixas ordenadas (S1: 1–250…)**, que é, na prática, **divisão por intervalo**, e fala em "limite inferior inclusivo e exclusivo", que também é vocabulário de intervalo. O exemplo não demonstra o *hash*. *Complementação:* no *hash*, o valor é transformado e as faixas são sobre o **resultado do *hash***, não sobre o ID original.
10. **Cassandra: "sem controlador central" × "elege um líder com Zookeeper":** o material afirma que a arquitetura não tem controlador central nem mestre/escravo e, no parágrafo da replicação, que o Cassandra elege um líder entre os nós **com o Zookeeper**. As duas afirmações são difíceis de conciliar. *Complementação (conferir na documentação):* segundo meu conhecimento, as versões atuais do Cassandra **não dependem do Zookeeper** e coordenam membership/falhas por *gossip*; a referência a Zookeeper parece vir do artigo original (Lakshman e Malik, 2010).
11. **Terminologia do Cassandra:** o material fala em "colunas do *cluster*" na chave primária. *Complementação:* o termo técnico é **colunas de *clustering*** (que ordenam as linhas **dentro** da partição), sem relação com o *cluster* de máquinas. Também o infográfico diz que a arquitetura se baseia "no BigTable, **no Amazon Web Service** e no DynamoDB"; o que se costuma citar é o **Dynamo** (distribuição) e o **BigTable** (modelo de dados).
12. **MongoDB: "*shard* primário" e "secundário":** o texto usa "primário/secundário" tanto para *shards* quanto para réplicas e diz que o *shard* primário "contém toda a informação não fragmentada". *Complementação:* em MongoDB, o *primary shard* de um banco guarda as coleções **não fragmentadas** dele; já "primário/secundário" dentro de cada *shard* se refere aos **membros do conjunto de réplicas**.
13. **MongoDB: "os *mongos* usam as chaves primárias" (exemplo do CPF):** *Complementação:* o roteamento usa a **chave de fragmentação** (*shard key*), que pode ser ou não a chave primária. O exemplo de CPF funciona como intervalo, mas a explicação mistura os conceitos. Além disso, o material diz que a chave de fragmento é **imutável** — *conferir:* o texto é de 2020 e, segundo meu conhecimento, **versões mais recentes do MongoDB** passaram a permitir refinar a chave ou refragmentar (*resharding*); verificar na documentação da versão usada.
14. **Hadoop "várias cópias de um dado em um mesmo servidor" (Gemayel, 2016):** *Complementação (conferir na fonte):* no comportamento padrão do HDFS, as **réplicas são colocadas em nós (DataNodes) diferentes**, justamente para tolerar falhas de nó; manter cópias no mesmo servidor não protegeria contra a falha dele.
15. **BigTable "se conecta a Cassandra, HBase e MongoDB" (infográfico):** afirmação genérica. *Complementação (conferir):* o Cloud Bigtable oferece **API compatível com HBase**; com outros bancos a integração costuma se dar por **conectores/ferramentas de migração**, não por "conexão direta" como característica do produto.
16. **"Cluster remoto" (3.11):** os termos **nós-semente**, **nós de *gateway*** e "pesquisa de *cluster* cruzado" soam como descrição de um produto específico (o texto aparece logo após o ElasticSearch), embora o material os apresente como característica geral de *clusters* remotos. *Complementação:* conferir se a regra "até três nós de *gateway*" vale fora do contexto original.
17. **Fatores numéricos do material sem fonte direta no texto:** "Murmur3 de 3 a 5 vezes mais rápido", "partição ≤ 10 MB (até 100 MB)" e "até 255 *tokens* por nó" são apresentados como fatos, mas dependem de versão/configuração. Mantidos como no material.
18. **Número de réplicas e falhas bizantinas (2F+1):** *Complementação:* na literatura de tolerância a falhas bizantinas, protocolos clássicos sem assinaturas exigem **3F+1** réplicas; o **2F+1** do material pressupõe votação no FE e respostas assinadas. Registrar como pressuposto.
19. **"Saiba mais — falhas bizantinas":** a definição do quadro ("não conseguem concordar com uma estratégia para falhas catastróficas") é informal. *Complementação:* falha bizantina é aquela em que um componente se comporta de forma **arbitrária ou maliciosa**, inclusive enviando informações conflitantes a diferentes nós.
20. **Infográfico de replicação, "Passivo: os dados são divididos em cópias primárias e secundárias":** "divididos" pode confundir com *sharding*; no modelo passivo os dados são **copiados** (cada secundário tem a cópia completa), não repartidos.
21. **Replicação ativa e Cassandra/Mongo:** o material estuda **replicação ativa e passiva** no capítulo de Mengato, mas **não diz qual modelo** Cassandra e MongoDB adotam. Não foi atribuída classificação.
22. **"Hibernate Shards":** o material o recomenda como estrutura "bastante recomendada". *Complementação (conferir):* segundo meu conhecimento, é um projeto antigo, sem evolução nas versões recentes do Hibernate; tratar como exemplo histórico de *sharding* em camada de aplicação.
23. **Materiais complementares não acessados:** os **QR codes/links** das *Dicas do Professor* e dos *Saiba mais* **não foram abertos**; foram usados apenas os títulos e descrições do PDF (lista em 6). O texto da quarta *Dica* menciona *blockchain*, mas não traz conteúdo no PDF.
24. **Atividade 3 (A3):** o PDF inclui a atividade; por padrão do projeto, ela **não** foi incorporada a este arquivo.
25. **Duas versões do capítulo *Sharding*:** o capítulo reenviado (Soares) tem o **mesmo título e o mesmo livro** (*Framework de Big Data*) do usado inicialmente (Brandão), mas **autoria, estrutura, exemplos e referências diferentes** (as referências chegam a out. 2026). Não está claro se a unidade usa **uma ou as duas**. Foram **mantidos** os dois conteúdos: Brandão em 3.9–3.13 e Soares em 3.18, sem substituição. Confirmar na plataforma qual é a versão oficial.
26. **Soares dá base no material a dois pontos antes marcados como complementação:** (a) na partição **vertical** a divisão é por colunas com **atributos comuns** para reconstruir os registros (ver 5.4); (b) a chave de fragmentação **não precisa ser a chave primária** (ver 5.13). Os dois pontos passam a ter respaldo no próprio material.
27. ***Hash* (Soares × Pereira, ver 5.9):** Soares descreve o *hash* como função que **distribui valores distintos e separa valores próximos**, o que torna consultas por faixa mais custosas. Essa descrição é coerente; o exemplo de Pereira (IDs 1–1000 em faixas) ilustra **intervalo**. Usar a descrição de Soares como referência para *hash*.
28. **Índices (Soares × Quadro 2 da Oracle, ver 5.8):** Soares afirma que a escolha do índice depende de **filtros, ordenação e relacionamentos** das consultas, e não de apenas chave primária, estrangeira e *unique*; isso é compatível com a Aula 02. A restrição a esses três tipos de campo fica restrita ao quadro adaptado da Oracle.
29. **Fontes de Soares:** o exemplo bancário (20 mil tabelas, 50 bilhões de registros, 60 nós) e o GeoTP (versão 3, 2024) vêm de **trabalhos citados** (o GeoTP é um ***preprint***, sem revisão por pares confirmada no PDF). Mantidos como no material; os números não foram conferidos nas fontes.

---

## 6. Referências e conexões

### Conexões com as Aulas 01 e 02 *(complementação — conceitos explicados antes; aqui apenas ponteiros)*

| Tema desta aula | Onde foi visto | O que acrescenta agora |
|-----------------|----------------|------------------------|
| Escalabilidade horizontal, *sharding* e hash consistente | **Aula 01 §3.4** | Detalhe das **estratégias** (hash, intervalo, diretório, zona) e dos *clusters* |
| CAP, consistência eventual, BASE | **Aula 01 §3.4 e §3.5** | Consistência × disponibilidade na **replicação** (bancário × rede social) |
| *Gossip* e *vector clocks* | **Aula 01 §3.4** | *Gossip* como **arquitetura de replicação** e como **detecção de falhas** no Cassandra |
| Tipos de NoSQL: colunar, documentos | **Aula 01 §3.6 e §3.7** | Cassandra (colunar) e MongoDB (documentos) com o foco em **distribuição** |
| MapReduce e *scatter/gather* | **Aula 01 §3.4 e §3.9** | A busca por mensalidade X em **todos os *shards*** do MongoDB é um *scatter/gather* *(interpretação de estudo)* |
| Índices (B-*tree*, primário/secundário) | **Aula 02 §3.7, Anexos A e B** | **Comparação** índice × *sharding*; índice de suporte da chave de fragmento |
| `GROUP BY`/agregações | **Aula 02 §3.1–3.2** | Em bases fragmentadas, agregações precisam de **mesclagem** entre *shards* (ver *mongos*) |
| Índices: B-*tree*, *hash*, secundários | **Aula 02 §3.7** | Em dados fragmentados, **índice local × global** (3.18f) |
| ElasticSearch (*shards* e réplicas do índice de busca) | **Aula 04 §3.10** *(adiante)* | O mesmo *sharding* aplicado a **motores de busca** |

**Dependência de ideias:** replicação (3.2–3.8) → *sharding* (3.9–3.12) → combinação das duas em Cassandra e MongoDB (3.13–3.16). O capítulo de Soares (3.18) revisita *sharding*, *clusters* e índices com ênfase em *hotspot*, roteamento, disponibilidade geográfica e índice local × global.

### Aplicação profissional *(complementação)*
- **Arquitetura de dados e *cloud*:** a escolha entre **réplicas de leitura**, *sharding* e serviços gerenciados em nuvem é decisão recorrente de projeto (ver 3.11: *clusters* remotos, Kubernetes/GKE).
- **IA/ML:** clusters e armazenamento distribuído alimentam *pipelines* de dados e *feature stores* (a Aula 01 cita o caso da Uber com Cassandra); o material associa os *clusters* a **supercomputadores** para algoritmos de IA.
- **Operação:** escolha da chave de fragmentação, rebalanceamento e monitoramento são trabalhos de **planejamento e DBA/SRE** (3.10).

### Referências acadêmicas (do material)
- COULOURIS, G. *et al.* **Sistemas distribuídos**: conceitos e projeto. 5. ed. Porto Alegre: Bookman, 2013.
- TANENBAUM, A. S.; STEEN, M. **Sistemas distribuídos**: princípios e paradigmas. 2. ed. São Paulo: Pearson Prentice Hall, 2008.
- TANENBAUM, A. S.; BOS, H. **Sistemas operacionais modernos**. 4. ed. São Paulo: Pearson, 2016.
- LADIN, R. *et al.* Providing high availability using lazy replication. **ACM Transactions on Computer Systems**, v. 10, n. 4, p. 360–391, 1992.
- BRONSON, N. *et al.* TAO: Facebook's Distributed Data Store for the Social Graph. **USENIX ATC**, 2013.
- GEMAYEL, N. Analyzing Google File System and Hadoop Distributed File System. **Research Journal of Information Technology**, v. 8, n. 3, p. 66–74, 2016.
- RAMAKRISHNAN, R.; GEHRKE, J. **Sistemas de gerenciamento de banco de dados**. 3. ed. Porto Alegre: AMGH, 2011.
- CARPENTER, J.; HEWITT, E. **Cassandra**: the definitive guide. 2. ed. O'Reilly, 2016.
- BRADSHAW, S.; BRAZIL, E.; CHODOROW, K. **MongoDB**: the definitive guide. 3. ed. O'Reilly, 2019.
- BOAGLIO, F. **MongoDB**: construa novas aplicações com novas tecnologias. Casa do Código, 2015.
- BHAMRA, K. **A comparative analysis of MongoDB and Cassandra**. Dissertação (Mestrado), University of Bergen, 2017.
- LAKSHMAN, A.; MALIK, P. Cassandra: a decentralized structured storage system. **ACM SIGOPS Operating Systems Review**, v. 44, n. 2, p. 35–40, 2010.
- NAZEER, H. *et al.* Real-time text analytics pipeline using open-source big data tools. **Arxiv**, 2017.
- KEEP, M.; INGO, H. Performance Best Practices: Sharding. **MongoDB**, 2020.
- GOMES, P. C. T. O que é e como funciona um cluster? **OPServices**, 2015.
- BIANCHI, W. Entendendo e usando índices: parte 1. **DevMedia**, 2007.
- REIS, F. dos. O que são índices em bancos de dados: indexação em tabelas. **Bóson Treinamentos**, 2019.
- VERAS, M. **Virtualização**: tecnologia central do datacenter. 2. ed. Rio de Janeiro: Brasport, 2016.
- FERREIRA (2020); CASTRO (2020); ORACLE (Oracle Sharding, 2020); HIBERNATE SHARDS; SLICE (OpenJPA); IBM (WebSphere); ELASTIC (ElasticSearch 7.6); APPLIED INNOVATIONS (*Cloud servers vs. clustered cloud servers*); GOOGLE CLOUD (*Cloud Bigtable*; *Arquitetura do cluster*); AMAZON WEB SERVICE (DynamoDB); APACHE (Cassandra, HBase, Hadoop, Zookeeper); MONGODB (*Sharding reference*) — conforme listadas nas referências dos capítulos.
- **Capítulo *Sharding* (Soares, reenviado):** ELMASRI, R.; NAVATHE, S. B. **Sistemas de banco de dados**. 7. ed. São Paulo: Pearson, 2018. · FOWLER, A. **NoSQL for dummies**. Hoboken: John Wiley & Sons, 2015. · HUSSAIN, K.; HUSSAIN, F. **NoSQL essentials**: navigating the world of non-relational databases. Sonar Publishing, 2024. · KLEPPMANN, M. **Designing data-intensive applications**. Sebastopol: O'Reilly Media, 2017. · MONGODB. Sharded cluster components (2026a); Routing with mongos (2026b); Security checklist for self-managed deployments (2026c). **MongoDB Manual**. · ZHOU, X. *et al.* Grep: a graph learning based database partitioning system. **Proceedings of the ACM on Management of Data**, v. 1, n. 1, art. 94, 2023. · ZHUANG, Q. *et al.* GeoTP: latency-aware geo-distributed transaction processing in database middlewares (extended version). v. 3, 2024. Preprint.
- **Leitura recomendada (material):** LUZ, K. S.; ALMEIDA, T. V. M. **Apache Cassandra**. 2016 (Departamento de Ciência da Computação, UnB).

### Materiais complementares indicados no PDF *(links/QR codes não acessados — apenas títulos e descrições do próprio PDF)*

| Tipo | Título | Descrição do PDF |
|------|--------|------------------|
| Dica do Professor | CODA (sistema de arquivos distribuído) | Funcionalidades para o compartilhamento de arquivos |
| Saiba mais | *Cluster* de alta disponibilidade da informação com *software* livre | Tecnologias livres para *clusters*, replicação e monitoramento de falhas |
| Saiba mais | Administrando MongoDB: replicação/espelhamento | Modelo de replicação no MongoDB |
| Saiba mais (vídeo) | Sistemas distribuídos — abordagens de consistência e replicação (Jó Uyeama) | Consistência causal e sequencial; posicionamento de servidores de réplicas |
| Saiba mais | Uma introdução ao Apache Kafka, lições aprendidas em um ambiente de varejo | Kafka, replicação para desempenho no fluxo de dados (*stream*), caso de uso |
| Dica do Professor | *Sharding* em servidores clusterizados em sistemas bancários | Uso de *sharding* em *clusters* bancários |
| Saiba mais | Padrões e diretrizes arquiteturais para escalabilidade | Arquiteturas com foco em escalabilidade |
| Saiba mais | O que são índices em bancos de dados — indexação em tabelas | Conceito de índices no relacional; prós e contras |
| Dica do Professor | *Sharding* e *blockchain* | Importância do *sharding* em sistemas de *blockchain* |
| Saiba mais (vídeo) | Diferenças entre *sharding* e replicação | Diferenças entre os dois e em relação ao *clustering* |
| Saiba mais | Cassandra — um sistema de armazenamento NoSQL altamente escalável | Arquitetura e estudos de caso em redes sociais |
| Saiba mais | Sistemas de Gerenciamento de Bancos de Dados (3ª ed.) | Índices baseados em *hash*, seus tipos e utilizações |

---

## 7. Anexo A — Minhas observações e dúvida: georredundância no Azure *(observação da Dani; a ligação com o Azure é complementação, não faz parte do material da FMU)*

**Tema principal destacado por mim nesta aula:** *sharding*.

**Dúvida:** "georredundância no Azure" seria o eixo **processo** ou **fluxo** da classificação de replicação (3.4)? Conclusão a que cheguei: **não é um eixo só — é uma característica que combina os quatro**: **passivo, assíncrono, unidirecional, *on-line***.

| Eixo (3.4) | Como a georredundância (ex.: Azure Storage GRS) se encaixa *(complementação)* | Por quê |
|-----------|-------------------------------------------------------------------------|---------|
| **Processo** | **Passivo** | Há uma região **primária** que recebe as gravações; a região **secundária** é cópia (*backup*). Não é replicação ativa, em que todos executam |
| **Fluxo** | **Assíncrono** | A gravação é confirmada na região primária e **depois** copiada à secundária, sem bloquear o cliente (por isso pode haver pequeno atraso) |
| **Direção** | **Unidirecional** | Primária → secundária. Mesmo com leitura na secundária (RA-GRS), ela é **somente leitura** |
| **Conexão** | ***On-line*** (contínua) | A cópia acontece de forma contínua, não em janelas agendadas. Ressalva: *on-line* aqui significa "ao longo das operações", **não** "sem atraso" |

**Leitura da conclusão:** os quatro eixos da classificação **descrevem a mesma estratégia ao mesmo tempo**, então "georredundância" não pertence a um eixo; ela **é uma combinação**. A escolha **assíncrona** tem custo: se a região primária falhar, a cópia secundária pode estar **alguns instantes atrasada** (perda possível dos últimos dados) — é o dilema disponibilidade × consistência da Aula 01 (§3.4) e de 3.2.

> *Complementação (conferir na documentação do Azure):* segundo meu conhecimento, o armazenamento georredundante copia os dados de forma **síncrona dentro da região primária** (várias cópias) e **assíncrona para a região secundária**, sem SLA de tempo para essa cópia. O material da FMU não cita o Azure; a tabela é aplicação dos conceitos da aula.

---

## 8. Anexo B — Pontos de discussão: *sharding* × fatos e dimensões, e *sharding* × georredundância *(levantados pela Dani; análise é complementação, não faz parte do material da FMU)*

### 8.1 O infográfico de Big Data (BigTable) é o mesmo princípio de fatos e dimensões?

**Hipótese da Dani:** o princípio é o mesmo — distribuir em tabelas menores conectadas.
**Avaliação:** a intuição de "partir o dado grande em partes menores" é comum às duas ideias, mas o **princípio é diferente**. O parentesco mais próximo é com o **particionamento vertical** (3.9), não com o horizontal.

| | Fatos e dimensões (*star schema*) | *Sharding* |
|---|---|---|
| **Como divide** | Por **assunto/colunas**: cada tabela tem esquema próprio (venda, cliente, produto) | Por **linhas**: todas as partes têm o **mesmo esquema** |
| **Como as partes se relacionam** | Se **complementam** e são unidas por *join* | São **intercambiáveis**; a consulta vai a um *shard* ou a todos e os resultados são **somados** (*scatter/gather*, ver Aula 01 §3.4) |
| **Objetivo** | Modelagem para análise: clareza, desempenho do *join*, menos redundância | Escalar armazenamento e carga em várias máquinas |
| **Nível** | **Lógico** (modelo) | **Físico** (onde o dado fica) |

**Sobre o infográfico em si (3.17):**
- O BigTable é **colunar** e não faz *join*: o infográfico mostra **uma** tabela dividida em **faixas de linhas contíguas**, e não tabelas conectadas.
- O infográfico do Cassandra (3.14) usa **desnormalização e duplicação** de tabelas por tipo de consulta, o oposto do modelo dimensional.
- Pode ter gerado a associação o fato de o BigTable ser indicado para **relatórios, visualizações e séries temporais** (uso analítico, como o DW) e o contraste com a Aula 02 (relacional).

**Onde as duas ideias se encontram (*data warehouse* distribuído):**

| Tabela | Tratamento | Por quê |
|--------|-----------|---------|
| **Fatos** (enorme) | **Fragmentada** (*sharding*) | Não cabe/aguenta em um nó |
| **Dimensões** (pequenas) | **Replicadas em cada nó** | O *join* fica local, sem trafegar dado entre nós |

Isso corresponde às **tabelas de referência replicadas em cada *shard*** descritas no material (3.9; exemplo: tabela de taxas de conversão). Padrão análogo existe em serviços como o Azure Synapse (tabelas distribuídas e replicadas) — *conferir na documentação*.

### 8.2 *Sharding* × georredundância do Azure

**Georredundância é replicação, não *sharding***: copia os dados completos para outra região (passiva, assíncrona, unidirecional — Anexo A). Ninguém está dividindo os dados.

A relação é de **camadas**, como o material mostra em Cassandra e MongoDB (3.16: no MongoDB, *shard* = conjunto de réplicas):

| Camada | O que resolve | Exemplo no Azure *(conferir na documentação)* |
|--------|---------------|-----------------------------------------------|
| ***Sharding*** | Capacidade e carga acima de um servidor | Cosmos DB: dados divididos por **chave de partição** |
| **Replicação local** | Falha de nó ou disco | Cópias dentro da região |
| **Georredundância** | Falha de uma região inteira | Replicação para outra região (GRS no Storage; multirregião no Cosmos DB) |

O Cosmos DB reúne as três camadas; o Storage com GRS tem só a replicação local e a georredundância.

**Frase-resumo:** *sharding* responde "cabe e aguenta?"; georredundância responde "sobrevive se a região cair?". São complementares (ver 3.13 e 3.16).
