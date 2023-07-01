pessoas = []  # Lista para armazenar os dicionários das pessoas

while True:
    pessoa = {}  # Dicionário para armazenar os dados de cada pessoa

    pessoa["Nome"] = input("Digite o nome da pessoa: ")
    pessoa["Sexo"] = input("Digite o sexo da pessoa (M/F): ")
    pessoa["Idade"] = int(input("Digite a idade da pessoa: "))

    pessoas.append(pessoa)  # Adiciona o dicionário da pessoa à lista de pessoas

    opcao = input("Deseja cadastrar mais uma pessoa? (S/N): ")
    if opcao.upper() == "N":
        break

# Número de pessoas cadastradas
total_pessoas = len(pessoas)

# Cálculo da média de idade
soma_idades = sum(pessoa["Idade"] for pessoa in pessoas)
media_idade = soma_idades / total_pessoas

# Listas para armazenar as mulheres e pessoas acima da média de idade
mulheres = []
acima_da_media = []

# Percorre a lista de pessoas e realiza as devidas adições às listas
for pessoa in pessoas:
    if pessoa["Sexo"].upper() == "F":
        mulheres.append(pessoa)
    if pessoa["Idade"] > media_idade:
        acima_da_media.append(pessoa)

# Exibição das informações
print(f"Total de pessoas cadastradas: {total_pessoas}")
print(f"Média de idade do grupo: {media_idade:.1f}")

print("\nLista de mulheres:")
for mulher in mulheres:
    print(mulher)

print("\nLista de pessoas acima da média de idade:")
for pessoa in acima_da_media:
    print(pessoa)
