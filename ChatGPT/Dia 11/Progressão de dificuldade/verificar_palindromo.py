# Nível de dificuldade: 70%
palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
