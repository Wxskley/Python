import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Dados de exemplo
np.random.seed(42)
dados_normais = np.random.normal(0, 0.5, 1000).reshape(-1, 1)
dados_anomalia = np.random.normal(4, 0.5, 50).reshape(-1, 1)
dados = np.vstack((dados_normais, dados_anomalia))

# Criação do modelo
modelo = IsolationForest(contamination=0.05)

# Treinamento do modelo
modelo.fit(dados)

# Pontuação de anomalia para cada instância
pontuacao_anomalia = modelo.decision_function(dados)

# Plot dos dados e das anomalias
plt.scatter(range(len(dados)), dados, c=pontuacao_anomalia, cmap="viridis")
plt.colorbar(label="Pontuação de Anomalia")
plt.xlabel("Índice da Instância")
plt.ylabel("Valor")
plt.show()
