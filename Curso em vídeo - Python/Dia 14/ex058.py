import random

numero_pensado = random.randint(
    0, 10
)  # O computador "pensa" em um número aleatório entre 0 e 10
tentativas = 0  # Variável para contar o número de tentativas

while True:
    numero_usuario = int(
        input("Tente adivinhar o número que estou pensando (entre 0 e 10): ")
    )
    tentativas += 1  # Incrementa o número de tentativas

    if numero_usuario == numero_pensado:
        print("Parabéns! Você acertou o número em", tentativas, "tentativas.")
        break  # Sai do loop quando o jogador acerta o número
    else:
        print("Você errou. Tente novamente.")
