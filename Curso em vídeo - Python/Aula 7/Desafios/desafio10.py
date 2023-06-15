dinheiro = float(
    input("Quantos Reais você tem? ")
)  # Solicita ao usuário para digitar a quantidade de dinheiro em reais e converte a entrada em um número de ponto flutuante (float)

conversao = (
    dinheiro / 3.27
)  # Realiza a conversão de reais para dólares, dividindo a quantidade de dinheiro pela taxa de câmbio de 3.27

print(
    "Você pode comprar {:.2f} dólares".format(conversao)
)  # Exibe o resultado na tela, formatando a mensagem para mostrar a quantidade de dólares com duas casas decimais
