soma = 0  # Variável para armazenar a soma dos números
contador = 0  # Variável para contar a quantidade de números digitados

while True:
    numero = int(input("Digite um número inteiro (ou 999 para parar): "))

    if numero == 999:
        break  # Sai do loop caso seja digitado 999

    soma += numero  # Adiciona o número à soma
    contador += 1  # Incrementa o contador

print("Foram digitados", contador, "números.")
print("A soma dos números é:", soma)
