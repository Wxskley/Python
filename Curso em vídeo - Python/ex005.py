# Solicita ao usuário para digitar um valor
numero = int(input("Digite um valor: "))  # Armazena o valor fornecido pelo usuário

# Calcula o sucessor e o antecessor do valor digitado
sucessor = numero + 1  # Calcula o sucessor adicionando 1 ao número
antecessor = numero - 1  # Calcula o antecessor subtraindo 1 do número

# Exibe o resultado na tela
print(
    "O número digitado foi {}, seu sucessor é {} e seu antecessor é {}".format(
        numero, sucessor, antecessor
    )
)
