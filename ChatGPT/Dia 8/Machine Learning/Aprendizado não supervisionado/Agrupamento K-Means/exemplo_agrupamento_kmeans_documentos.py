import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# Lista de documentos de exemplo
documents = [
    "Eu gosto de comer maçãs",
    "Eu tenho uma maçã vermelha",
    "A maçã é uma fruta deliciosa",
    "Gosto de bananas",
    "Eu não gosto de brócolis",
]

# Vetorizando os documentos usando TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Criando o objeto KMeans com 2 grupos
kmeans = KMeans(n_clusters=2)

# Treinando o modelo
kmeans.fit(X)

# Obtendo as previsões dos grupos
previsoes = kmeans.predict(X)

# Visualizando os resultados
colors = ["r", "g"]

# Percorrendo cada documento
for i in range(len(documents)):
    # Mostrando a posição do documento no gráfico, com cores diferentes para cada grupo
    plt.scatter(X[i, 0], X[i, 1], c=colors[previsoes[i]], marker="o")

# Mostrando o gráfico
plt.show()
