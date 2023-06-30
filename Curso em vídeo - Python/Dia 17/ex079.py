# Lista para armazenar os valores únicos
valores = []

# Loop para ler os valores
while True:
    valor = int(input("Digite um valor (ou 0 para sair): "))

    if valor == 0:
        break

    if valor not in valores:
        valores.append(valor)

# Ordenar os valores em ordem crescente
valores.sort()

# Exibir os valores únicos em ordem crescente
print("Valores únicos digitados em ordem crescente:")
for valor in valores:
    print(valor)
