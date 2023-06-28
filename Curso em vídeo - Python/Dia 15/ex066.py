numero = 0  # Variável para armazenar o número digitado pelo usuário
soma = 0  # Variável para armazenar a soma dos números
contador = 0  # Variável para contar a quantidade de números digitados

while numero != 999:
    numero = int(input("Digite um número (999 para parar): "))

    if numero != 999:
        soma += numero
        contador += 1

print("Quantidade de números digitados:", contador)
print("Soma dos números:", soma)
