# Função para verificar se um número é um número feliz
# Dificuldade: 50%
def verificar_numero_feliz(numero):
    # Inicializa um conjunto vazio para armazenar os números já visitados
    numeros_visitados = set()
    # Repetição até encontrar o número feliz ou um ciclo infinito
    while numero != 1:
        # Verifica se o número já foi visitado (indica um ciclo infinito)
        if numero in numeros_visitados:
            return False
        # Adiciona o número ao conjunto de visitados
        numeros_visitados.add(numero)
        # Calcula o próximo número somando o quadrado de cada dígito
        numero = sum(int(digito) ** 2 for digito in str(numero))
    # Se chegou a 1, o número é feliz
    return True


# Número de exemplo
numero = 19
# Chama a função para verificar se o número é um número feliz e imprime o resultado
print(verificar_numero_feliz(numero))
