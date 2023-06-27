numero = input("Digite um número de 0 a 9999: ")

# Verifica se o número fornecido é maior que 9999
if int(numero) > 9999:
    print("Número inválido. Digite um número de 0 a 9999.")
else:
    # Obtém a unidade do número
    unidade = numero[-1]

    # Obtém a dezena do número, considerando que pode não existir
    dezena = numero[-2] if len(numero) >= 2 else "0"

    # Obtém a centena do número, considerando que pode não existir
    centena = numero[-3] if len(numero) >= 3 else "0"

    # Obtém o milhar do número, considerando que pode não existir
    milhar = numero[-4] if len(numero) == 4 else "0"

    # Exibe os dígitos separados
    print("Unidade:", unidade)
    print("Dezena:", dezena)
    print("Centena:", centena)
    print("Milhar:", milhar)
