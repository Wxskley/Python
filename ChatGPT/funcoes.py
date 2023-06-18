# Exemplo de código para criar e utilizar funções em Python
def calcular_soma(a, b):
    resultado = a + b
    return resultado


def calcular_subtracao(a, b):
    resultado = a - b
    return resultado


def calcular_multiplicacao(a, b):
    resultado = a * b
    return resultado


def calcular_divisao(a, b):
    resultado = a / b
    return resultado


# Utilizando as funções definidas
soma = calcular_soma(10, 5)
subtracao = calcular_subtracao(10, 5)
multiplicacao = calcular_multiplicacao(10, 5)
divisao = calcular_divisao(10, 5)

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
