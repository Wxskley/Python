valores = [[], []]  # Lista única para armazenar os valores pares e ímpares

for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))

    if valor % 2 == 0:  # Verifica se o valor é par
        valores[0].append(valor)  # Adiciona o valor par à primeira lista
    else:
        valores[1].append(valor)  # Adiciona o valor ímpar à segunda lista

valores[0].sort()  # Ordena a lista de valores pares em ordem crescente
valores[1].sort()  # Ordena a lista de valores ímpares em ordem crescente

print("Valores pares em ordem crescente:", valores[0])
print("Valores ímpares em ordem crescente:", valores[1])
