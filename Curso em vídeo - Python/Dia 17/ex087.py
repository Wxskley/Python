matriz = []  # Matriz vazia para armazenar os valores
soma_pares = 0  # Variável para armazenar a soma dos valores pares
soma_terceira_coluna = (
    0  # Variável para armazenar a soma dos valores da terceira coluna
)
maior_segunda_linha = float(
    "-inf"
)  # Variável para armazenar o maior valor da segunda linha

# Preenchimento da matriz
for i in range(3):
    linha = []  # Lista para armazenar os valores da linha i

    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)  # Adiciona o valor à linha

        # Verifica se o valor é par e realiza a soma
        if valor % 2 == 0:
            soma_pares += valor

        # Verifica se é a terceira coluna e realiza a soma
        if j == 2:
            soma_terceira_coluna += valor

        # Verifica se é a segunda linha e atualiza o maior valor
        if i == 1 and valor > maior_segunda_linha:
            maior_segunda_linha = valor

    matriz.append(linha)  # Adiciona a linha à matriz

# Exibição da matriz
print("Matriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:^5}", end="")  # Centraliza o valor na coluna de largura 5
    print()  # Quebra de linha após exibir os valores da linha

# Exibição dos resultados
print("Soma dos valores pares:", soma_pares)
print("Soma dos valores da terceira coluna:", soma_terceira_coluna)
print("Maior valor da segunda linha:", maior_segunda_linha)
