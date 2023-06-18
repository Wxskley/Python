# Definição das matrizes
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8], [9, 10], [11, 12]]

# Criação da matriz resultado
matriz_resultado = []

# Percorrendo as linhas de matriz1 e colunas de matriz2
for i in range(len(matriz1)):
    linha_resultado = []
    for j in range(len(matriz2[0])):
        soma_produto = 0

        # Realizando a multiplicação das matrizes
        for k in range(len(matriz2)):
            # Multiplica os elementos correspondentes de matriz1 e matriz2
            # e acumula a soma no valor de soma_produto
            soma_produto += matriz1[i][k] * matriz2[k][j]

        # Adicionando o resultado da soma dos produtos à linha_resultado
        linha_resultado.append(soma_produto)

    # Adicionando a linha_resultado à matriz_resultado
    matriz_resultado.append(linha_resultado)

# Imprimindo a matriz resultado
for linha in matriz_resultado:
    print(linha)
