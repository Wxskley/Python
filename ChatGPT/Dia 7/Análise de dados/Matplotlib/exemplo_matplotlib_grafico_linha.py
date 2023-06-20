import matplotlib.pyplot as plt

# Dados para o gráfico de barras
categorias = ["A", "B", "C", "D"]
valores = [10, 15, 7, 12]

# Criação do gráfico de barras
plt.bar(categorias, valores)

# Configurações adicionais do gráfico
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")

# Exibição do gráfico
plt.show()
