frase = input("Digite uma frase: ")  # Solicita ao usuário que digite uma frase

frase = frase.replace(" ", "")  # Remove os espaços em branco da frase

frase_invertida = frase[::-1]  # Inverte a ordem dos caracteres da frase

if frase == frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
