import random

vitorias_consecutivas = 0

while True:
    jogador = int(input("Digite um número de 0 a 10: "))
    escolha = input("Par ou ímpar? [P/I]: ").upper()

    computador = random.randint(0, 10)
    soma = jogador + computador

    resultado = "par" if soma % 2 == 0 else "ímpar"

    print(f"Você escolheu {jogador} e o computador escolheu {computador}.")
    print(f"A soma é {soma} ({resultado}).")

    if resultado[0].upper() == escolha:
        print("Você venceu!")
        vitorias_consecutivas += 1
    else:
        print("Você perdeu!")
        break

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")
