def aumentar(valor, taxa):
    aumento = valor * (taxa / 100)
    return valor + aumento


def diminuir(valor, taxa):
    desconto = valor * (taxa / 100)
    return valor - desconto


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def moeda(valor):
    return f"R${valor:.2f}".replace(".", ",")
