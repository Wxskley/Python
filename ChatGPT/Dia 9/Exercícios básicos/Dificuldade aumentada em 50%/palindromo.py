# Solicita ao usuário que insira uma string
string = input("Digite uma string: ")

# Remove os espaços em branco da string
string = string.replace(" ", "")

# Verifica se a string é um palíndromo
if string == string[::-1]:
    print("A string é um palíndromo")
else:
    print("A string não é um palíndromo")
