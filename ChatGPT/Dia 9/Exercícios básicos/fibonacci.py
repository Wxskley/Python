# Solicita ao usuário que insira um número
num = int(input("Digite um número: "))

# Calcula a sequência de Fibonacci
fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] <= num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Exibe a sequência de Fibonacci
print("Sequência de Fibonacci até", num, ":", fibonacci)
