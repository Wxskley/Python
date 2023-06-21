import numpy as np
from neupy import algorithms

# Dados de exemplo
X = np.array([[0.2, 0.3], [0.4, 0.5], [0.7, 0.9]])

# Criação e treinamento da Rede Neural Competitiva
network = algorithms.CPCN(n_inputs=2, n_classes=2)
network.train(X, epsilon=0.1, epochs=100)

# Classificação dos dados
y_predicted = network.predict(X)

# Exibição dos resultados
print("Dados Originais:\n", X)
print("Classificação:\n", y_predicted)
