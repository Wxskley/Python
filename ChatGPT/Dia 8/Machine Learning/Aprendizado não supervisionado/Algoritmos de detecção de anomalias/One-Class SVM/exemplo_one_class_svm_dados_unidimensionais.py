import numpy as np
from sklearn.svm import OneClassSVM

# Dados de exemplo
dados = np.array([1, 2, 3, 4, 1000])

# Reformatar os dados para um formato adequado
X = dados.reshape(-1, 1)

# Criação do modelo
modelo = OneClassSVM(nu=0.1)

# Treinamento do modelo
modelo.fit(X)

# Detecção de anomalias
anomalias = modelo.predict(X)

# Exibição dos resultados
for i, anomalia in enumerate(anomalias):
    if anomalia == -1:
        print(f"Dado {dados[i]} é uma anomalia")
