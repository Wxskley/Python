lista_pessoas = []  # Lista para armazenar os dados das pessoas
mais_pesadas = []  # Lista para armazenar as pessoas mais pesadas
mais_leves = []  # Lista para armazenar as pessoas mais leves

while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break

    peso = float(input("Digite o peso da pessoa: "))

    pessoa = (nome, peso)  # Cria uma tupla com o nome e peso da pessoa
    lista_pessoas.append(pessoa)  # Adiciona a tupla à lista de pessoas

    if len(mais_pesadas) == 0 or peso > mais_pesadas[0][1]:
        mais_pesadas = [pessoa]  # Atualiza a lista de pessoas mais pesadas
    elif peso == mais_pesadas[0][1]:
        mais_pesadas.append(pessoa)

    if len(mais_leves) == 0 or peso < mais_leves[0][1]:
        mais_leves = [pessoa]  # Atualiza a lista de pessoas mais leves
    elif peso == mais_leves[0][1]:
        mais_leves.append(pessoa)

quantidade_pessoas = len(lista_pessoas)

print("Quantidade de pessoas cadastradas:", quantidade_pessoas)

print("Pessoas mais pesadas:")
for pessoa in mais_pesadas:
    print("Nome:", pessoa[0], "- Peso:", pessoa[1])

print("Pessoas mais leves:")
for pessoa in mais_leves:
    print("Nome:", pessoa[0], "- Peso:", pessoa[1])
