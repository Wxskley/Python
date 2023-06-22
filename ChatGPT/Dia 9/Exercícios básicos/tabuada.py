# Solicita ao usuário que insira um número
num = int(input("Digite um número: "))

# Exibe a tabuada do número
for i in range(1, 11):
    resultado = num * i
    print(num, "x", i, "=", resultado)
