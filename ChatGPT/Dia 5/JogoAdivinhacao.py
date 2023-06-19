import random

numero_aleatorio = random.randint(1, 100)
tentativas = 0
acertou = False

while not acertou:
    tentativa = int(input("Digite um número: "))
    tentativas += 1

    if tentativa == numero_aleatorio:
        print("Parabéns! Você acertou o número em", tentativas, "tentativas.")
        acertou = True
    elif tentativa < numero_aleatorio:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
