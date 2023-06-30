import random

quantidade_jogos = int(input("Quantos jogos você deseja gerar? "))

jogos = []  # Lista composta para armazenar os jogos gerados

for _ in range(quantidade_jogos):
    jogo = []  # Lista para armazenar os números de um jogo

    while len(jogo) < 6:
        numero = random.randint(1, 60)

        if numero not in jogo:
            jogo.append(numero)

    jogo.sort()  # Ordena os números do jogo em ordem crescente
    jogos.append(jogo)  # Adiciona o jogo à lista de jogos

# Exibição dos jogos gerados
print("Jogos gerados:")
for jogo in jogos:
    print(jogo)
