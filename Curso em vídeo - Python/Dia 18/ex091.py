import random

# Dicionário para armazenar os resultados dos jogadores
resultados = {}

# Simula os lançamentos dos dados para cada jogador
for jogador in range(1, 5):
    resultado = random.randint(
        1, 6
    )  # Gera um número aleatório entre 1 e 6 (resultado do dado)
    resultados[f"Jogador {jogador}"] = resultado  # Armazena o resultado no dicionário

# Ordena o dicionário em ordem decrescente com base nos valores (resultados)
resultados_ordenados = dict(
    sorted(resultados.items(), key=lambda x: x[1], reverse=True)
)

# Exibe na tela o resultado ordenado
print("Resultado:")
for jogador, resultado in resultados_ordenados.items():
    print(f"{jogador}: {resultado}")
