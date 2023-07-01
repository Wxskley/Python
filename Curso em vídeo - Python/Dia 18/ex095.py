jogadores = []  # Lista para armazenar os dicionários dos jogadores

while True:
    jogador = {}  # Dicionário para armazenar as informações do jogador

    jogador["Nome"] = input("Digite o nome do jogador: ")
    partidas = int(
        input(f"Digite a quantidade de partidas jogadas por {jogador['Nome']}: ")
    )

    gols_por_partida = []  # Lista para armazenar os gols feitos em cada partida

    # Leitura da quantidade de gols feitos em cada partida
    for partida in range(partidas):
        gols = int(
            input(f"Digite a quantidade de gols feitos na partida {partida+1}: ")
        )
        gols_por_partida.append(gols)

    jogador["Gols"] = gols_por_partida
    jogador["Total de Gols"] = sum(gols_por_partida)  # Cálculo do total de gols

    jogadores.append(jogador)  # Adiciona o dicionário do jogador à lista de jogadores

    opcao = input("Deseja cadastrar mais um jogador? (S/N): ")
    if opcao.upper() == "N":
        break

# Exibição dos dados dos jogadores
print("\nDetalhes dos Jogadores:")
for jogador in jogadores:
    print("\nDados do Jogador:")
    for chave, valor in jogador.items():
        print(f"{chave}: {valor}")
