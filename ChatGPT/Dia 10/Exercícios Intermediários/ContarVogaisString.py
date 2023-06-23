# Este algoritmo conta o número de vogais em uma palavra ou frase.


def count_vowels(string):
    vowels = "aeiou"  # Definimos as vogais
    count = 0

    # Percorremos a string e contamos as vogais
    for char in string.lower():
        if char in vowels:
            count += 1

    return count


print(
    count_vowels("Hello, World!")
)  # Exemplo de uso: Conta o número de vogais na frase "Hello, World!"
