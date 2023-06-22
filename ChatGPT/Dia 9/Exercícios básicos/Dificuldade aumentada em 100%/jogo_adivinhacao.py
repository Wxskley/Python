import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

tentativas = 0
acertou = False

while not acertou:
    tentativa = int(input("Digite sua tentativa: "))
    tentativas += 1

    if tentativa == numero_secreto:
        acertou = True
        print("Parabéns! Você acertou o número em", tentativas, "tentativas.")
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
