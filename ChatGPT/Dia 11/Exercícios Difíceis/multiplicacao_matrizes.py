# Algoritmo de Multiplicação de Matrizes
# Este algoritmo realiza a multiplicação de duas matrizes.


def multiplicacao_matrizes(matriz1, matriz2):
    linhas1 = len(matriz1)
    colunas1 = len(matriz1[0])
    linhas2 = len(matriz2)
    colunas2 = len(matriz2[0])

    if colunas1 != linhas2:
        return None

    resultado = [[0] * colunas2 for _ in range(linhas1)]

    for i in range(linhas1):
        for j in range(colunas2):
            for k in range(colunas1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado


# Exemplo de uso:
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8], [9, 10], [11, 12]]
resultado = multiplicacao_matrizes(matriz1, matriz2)
print(resultado)
