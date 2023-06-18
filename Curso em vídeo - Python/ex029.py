velocidade = float(
    input("Insira a velocidade do carro: ")
)  # Lê a velocidade do carro informada pelo usuário

multa = (
    velocidade - 80
) * 7  # Calcula o valor da multa, considerando R$7 por cada km acima do limite de 80 km/h

if velocidade > 80:
    # Se a velocidade for maior que 80 km/h, o motorista foi multado
    print("Você foi multado!")
    print(
        f"A multa foi de R${multa:.2f}"
    )  # Exibe o valor da multa formatado com duas casas decimais
else:
    # Caso contrário, o motorista está dentro do limite de velocidade
    print("Você está dentro do limite de velocidade!")
