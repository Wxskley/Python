# Algoritmo de Regressão Linear
# Este algoritmo ajusta um conjunto de pontos a uma linha reta utilizando regressão linear.


def regressao_linear(pontos):
    n = len(pontos)
    soma_x = 0
    soma_y = 0
    soma_xy = 0
    soma_x2 = 0

    for x, y in pontos:
        soma_x += x
        soma_y += y
        soma_xy += x * y
        soma_x2 += x**2

    media_x = soma_x / n
    media_y = soma_y / n

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
    b = media_y - a * media_x

    return a, b


# Exemplo de uso:
pontos = [(1, 2), (2, 3), (3, 4), (4, 5)]
coeficientes = regressao_linear(pontos)
print(coeficientes)
