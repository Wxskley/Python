# Vamos aplicar algumas operações em uma lista de números usando programação funcional

# Primeiro, importamos a função reduce do módulo functools
from functools import reduce

# Vamos criar uma lista de números
numbers = [1, 2, 3, 4, 5]

# Vamos usar a função map para calcular o quadrado de cada número
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Imprime a lista com os quadrados dos números

# Vamos usar a função filter para filtrar apenas os números pares
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Imprime a lista com os números pares

# Vamos usar a função reduce para calcular o produto de todos os números
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Imprime o produto dos números
