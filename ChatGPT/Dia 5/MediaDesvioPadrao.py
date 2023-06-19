numeros = input("Digite os números separados por espaço: ").split()
# Solicita ao usuário que digite uma sequência de números separados por espaço e armazena como uma lista de strings.

numeros = [float(numero) for numero in numeros]
# Converte cada elemento da lista de strings em números float.

media = sum(numeros) / len(numeros)
# Calcula a média dos números dividindo a soma deles pelo total de números.

diferenca_quadrado = [(numero - media) ** 2 for numero in numeros]
# Calcula a diferença ao quadrado entre cada número e a média.

desvio_padrao = (sum(diferenca_quadrado) / len(numeros)) ** 0.5
# Calcula o desvio padrão dividindo a soma das diferenças ao quadrado pelo total de números e tirando a raiz quadrada.

print("A média dos números é:", media)
# Exibe a média dos números.

print("O desvio padrão dos números é:", desvio_padrao)
# Exibe o desvio padrão dos números.
