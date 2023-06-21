import numpy as np
from sklearn.decomposition import PCA

# Criando uma matriz de exemplo
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Criando o objeto PCA com 2 componentes
pca = PCA(n_components=2)

# Aplicando o PCA aos dados
X_pca = pca.fit_transform(X)

# Exibindo os dados transformados
print(X_pca)
