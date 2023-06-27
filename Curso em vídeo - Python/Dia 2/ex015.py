kmPercorrido = float(
    input("Quantos km foram percorridos? ")
)  # Solicita a quantidade de quilômetros percorridos ao usuário e armazena na variável kmPercorrido

diasAlugado = int(
    input("Quantos dias o carro foi alugado? ")
)  # Solicita a quantidade de dias de aluguel ao usuário e armazena na variável diasAlugado

valorDiario = (
    diasAlugado * 60
)  # Calcula o valor do aluguel por dia multiplicando a quantidade de dias alugados pela taxa diária fixa de R$60 e armazena na variável valorDiario

valorKm = (
    kmPercorrido * 0.15
)  # Calcula o valor do aluguel por quilômetro percorrido multiplicando a quantidade de quilômetros percorridos pela taxa de R$0.15 e armazena na variável valorKm

valorTotal = (
    valorDiario + valorKm
)  # Calcula o valor total a pagar somando o valor do aluguel por dia e o valor do aluguel por quilômetro e armazena na variável valorTotal

print(
    "O custo total fica R${:.2f}".format(valorTotal)
)  # Exibe na tela o valor total a pagar formatado com duas casas decimais
