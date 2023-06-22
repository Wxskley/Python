# Função de busca binária
def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return True
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return False


# Lista ordenada
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Elemento a ser buscado
elemento = int(input("Digite um número: "))

# Verifica se o elemento está presente na lista
if busca_binaria(lista, elemento):
    print("O elemento está presente na lista")
else:
    print("O elemento não está presente na lista")
