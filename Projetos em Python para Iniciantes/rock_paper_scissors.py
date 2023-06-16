import random

user_points = 0  # Variável para armazenar a pontuação do jogador
computer_points = 0  # Variável para armazenar a pontuação do computador

options = [
    "r",
    "t",
    "p",
]  # Lista de opções disponíveis: "r" (pedra), "t" (tesoura), "p" (papel)

while True:  # Loop principal do jogo
    user_choice = input(
        "Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair: "
    ).lower()  # Solicita a escolha do jogador e converte para minúsculas

    if user_choice == "q":  # Se o jogador escolher "q", sai do jogo
        break

    if (
        user_choice not in options
    ):  # Se a escolha do jogador não estiver nas opções válidas, volta para o início do loop
        continue

    computer_choice = random.randint(
        0, 2
    )  # Gera uma escolha aleatória para o computador (0: "r", 1: "t", 2: "p")
    computer_option = options[
        computer_choice
    ]  # Obtém a opção escolhida pelo computador

    print(
        "O computador escolheu " + computer_option
    )  # Exibe a opção escolhida pelo computador

    if (
        user_choice == computer_option
    ):  # Se a escolha do jogador for igual à escolha do computador, é um empate
        print("Empate!")

    elif (
        (
            user_choice == "r" and computer_option == "t"
        )  # Se a escolha do jogador for "r" e a escolha do computador for "t"
        or (
            user_choice == "t" and computer_option == "p"
        )  # ou a escolha do jogador for "t" e a escolha do computador for "p"
        or (
            user_choice == "p" and computer_option == "r"
        )  # ou a escolha do jogador for "p" e a escolha do computador for "r"
    ):
        print("Você ganhou!")  # O jogador ganha
        user_points += 1  # Incrementa a pontuação do jogador em 1

    else:
        print("Você perdeu!")  # O jogador perde
        computer_points += 1  # Incrementa a pontuação do computador em 1

print("Sua pontuação: " + str(user_points))  # Exibe a pontuação final do jogador
print(
    "Pontuação do Computador: " + str(computer_points)
)  # Exibe a pontuação final do computador

if (
    computer_points > user_points
):  # Se a pontuação do computador for maior que a pontuação do jogador, é uma derrota
    print("Derrota!!!!")
elif (
    computer_points == user_points
):  # Se a pontuação do computador for igual à pontuação do jogador, é um empate
    print("Empate")
else:  # Caso contrário, a pontuação do jogador é maior e é uma vitória
    print("Vitória!!")
