n1 = float(
    input("Digite sua primeira nota: ")
)  # Solicita ao usuário para digitar a primeira nota e converte para um número de ponto flutuante (float)
n2 = float(
    input("Digite sua segunda nota: ")
)  # Solicita ao usuário para digitar a segunda nota e converte para um número de ponto flutuante (float)

media = (n1 + n2) / 2  # Calcula a média das duas notas

# Exibe o resultado na tela, formatando a mensagem com a média com duas casas decimais
print("A sua média foi {:.2f}".format(media))
