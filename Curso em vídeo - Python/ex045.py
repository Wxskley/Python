import random

opcoes = ["pedra", "papel", "tesoura"]

print("Vamos jogar Jokenpô!")

jogador = input("Escolha uma opção (pedra, papel ou tesoura): ")

computador = random.choice(opcoes)

print(f"Você escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif (
    (jogador == "pedra" and computador == "tesoura")
    or (jogador == "papel" and computador == "pedra")
    or (jogador == "tesoura" and computador == "papel")
):
    print("Você venceu!")
else:
    print("Você perdeu!")
