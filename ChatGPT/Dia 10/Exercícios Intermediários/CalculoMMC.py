# Este algoritmo calcula o mínimo múltiplo comum (MMC) entre dois números.
# O MMC é o menor número que é múltiplo comum de dois números.
from CalculoMDC import *


def lcm(a, b):
    # Calculamos o MMC usando a fórmula do produto entre os números dividido pelo MDC
    return (a * b) // gcd(a, b)


print(lcm(24, 36))  # Exemplo de uso: Calcula o MMC entre 24 e 36
