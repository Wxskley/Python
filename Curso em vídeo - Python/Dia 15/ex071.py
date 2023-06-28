# Solicita o valor a ser sacado
valor_saque = int(input("Digite o valor a ser sacado: "))

# Inicializa a contagem das cédulas
cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0

# Verifica a quantidade de cédulas de cada valor
while valor_saque > 0:
    if valor_saque >= 50:
        cedulas_50 += 1
        valor_saque -= 50
    elif valor_saque >= 20:
        cedulas_20 += 1
        valor_saque -= 20
    elif valor_saque >= 10:
        cedulas_10 += 1
        valor_saque -= 10
    else:
        cedulas_1 += 1
        valor_saque -= 1

# Exibe a quantidade de cédulas de cada valor
print("Quantidade de cédulas:")
print(f"R$50: {cedulas_50}")
print(f"R$20: {cedulas_20}")
print(f"R$10: {cedulas_10}")
print(f"R$1: {cedulas_1}")
