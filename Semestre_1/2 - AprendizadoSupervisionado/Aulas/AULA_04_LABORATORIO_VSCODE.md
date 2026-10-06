# AULA 4 — ANEXO: LABORATÓRIO PRÁTICO (VSCODE)

## Disciplina: Aprendizado de Máquina Supervisionado — Graduação em IA (FMU)

> Este anexo guia você, passo a passo, na execução do pipeline de classificação de texto (SMS Spam Collection + Naïve Bayes) no **VSCode**, sem precisar de Jupyter/Colab. A cada passo: o que fazer, por quê, e o que conferir antes de seguir para o próximo.
>
> **Como rodar cada bloco:** crie um arquivo `sms_classifier.py` na pasta do laboratório e vá colando os blocos nele, **nesta ordem**. Depois de colar um bloco, selecione o trecho novo e aperte **Shift+Enter** — o VSCode abre um terminal Python interativo e executa só aquele trecho, mostrando o resultado na hora. Isso permite ver cada etapa funcionando antes de ir para a próxima, sem precisar rodar o arquivo inteiro de novo a cada vez. Quando quiser rodar tudo de uma vez, use o botão "Run Python File" ou `python sms_classifier.py` no terminal.

---

## Passo 0 — Preparar o ambiente

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

## Passo 1 — Baixar o dataset

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

## Passo 2 — Explorar o dataset com Pandas

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

## Passo 3 — Ver o problema do ruído (opcional, só para visualizar)

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

## Passo 4 — Limpeza do texto com expressões regulares

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

## Passo 5 — Remover stopwords e aplicar stemming (NLTK)

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

## Passo 6 — Montar o vetor de features (palavras mais frequentes)

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

## Passo 7 — Vetorizar cada mensagem e binarizar os rótulos

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

## Passo 8 — Dividir em treino e teste

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

## Passo 9 — Treinar o classificador Naïve Bayes

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

## Passo 10 — Avaliar o modelo

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

## Passo 11 — Ajustar hiperparâmetros (opcional)

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

## Resumo das diferenças entre este laboratório e o código do livro

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

**Status:** anexo de laboratório da Aula 4 pronto para execução passo a passo no VSCode.
