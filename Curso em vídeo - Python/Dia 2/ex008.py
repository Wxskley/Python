medida = float(
    input("Digite o valor em metros: ")
)  # Solicita ao usuário para digitar um valor em metros e converte para um número de ponto flutuante (float)

centimetros = medida * 100  # Converte a medida de metros para centímetros
milimetros = medida * 1000  # Converte a medida de metros para milímetros

# Exibe o resultado na tela, formatando a mensagem com os valores calculados
print(
    "A medida em centímetros é {} e em milímetros é {}".format(centimetros, milimetros)
)
