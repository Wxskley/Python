# Inicialização das variáveis de contagem
maiores_18 = 0
homens_cadastrados = 0
mulheres_menos_20 = 0

while True:
    # Solicita a idade e o sexo da pessoa
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo [M/F]: ").upper()

    # Verifica as condições e incrementa as contagens correspondentes
    if idade > 18:
        maiores_18 += 1

    if sexo == "M":
        homens_cadastrados += 1
    elif sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

    # Pergunta ao usuário se deseja continuar cadastrando pessoas
    opcao = input("Deseja continuar? [S/N]: ").upper()
    if opcao == "N":
        break

# Exibe os resultados finais
print(f"Quantidade de pessoas com mais de 18 anos: {maiores_18}")
print(f"Quantidade de homens cadastrados: {homens_cadastrados}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
