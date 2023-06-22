# Solicita ao usuário que insira um número
num = int(input("Digite um número: "))

# Calcula o fatorial do número
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

# Exibe o fatorial do número
print("O fatorial de", num, "é:", fatorial)
