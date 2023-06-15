largura = float(
    input("Qual a largura da parede em metros? ")
)  # Solicita ao usuário para digitar a largura da parede e converte a entrada em um número de ponto flutuante (float)
altura = float(
    input("Qual a altura da parede em metros? ")
)  # Solicita ao usuário para digitar a altura da parede e converte a entrada em um número de ponto flutuante (float)

area = altura * largura  # Calcula a área da parede multiplicando a altura pela largura

quantidadeTinta = (
    area / 2
)  # Calcula a quantidade de tinta necessária dividindo a área da parede por 2

print(
    "Você tem uma parede de {:.2f} metros quadrados e precisa de {:.2f} litros de tinta para pintá-la".format(
        area, quantidadeTinta
    )
)  # Exibe a mensagem com a área da parede e a quantidade de tinta necessária, substituindo os espaços reservados pelos valores de 'area' e 'quantidadeTinta', respectivamente
