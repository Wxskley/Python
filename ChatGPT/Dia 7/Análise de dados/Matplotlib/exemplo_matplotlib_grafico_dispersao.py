import matplotlib.pyplot as plt

# Dados para o gráfico de dispersão
x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 6, 1]

# Criação do gráfico de dispersão
plt.scatter(x, y)

# Configurações adicionais do gráfico
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de Dispersão")

# Exibição do gráfico
plt.show()
