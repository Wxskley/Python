def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número válido.")


# Exemplo de uso das funções
n = leiaInt("Digite um número inteiro: ")
print(f"O número inteiro digitado foi: {n}")

x = leiaFloat("Digite um número real: ")
print(f"O número real digitado foi: {x}")
