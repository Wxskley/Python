# Inicializar a variável de soma
soma = 0

# Loop for para percorrer os números de 1 a 500
for numero in range(1, 501):
    # Verificar se o número é ímpar e múltiplo de três
    if numero % 2 != 0 and numero % 3 == 0:
        # Adicionar o número à soma
        soma += numero

# Imprimir o resultado da soma
print("A soma dos números ímpares múltiplos de três no intervalo de 1 a 500 é:", soma)
