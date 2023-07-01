def ficha(nome="<desconhecido>", gols=0):
    """
    Função para exibir a ficha de um jogador.
    :param nome: Nome do jogador (opcional).
    :param gols: Quantidade de gols do jogador (opcional).
    """
    print(f"O jogador {nome} marcou {gols} gol(s).")


# Exemplo de uso da função
nome_jogador = input("Digite o nome do jogador: ")
quantidade_gols = input("Digite a quantidade de gols: ")

if quantidade_gols.isnumeric():
    quantidade_gols = int(quantidade_gols)
else:
    quantidade_gols = 0

ficha(nome_jogador, quantidade_gols)
