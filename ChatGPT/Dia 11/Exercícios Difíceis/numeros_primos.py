# Algoritmo de Números Primos
# Este algoritmo verifica se um número é primo.


def eh_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True


# Exemplo de uso:
numero1 = 17
resultado1 = eh_primo(numero1)
print(resultado1)

numero2 = 20
resultado2 = eh_primo(numero2)
print(resultado2)
