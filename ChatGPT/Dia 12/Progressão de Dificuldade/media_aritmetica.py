# Função para calcular a média aritmética de uma lista de números
# Dificuldade: 50%
def calcular_media(lista):
    # Calcula a soma dos elementos da lista
    soma = sum(lista)
    # Calcula a quantidade de elementos na lista
    quantidade = len(lista)
    # Calcula a média dividindo a soma pela quantidade de elementos
    media = soma / quantidade
    # Retorna a média
    return media


# Lista de números de exemplo
lista = [5, 7, 3, 9, 2]
# Chama a função para calcular a média aritmética e imprime o resultado
print(calcular_media(lista))
