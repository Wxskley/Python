# Algoritmo 5: Verificar se um número é primo
# Nível de dificuldade: 30%
num = int(input("Digite um número: "))
primo = True
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
if primo:
    print("O número é primo.")
else:
    print("O número não é primo.")
