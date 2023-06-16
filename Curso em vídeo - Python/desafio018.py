import math

angulo = float(
    input("Digite o valor do ângulo: ")
)  # Solicita ao usuário o valor do ângulo
angulo_rad = math.radians(angulo)  # Converte o ângulo de graus para radianos

seno = math.sin(angulo_rad)  # Calcula o seno do ângulo
cosseno = math.cos(angulo_rad)  # Calcula o cosseno do ângulo
tangente = math.tan(angulo_rad)  # Calcula a tangente do ângulo

print("O seno do ângulo é: ", seno)  # Exibe o valor do seno na tela
print("O cosseno do ângulo é: ", cosseno)  # Exibe o valor do cosseno na tela
print("A tangente do ângulo é: ", tangente)  # Exibe o valor da tangente na tela
