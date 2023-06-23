# Este algoritmo verifica se uma palavra ou frase é um palíndromo.
# Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma tanto da esquerda para a direita quanto vice-versa.


def is_palindrome(string):
    string = string.lower().replace(
        " ", ""
    )  # Convertemos a string para minúsculas e removemos os espaços em branco
    return string == string[::-1]  # Comparamos a string original com ela invertida


print(
    is_palindrome("radar")
)  # Exemplo de uso: Verifica se a palavra "radar" é um palíndromo
