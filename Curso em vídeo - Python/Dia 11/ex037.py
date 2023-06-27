numero = int(input("Digite um número inteiro: "))
base = int(
    input(
        "Escolha a base de conversão:\n1 para binário\n2 para octal\n3 para hexadecimal\n"
    )
)

if base == 1:
    resultado = bin(numero)  # Converte o número para binário
elif base == 2:
    resultado = oct(numero)  # Converte o número para octal
elif base == 3:
    resultado = hex(numero)  # Converte o número para hexadecimal
else:
    resultado = "Opção inválida"

print("O resultado da conversão é:", resultado)
