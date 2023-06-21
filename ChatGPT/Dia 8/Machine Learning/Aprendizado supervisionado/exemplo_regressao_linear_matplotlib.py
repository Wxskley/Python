import numpy as np
import matplotlib.pyplot as plt
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

# Plotagem dos dados e da linha de regressão
plt.scatter(X, y, color="red", label="Dados")
plt.plot(X_novo, y_pred, color="blue", label="Regressão Linear")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regressão Linear")
plt.legend()
plt.show()
