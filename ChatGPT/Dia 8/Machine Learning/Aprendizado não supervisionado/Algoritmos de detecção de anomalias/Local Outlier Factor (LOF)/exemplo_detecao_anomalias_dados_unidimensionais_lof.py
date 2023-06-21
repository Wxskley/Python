import numpy as np
from sklearn.neighbors import LocalOutlierFactor

# Dados de exemplo
dados = np.array([1, 2, 3, 4, 1000])

# Reformatar os dados para um formato adequado
X = dados.reshape(-1, 1)

# Criação do modelo
modelo = LocalOutlierFactor(contamination=0.1)

# Detecção de anomalias
anomalias = modelo.fit_predict(X)

# Exibição dos resultados
for i, anomalia in enumerate(anomalias):
    if anomalia == -1:
        print(f"Dado {dados[i]} é uma anomalia")
