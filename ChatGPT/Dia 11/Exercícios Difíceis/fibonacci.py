# Algoritmo de Fibonacci
# Este algoritmo gera a sequência de Fibonacci até um determinado número.


def fibonacci(n):
    sequencia = [0, 1]

    while sequencia[-1] < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)

    return sequencia


# Exemplo de uso:
limite = 100
sequencia_fibonacci = fibonacci(limite)
print(sequencia_fibonacci)
