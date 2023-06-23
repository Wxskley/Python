# Este algoritmo gera os primeiros N números da sequência de Fibonacci.


def fibonacci(n):
    sequence = [0, 1]  # Definimos os dois primeiros números da sequência

    # Geramos os próximos números somando os dois últimos
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


print(
    fibonacci(10)
)  # Exemplo de uso: Gera os primeiros 10 números da sequência de Fibonacci
