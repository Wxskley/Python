jogador = {}  # Dicionário para armazenar as informações do jogador

jogador["Nome"] = input("Digite o nome do jogador: ")
partidas = int(
    input(f"Digite a quantidade de partidas jogadas por {jogador['Nome']}: ")
)

gols_por_partida = []  # Lista para armazenar os gols feitos em cada partida

# Leitura da quantidade de gols feitos em cada partida
for partida in range(partidas):
    gols = int(input(f"Digite a quantidade de gols feitos na partida {partida+1}: "))
    gols_por_partida.append(gols)

jogador["Gols"] = gols_por_partida
jogador["Total de Gols"] = sum(gols_por_partida)  # Cálculo do total de gols

# Exibição dos dados
print("\nDados do Jogador:")
for chave, valor in jogador.items():
    print(f"{chave}: {valor}")
