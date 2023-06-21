import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits

# Carregando o conjunto de dados de dígitos escritos à mão
digits = load_digits()
X = digits.data

# Criando o objeto KMeans com 10 grupos
kmeans = KMeans(n_clusters=10)

# Treinando o modelo
kmeans.fit(X)

# Obtendo as previsões dos grupos
previsoes = kmeans.predict(X)

# Visualizando alguns exemplos de imagens e seus respectivos grupos
fig, axs = plt.subplots(2, 5, figsize=(8, 3))
axs = axs.flatten()

# Percorrendo cada grupo
for i in range(10):
    # Mostrando a primeira imagem do grupo no gráfico
    axs[i].imshow(X[previsoes == i][0].reshape(8, 8), cmap="gray")
    axs[i].set_title(f"Grupo {i}")

# Ajustando o layout do gráfico
plt.tight_layout()
# Mostrando o gráfico
plt.show()
