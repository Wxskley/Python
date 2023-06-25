# Função para buscar um valor em uma lista
# Dificuldade: 25%
def buscar_elemento(lista, valor):
    # Percorre cada elemento da lista
    for elemento in lista:
        # Verifica se o elemento é igual ao valor buscado
        if elemento == valor:
            # Se encontrou, retorna True
            return True
    # Se chegou ao final da lista sem encontrar, retorna False
    return False


# Lista de exemplo
lista = [5, 10, 15, 20, 25]
# Valor a ser buscado
valor = 15
# Chama a função para buscar o valor na lista e imprime o resultado
print(buscar_elemento(lista, valor))
