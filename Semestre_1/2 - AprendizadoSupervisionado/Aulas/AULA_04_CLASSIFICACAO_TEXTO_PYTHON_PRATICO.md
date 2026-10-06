# AULA 4 — MATERIAL PRÁTICO: CLASSIFICAÇÃO DE TEXTO COM PYTHON (NAÏVE BAYES)

## Disciplina: Aprendizado de Máquina Supervisionado — Graduação em IA (FMU)

> Código extraído e organizado a partir do capítulo "Classificação de textos — Utilizando Python para construir e treinar modelos de machine learning" (Juliano Vieira Martins, SAGAH). O PDF original apresenta espaços indevidos dentro de identificadores Python (ex.: `word _ tokens`), provavelmente um artefato de diagramação do livro — abaixo, o código foi normalizado para sintaxe Python válida (`word_tokens`), preservando integralmente a lógica e os comentários do capítulo. Organizado em células, pronto para colar em um Jupyter Notebook / Google Colab.

---

## Célula 0 — Verificar versão do Python (opcional)

```python
!python --version
```

---

## Célula 1 — Download do dataset (SMS Spam Collection, UCI)

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

## Célula 2 — Explorar o dataset com Pandas

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

## Célula 3 — Expressões regulares: identificar caracteres especiais (exemplo informativo)

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

## Célula 4 — Limpeza do texto com regex (substituições definitivas)

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

## Célula 5 — Remoção de stopwords e stemming (NLTK)

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

## Célula 6 — Construção do vetor-modelo de features (palavras mais frequentes)

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

## Célula 7 — Vetorizar cada mensagem como vetor de features + rótulo binário

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

## Célula 8 — Dividir em treino e teste

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

## Célula 9 — Vetorizar dicionários em matriz e treinar o Naïve Bayes

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

## Célula 10 — Matriz de confusão e relatório de avaliação

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

## Célula 11 — Ajuste de hiperparâmetros com Grid Search

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

## Bibliotecas utilizadas neste capítulo (resumo)

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

**Status:** material prático da Aula 4 organizado e pronto para execução em notebook (Google Colab ou Jupyter local).
