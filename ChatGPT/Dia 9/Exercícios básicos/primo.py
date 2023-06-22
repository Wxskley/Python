# Solicita ao usuário que insira um número
num = int(input("Digite um número: "))

# Verifica se o número é primo
primo = True
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
else:
    primo = False

# Exibe o resultado da verificação
if primo:
    print("O número é primo")
else:
    print("O número não é primo")
