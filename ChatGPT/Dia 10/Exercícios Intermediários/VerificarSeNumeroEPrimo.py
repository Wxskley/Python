# Este algoritmo verifica se um número é primo.
# Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.


def is_prime(n):
    if n <= 1:
        return False  # Se o número for menor ou igual a 1, não é primo

    # Percorremos todos os números de 2 até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Se encontrarmos algum número que divide n, não é primo

    return True  # Se o número não foi divisível por nenhum outro, é primo


print(is_prime(17))  # Exemplo de uso: Verifica se o número 17 é primo
