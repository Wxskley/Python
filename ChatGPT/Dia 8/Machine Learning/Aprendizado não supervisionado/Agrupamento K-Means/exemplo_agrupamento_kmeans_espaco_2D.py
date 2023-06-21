import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Criando alguns pontos de exemplo
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Criando o objeto KMeans com 2 grupos
kmeans = KMeans(n_clusters=2)

# Treinando o modelo
kmeans.fit(X)

# Obtendo as previsões dos grupos
previsoes = kmeans.predict(X)

# Obtendo as coordenadas dos centróides
centroides = kmeans.cluster_centers_

# Visualizando os resultados
cores = ["r", "g"]

# Percorrendo cada ponto de exemplo
for i in range(len(X)):
    # Desenhe um ponto no gráfico usando as coordenadas X e Y do ponto
    # A cor do ponto é determinada pela previsão do grupo a que pertence
    plt.scatter(X[i][0], X[i][1], c=cores[previsoes[i]], marker="o")

# Desenhe os centróides dos grupos no gráfico
plt.scatter(centroides[:, 0], centroides[:, 1], color="black", marker="x")

# Mostrar o gráfico
plt.show()
