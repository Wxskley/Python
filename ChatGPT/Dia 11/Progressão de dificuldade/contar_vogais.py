# Nível de dificuldade: 65%
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
num_vogais = 0

for letra in palavra:
    if letra in vogais:
        num_vogais += 1

print("O número de vogais na palavra é:", num_vogais)
