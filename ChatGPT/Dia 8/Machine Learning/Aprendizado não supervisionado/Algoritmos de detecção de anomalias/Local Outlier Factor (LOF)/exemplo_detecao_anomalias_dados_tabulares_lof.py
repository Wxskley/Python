import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

# Dados de exemplo em formato de DataFrame
df = pd.DataFrame(
    {
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [2, 3, 4, 5, 6],
        "feature3": [3, 4, 5, 6, 7],
    }
)

# Seleção das colunas com as features
X = df[["feature1", "feature2", "feature3"]]

# Criação do modelo
modelo = LocalOutlierFactor(contamination=0.1)

# Detecção de anomalias
anomalias = modelo.fit_predict(X)

# Exibição dos resultados
df["anomalia"] = anomalias
print(df)
