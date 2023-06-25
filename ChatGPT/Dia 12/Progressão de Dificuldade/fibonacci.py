# Função para gerar a sequência de Fibonacci
# Dificuldade: 30%
def gerar_fibonacci(n):
    # Inicializa os primeiros dois números da sequência
    fibonacci = [0, 1]
    # Percorre os próximos números da sequência
    for i in range(2, n):
        # Calcula o próximo número somando os dois números anteriores
        proximo = fibonacci[i - 1] + fibonacci[i - 2]
        # Adiciona o próximo número à sequência
        fibonacci.append(proximo)
    # Retorna a sequência de Fibonacci
    return fibonacci


# Número de exemplo
numero = 10
# Chama a função para gerar a sequência de Fibonacci e imprime o resultado
print(gerar_fibonacci(numero))
