import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Criando uma matriz de exemplo
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Criando o objeto PCA com 2 componentes
pca = PCA(n_components=2)

# Aplicando o PCA aos dados
X_pca = pca.fit_transform(X)

# Obtendo os componentes principais
componentes = pca.components_

# Visualizando os componentes principais
plt.scatter(componentes[:, 0], componentes[:, 1])
plt.xlabel("Primeiro Componente Principal")
plt.ylabel("Segundo Componente Principal")
plt.show()
