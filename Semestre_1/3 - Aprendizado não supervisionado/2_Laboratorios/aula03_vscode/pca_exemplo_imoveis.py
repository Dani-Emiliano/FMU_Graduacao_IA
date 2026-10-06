# %% [markdown]
# # PCA em linguagem prática: exemplo dos imóveis
# Exemplo FICTÍCIO e pequeno (10 imóveis), feito para você enxergar o que a PCA entrega.
# Execute célula por célula (Shift+Enter) ou rode o arquivo inteiro.

# %% 1. A planilha: 10 imóveis, 5 colunas
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

imoveis = pd.DataFrame({
    "area_m2":      [45, 52, 60, 75, 80, 95, 110, 130, 150, 180],
    "quartos":      [1, 2, 2, 2, 3, 3, 3, 4, 4, 5],
    "banheiros":    [1, 1, 1, 2, 2, 2, 3, 3, 4, 4],
    "valor_mil_rs": [280, 320, 360, 450, 500, 610, 700, 820, 980, 1200],
    "dist_centro_km": [12, 3, 8, 15, 5, 10, 2, 14, 4, 9],
}, index=[f"Imóvel {i}" for i in range(1, 11)])
print(imoveis)

# %% 2. Quais colunas "andam juntas"? (correlação: perto de 1 = andam juntas)
print(imoveis.corr().round(2))

# %% 3. Colocar tudo na mesma régua e rodar a PCA
X = StandardScaler().fit_transform(imoveis)
pca = PCA().fit(X)

# %% 4. Quanta informação cada coluna-resumo (componente) guarda?
tabela = pd.DataFrame({
    "informação guardada (%)": pca.explained_variance_ratio_ * 100,
    "acumulada (%)": pca.explained_variance_ratio_.cumsum() * 100,
}, index=[f"PC{i+1}" for i in range(X.shape[1])])
print(tabela.round(1))

# %% 5. A "receita" de cada coluna-resumo (cargas): quanto de cada coluna original entra
receita = pd.DataFrame(pca.components_[:2].T, index=imoveis.columns, columns=["PC1", "PC2"])
print(receita.round(2))

# %% 6. A "nota" de cada imóvel nas duas colunas novas (scores)
notas = pd.DataFrame(pca.transform(X)[:, :2], index=imoveis.index, columns=["PC1", "PC2"])
print(notas.round(2))
# Interpretação (feita por você): PC1 ≈ "porte do imóvel" (área, quartos, banheiros, valor).
# PC2 ≈ "localização" (distância ao centro). Dar nome ao componente é interpretação, não resultado.

# %% 7. Quanto se perde ao ficar só com 2 colunas em vez de 5?
pca2 = PCA(n_components=2).fit(X)
X_aprox = pca2.inverse_transform(pca2.transform(X))
erro = np.abs(X - X_aprox).mean()
print(f"Informação mantida com 2 componentes: {pca2.explained_variance_ratio_.sum():.1%}")
print(f"Erro médio por célula da tabela (em desvios-padrão): {erro:.2f}")
