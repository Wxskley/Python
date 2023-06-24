# Algoritmo 6: Cálculo da média de uma lista
# Nível de dificuldade: 35%
lista = [4, 6, 8, 2, 9, 5]
soma = 0
for num in lista:
    soma += num
media = soma / len(lista)
print("A média da lista é:", media)
