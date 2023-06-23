# Vamos resolver o Problema da Mochila 0/1 usando programação dinâmica
# Dado um conjunto de itens com pesos e valores, queremos encontrar
# a combinação de itens que maximize o valor total, sem exceder a capacidade da mochila

# Vamos criar uma lista de pesos e valores dos itens
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]


# Agora, vamos implementar o algoritmo
def knapsack(weights, values, capacity):
    n = len(weights)
    # Criamos uma matriz para armazenar os valores máximos possíveis para diferentes capacidades
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Preenchemos a matriz com os valores máximos possíveis
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                # Se o peso do item atual é menor ou igual à capacidade atual da mochila,
                # podemos considerar incluir esse item na solução
                dp[i][j] = max(
                    values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j]
                )
            else:
                # Caso contrário, não podemos incluir o item na solução
                dp[i][j] = dp[i - 1][j]

    # O valor máximo possível estará na célula dp[n][capacity]
    return dp[n][capacity]


# Vamos calcular o valor máximo possível para uma capacidade específica
capacity = 8
max_value = knapsack(weights, values, capacity)
print(max_value)
