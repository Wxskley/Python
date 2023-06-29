# Tupla com os 20 primeiros colocados do Campeonato Brasileiro
colocados = (
    "Flamengo",
    "Atlético-MG",
    "Palmeiras",
    "Fortaleza",
    "Bragantino",
    "Corinthians",
    "Internacional",
    "Fluminense",
    "Athletico-PR",
    "Cuiabá",
    "Atlético-GO",
    "São Paulo",
    "Ceará",
    "Juventude",
    "Santos",
    "Bahia",
    "Grêmio",
    "Sport",
    "América-MG",
    "Chapecoense",
)

# Exibe os 5 primeiros colocados
print("Os 5 primeiros colocados são:", colocados[:5])

# Exibe os últimos 4 colocados
print("Os últimos 4 colocados são:", colocados[-4:])

# Cria uma lista com os times em ordem alfabética
times_ordem_alfabetica = sorted(colocados)
print("Times em ordem alfabética:", times_ordem_alfabetica)

# Verifica a posição da Chapecoense na tabela
posicao_chapecoense = colocados.index("Chapecoense") + 1
print("A Chapecoense está na posição:", posicao_chapecoense)
