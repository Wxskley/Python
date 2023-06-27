lado1 = float(
    input("Digite o comprimento da primeira reta: ")
)  # Lê o comprimento da primeira reta
lado2 = float(
    input("Digite o comprimento da segunda reta: ")
)  # Lê o comprimento da segunda reta
lado3 = float(
    input("Digite o comprimento da terceira reta: ")
)  # Lê o comprimento da terceira reta

# Verifica se é possível formar um triângulo com as retas fornecidas
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É possível formar um triângulo com as retas fornecidas.")

    # Verifica o tipo de triângulo baseado nas medidas dos lados
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero: todos os lados são iguais.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles: possui dois lados iguais.")
    else:
        print("O triângulo é escaleno: todos os lados são diferentes.")
else:
    print("Não é possível formar um triângulo com as retas fornecidas.")
