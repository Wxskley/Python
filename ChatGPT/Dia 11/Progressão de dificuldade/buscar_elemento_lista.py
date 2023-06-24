# Nível de dificuldade: 55%
lista = [3, 7, 1, 9, 4, 5]
elemento = int(input("Digite o elemento a ser buscado: "))
indice = -1
for i in range(len(lista)):
    if lista[i] == elemento:
        indice = i
        break
if indice != -1:
    print("O elemento", elemento, "foi encontrado na posição", indice)
else:
    print("O elemento", elemento, "não foi encontrado na lista.")
