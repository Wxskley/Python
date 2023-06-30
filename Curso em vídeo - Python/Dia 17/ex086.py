matriz = []  # Matriz vazia para armazenar os valores

# Preenchimento da matriz
for i in range(3):
    linha = []  # Lista para armazenar os valores da linha i

    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)  # Adiciona o valor à linha

    matriz.append(linha)  # Adiciona a linha à matriz

# Exibição da matriz
print("Matriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:^5}", end="")  # Centraliza o valor na coluna de largura 5
    print()  # Quebra de linha após exibir os valores da linha
