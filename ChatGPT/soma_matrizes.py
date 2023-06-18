# Definição das matrizes
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Criação da matriz resultado
matriz_soma = []

# Percorrendo as linhas e colunas das matrizes
for i in range(len(matriz1)):
    linha_soma = []  # Cria uma nova lista para armazenar a linha da matriz resultado
    for j in range(len(matriz1[0])):
        elemento_soma = (
            matriz1[i][j] + matriz2[i][j]
        )  # Soma os elementos correspondentes das matrizes
        linha_soma.append(
            elemento_soma
        )  # Adiciona o elemento somado à linha da matriz resultado
    matriz_soma.append(linha_soma)  # Adiciona a linha completa à matriz resultado

# Imprimindo a matriz resultado
for linha in matriz_soma:
    print(linha)
