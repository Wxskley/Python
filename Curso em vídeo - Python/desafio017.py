import math

cateto_oposto = float(
    input("Digite o comprimento do cateto oposto: ")
)  # Solicita ao usuário o comprimento do cateto oposto e converte para float
cateto_adjacente = float(
    input("Digite o comprimento do cateto adjacente: ")
)  # Solicita ao usuário o comprimento do cateto adjacente e converte para float

hipotenusa = math.sqrt(
    cateto_oposto**2 + cateto_adjacente**2
)  # Calcula a hipotenusa usando a fórmula de Pitágoras

print(
    "O comprimento da hipotenusa é: ", hipotenusa
)  # Exibe o valor da hipotenusa na tela
