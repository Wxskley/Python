import pandas as pd
from sklearn.svm import OneClassSVM

# Dados de exemplo
dados = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [2, 3, 4, 5, 6],
    "feature3": [3, 4, 5, 6, 7],
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Seleção das colunas com as features
X = df[["feature1", "feature2", "feature3"]]

# Criação do modelo
modelo = OneClassSVM(nu=0.1)

# Treinamento do modelo
modelo.fit(X)

# Detecção de anomalias
anomalias = modelo.predict(X)

# Exibição dos resultados
df["anomalia"] = anomalias
print(df)
