# Função para verificar se um número é primo
# Dificuldade: 25%
def verificar_primo(numero):
    # Verifica se o número é menor que 2 (números menores que 2 não são primos)
    if numero < 2:
        return False
    # Percorre os possíveis divisores do número
    for divisor in range(2, int(numero**0.5) + 1):
        # Se o número é divisível por algum divisor, não é primo
        if numero % divisor == 0:
            return False
    # Se não foi encontrado nenhum divisor, o número é primo
    return True


# Número de exemplo
numero = 17
# Chama a função para verificar se o número é primo e imprime o resultado
print(verificar_primo(numero))
