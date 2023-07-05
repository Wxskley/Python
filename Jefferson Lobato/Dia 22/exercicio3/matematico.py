def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if a != 0 or b != 0:
        return a / b
    else:
        print("Impossível dividir por zero.")


def par_impar(a, b):
    soma = a + b
    sobra = soma % 2
    if sobra == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"
    return par_impar
