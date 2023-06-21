import pandas as pd
from sklearn.ensemble import IsolationForest

# Exemplo de dados
data = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [2, 4, 6, 8, 10],
    "feature3": [3, 6, 9, 12, 15],
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Seleção das colunas com as features
X = df[["feature1", "feature2", "feature3"]]

# Criação do modelo
modelo = IsolationForest(contamination=0.1)

# Treinamento do modelo
modelo.fit(X)

# Detecção de anomalias
anomalias = modelo.predict(X)

# Exibição dos resultados
df["anomalia"] = anomalias
print(df)
