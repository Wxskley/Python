# Este algoritmo calcula o fatorial de um número.
# O fatorial de um número é o produto de todos os números inteiros positivos menores ou iguais a ele.


def factorial(n):
    if n == 0:
        return 1  # O fatorial de 0 é 1

    # Chamamos a função recursivamente para calcular o fatorial do número anterior
    return n * factorial(n - 1)


print(factorial(5))  # Exemplo de uso: Calcula o fatorial de 5
