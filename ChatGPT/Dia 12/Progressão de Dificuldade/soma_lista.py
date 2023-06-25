# Função para somar os elementos de uma lista
# Dificuldade: 20%
def soma_lista(lista):
    # Inicializa uma variável soma com valor zero
    soma = 0
    # Percorre cada elemento da lista
    for elemento in lista:
        # Adiciona o elemento à soma
        soma += elemento
    # Retorna a soma total
    return soma


# Lista de exemplo
lista = [1, 2, 3, 4, 5]
# Chama a função para somar os elementos e imprime o resultado
print(soma_lista(lista))
