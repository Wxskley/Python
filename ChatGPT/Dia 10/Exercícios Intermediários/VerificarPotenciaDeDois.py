# Este algoritmo verifica se um número é uma potência de 2.


def is_power_of_two(n):
    return (
        n != 0 and (n & (n - 1)) == 0
    )  # Verificamos se o número é diferente de zero e se possui apenas um bit ligado


print(
    is_power_of_two(16)
)  # Exemplo de uso: Verifica se o número 16 é uma potência de 2
