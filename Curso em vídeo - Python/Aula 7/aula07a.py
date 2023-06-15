# Solicita ao usuário para digitar dois valores
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

# Realiza operações matemáticas com os valores fornecidos
s = n1 + n2  # Calcula a soma de n1 e n2
m = n1 * n2  # Calcula o produto de n1 e n2
d = n1 / n2  # Calcula a divisão de n1 por n2
di = n1 // n2  # Calcula a divisão inteira de n1 por n2
e = n1**n2  # Calcula n1 elevado a n2 (potência)

# Exibe os resultados das operações na tela
print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(s, m, d), end=" ")
# O {:.3f} formata o valor de d como um número de ponto flutuante com três casas decimais
print("Divisão inteira é {} e potência é {}".format(di, e))
