import math  # Importação da biblioteca math para utilizar a função trunc.

numero = float(
    input("Digite um valor real: ")
)  # Solicita ao usuário que digite um valor real e armazena na variável 'numero'.
numero = math.trunc(
    numero
)  # Utiliza a função trunc da biblioteca math para obter a porção inteira do número digitado.
print(numero)  # Imprime na tela a porção inteira do número.
