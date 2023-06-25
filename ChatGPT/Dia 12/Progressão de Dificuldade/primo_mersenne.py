# Função para verificar se um número é um número primo de Mersenne
# Dificuldade: 60%
from numero_primo import verificar_primo


def verificar_primo_mersenne(expoente):
    # Calcula o número de Mersenne usando a fórmula 2^expoente - 1
    numero_mersenne = 2**expoente - 1
    # Verifica se o expoente é um número primo
    if verificar_primo(expoente):
        # Verifica se o número de Mersenne é primo
        if verificar_primo(numero_mersenne):
            return True
    return False


# Expoente de exemplo
expoente = 5
# Chama a função para verificar se o número é um número primo de Mersenne e imprime o resultado
print(verificar_primo_mersenne(expoente))
