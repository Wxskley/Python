import numpy as np
from minisom import MiniSom

# Dados de exemplo
X = np.random.rand(100, 2)  # 100 amostras de dados bidimensionais

# Criação e treinamento do SOM
som = MiniSom(10, 10, 2, sigma=1.0, learning_rate=0.5)
som.train_batch(X, 100)

# Visualização do SOM
import matplotlib.pyplot as plt

plt.pcolor(som.distance_map().T, cmap="bone_r")
plt.colorbar()
plt.show()
