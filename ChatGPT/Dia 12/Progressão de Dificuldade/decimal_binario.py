# Função para converter um número decimal em binário
# Dificuldade: 45%
def decimal_para_binario(decimal):
    # Inicializa uma lista vazia para armazenar os dígitos binários
    binario = []
    # Enquanto o decimal for maior que zero, continua a conversão
    while decimal > 0:
        # Calcula o resto da divisão por 2 e adiciona à lista de binários
        binario.append(decimal % 2)
        # Atualiza o valor do decimal dividindo por 2 (descartando a parte decimal)
        decimal //= 2
    # Inverte a lista de binários para obter o número binário final
    binario.reverse()
    # Retorna o número binário como uma string
    return "".join(map(str, binario))


# Número decimal de exemplo
decimal = 10
# Chama a função para converter o número decimal em binário e imprime o resultado
print(decimal_para_binario(decimal))
