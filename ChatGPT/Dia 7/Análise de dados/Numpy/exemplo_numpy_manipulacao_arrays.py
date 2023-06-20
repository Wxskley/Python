import numpy as np

# Criação de um array bidimensional
array = np.array([[1, 2, 3], [4, 5, 6]])

# Soma dos elementos ao longo das linhas
soma_linhas = np.sum(array, axis=1)
print("Soma das linhas:", soma_linhas)

# Produto dos elementos ao longo das colunas
produto_colunas = np.prod(array, axis=0)
print("Produto das colunas:", produto_colunas)
