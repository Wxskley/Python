# Algoritmo de Verificação de Palíndromo
# Este algoritmo verifica se uma palavra ou frase é um palíndromo.


def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


# Exemplo de uso:
texto1 = "arara"
resultado1 = eh_palindromo(texto1)
print(resultado1)

texto2 = "Python é legal"
resultado2 = eh_palindromo(texto2)
print(resultado2)
