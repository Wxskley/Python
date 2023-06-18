lado1 = float(
    input("Digite o comprimento da primeira reta: ")
)  # Solicita ao usuário o comprimento da primeira reta e armazena o valor em lado1
lado2 = float(
    input("Digite o comprimento da segunda reta: ")
)  # Solicita ao usuário o comprimento da segunda reta e armazena o valor em lado2
lado3 = float(
    input("Digite o comprimento da terceira reta: ")
)  # Solicita ao usuário o comprimento da terceira reta e armazena o valor em lado3

if (
    lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1
):  # Verifica se a soma de dois lados é maior do que o terceiro para todas as combinações possíveis
    print(
        "É possível formar um triângulo com as retas fornecidas."
    )  # Se a condição for verdadeira, imprime que é possível formar um triângulo
else:
    print(
        "Não é possível formar um triângulo com as retas fornecidas."
    )  # Caso contrário, imprime que não é possível formar um triângulo
