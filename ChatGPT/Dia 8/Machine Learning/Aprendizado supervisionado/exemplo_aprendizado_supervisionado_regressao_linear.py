import numpy as np
from sklearn.linear_model import LinearRegression

# Dados de exemplo
X = np.array([[1], [2], [3], [4], [5]])  # Variável preditora
y = np.array([2, 4, 6, 8, 10])  # Variável alvo

# Criação do modelo de regressão linear
modelo = LinearRegression()

# Treinamento do modelo
modelo.fit(X, y)

# Realizando predições
X_novo = np.array([[6], [7], [8]])  # Novos dados a serem previstos
y_pred = modelo.predict(X_novo)

# Exibindo os resultados
for i, x in enumerate(X_novo):
    print(f"Para x = {x}, a predição é y = {y_pred[i]}")
