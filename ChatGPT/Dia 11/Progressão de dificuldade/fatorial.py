# Algoritmo 4: Cálculo do fatorial
# Nível de dificuldade: 25%
num = int(input("Digite um número: "))
resultado = 1
for i in range(1, num + 1):
    resultado *= i
print("O fatorial de", num, "é", resultado)
