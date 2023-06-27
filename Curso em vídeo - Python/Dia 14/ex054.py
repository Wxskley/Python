from datetime import date

ano_atual = date.today().year  # Obtém o ano atual

maioridade = 18  # Idade considerada como maioridade

menores = 0  # Variável para contar o número de pessoas menores de idade
maiores = 0  # Variável para contar o número de pessoas maiores de idade

for i in range(1, 8):  # Loop para ler os sete anos de nascimento
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
    idade = ano_atual - ano_nascimento  # Calcula a idade da pessoa

    if idade < maioridade:
        menores += 1  # Incrementa o contador de menores de idade
    else:
        maiores += 1  # Incrementa o contador de maiores de idade

# Imprime o resultado
print(f"\nQuantidade de pessoas menores de idade: {menores}")
print(f"Quantidade de pessoas maiores de idade: {maiores}")
