# Função para calcular o fatorial de um número
# Dificuldade: 30%
def calcular_fatorial(numero):
    # Caso base: fatorial de 0 é 1
    if numero == 0:
        return 1
    # Caso geral: multiplica o número pelo fatorial do número anterior
    else:
        return numero * calcular_fatorial(numero - 1)


# Número de exemplo
numero = 5
# Chama a função para calcular o fatorial e imprime o resultado
print(calcular_fatorial(numero))
