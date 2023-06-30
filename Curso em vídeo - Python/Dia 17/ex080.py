# Lista para armazenar os valores
valores = []

# Loop para ler os valores
for i in range(5):
    valor = int(input("Digite um valor: "))

    # Encontrar a posição correta de inserção
    posicao = 0
    while posicao < len(valores) and valor > valores[posicao]:
        posicao += 1

    # Inserir o valor na posição correta
    valores.insert(posicao, valor)

# Exibir a lista ordenada
print("Lista ordenada:")
for valor in valores:
    print(valor)
