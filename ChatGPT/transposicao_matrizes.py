# Receber a matriz como entrada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Criar a matriz transposta
matriz_transposta = []

# Percorrer as colunas da matriz original
for coluna in range(len(matriz[0])):
    linha_transposta = []
    # Percorrer as linhas da matriz original
    for linha in range(len(matriz)):
        linha_transposta.append(matriz[linha][coluna])
    matriz_transposta.append(linha_transposta)

# Imprimir a matriz transposta
for linha in matriz_transposta:
    print(linha)
