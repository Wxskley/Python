import math

# Importa o módulo math


def is_palindrome(word):
    # Função que verifica se uma palavra é um palíndromo
    j = len(word) - 1
    result = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            result = result + 1
        if i >= j:
            break
        j = j - 1
    if result == math.ceil(len(word) / 2):
        # Verifica se a quantidade de caracteres iguais é igual à metade do tamanho da palavra
        return True
    else:
        return False


def is_palindrome_recursive(word):
    # Função recursiva que verifica se uma palavra é um palíndromo
    print(word)
    if len(word) <= 1:
        # Caso base: se a palavra tem tamanho menor ou igual a 1, é um palíndromo
        return True
    else:
        # Verifica se o primeiro e último caracteres da palavra são iguais e chama a função recursivamente
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])


words = ["arara", "racecar", "carro", "cama", "level"]
# Lista de palavras a serem verificadas

for word in words:
    print(word)
    # Imprime a palavra atual
    print(is_palindrome_recursive(word))
    # Chama a função is_palindrome_recursive para verificar se a palavra é um palíndromo
    print("\n")
