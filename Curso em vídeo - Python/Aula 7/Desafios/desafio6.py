import math  # Importa o módulo math para usar a função sqrt() que calcula raiz quadrada

numero = int(
    input("Digite um número: ")
)  # Solicita ao usuário para digitar um número e o converte para inteiro

dobro = numero * 2  # Calcula o dobro do número
triplo = numero * 3  # Calcula o triplo do número
raizQuadrada = math.sqrt(
    numero
)  # Calcula a raiz quadrada do número usando a função sqrt() do módulo math

# Exibe o resultado na tela, formatando a mensagem com os valores calculados
print(
    "O número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}".format(
        numero, dobro, triplo, raizQuadrada
    )
)
