# Função para verificar se um número é perfeito
# Dificuldade: 35%
def verificar_numero_perfeito(numero):
    # Inicializa a soma dos divisores como zero
    soma = 0
    # Percorre os possíveis divisores do número (exceto o próprio número)
    for divisor in range(1, numero):
        # Se o número é divisível pelo divisor, adiciona o divisor à soma
        if numero % divisor == 0:
            soma += divisor
    # Verifica se a soma dos divisores é igual ao número
    if soma == numero:
        return True
    else:
        return False


# Número de exemplo
numero = 28
# Chama a função para verificar se o número é perfeito e imprime o resultado
print(verificar_numero_perfeito(numero))
