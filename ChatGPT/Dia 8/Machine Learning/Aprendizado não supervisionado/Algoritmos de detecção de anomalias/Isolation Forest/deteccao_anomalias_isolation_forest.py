from sklearn.ensemble import IsolationForest

# Dados de exemplo
dados = [[1], [2], [3], [4], [5], [10]]

# Criação do modelo
modelo = IsolationForest(contamination=0.2)

# Treinamento do modelo
modelo.fit(dados)

# Detecção de anomalias
anomalias = modelo.predict(dados)

# Exibição dos resultados
for i, anomalia in enumerate(anomalias):
    if anomalia == -1:
        print(f"Instância {i+1} é uma anomalia.")
    else:
        print(f"Instância {i+1} é normal.")
