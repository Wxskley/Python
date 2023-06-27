soma = 0  # Variável para armazenar a soma dos valores
contador = 0  # Variável para contar a quantidade de valores digitados
maior = float(
    "-inf"
)  # Variável para armazenar o maior valor digitado (inicializada com o menor valor possível)
menor = float(
    "inf"
)  # Variável para armazenar o menor valor digitado (inicializada com o maior valor possível)

while True:
    numero = int(input("Digite um número inteiro: "))

    soma += numero  # Adiciona o número à soma
    contador += 1  # Incrementa o contador

    if numero > maior:  # Verifica se o número é maior que o maior valor atual
        maior = numero  # Atualiza o maior valor

    if numero < menor:  # Verifica se o número é menor que o menor valor atual
        menor = numero  # Atualiza o menor valor

    opcao = input("Deseja continuar? (S/N): ")
    if opcao.upper() == "N":  # Verifica se a opção é "N" (não)
        break  # Sai do loop caso a opção seja "N"

media = soma / contador  # Calcula a média

# Exibe os resultados
print("A média dos valores é:", media)
print("O maior valor digitado foi:", maior)
print("O menor valor digitado foi:", menor)
