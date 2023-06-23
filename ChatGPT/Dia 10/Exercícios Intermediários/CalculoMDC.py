# Este algoritmo calcula o máximo divisor comum (MDC) entre dois números.
# O MDC é o maior número que divide exatamente dois números.


def gcd(a, b):
    while b != 0:
        # Trocamos o valor de a pelo valor de b e b pelo resto da divisão entre a e b
        a, b = b, a % b

    return a  # O valor de a é o MDC


print(gcd(24, 36))  # Exemplo de uso: Calcula o MDC entre 24 e 36
