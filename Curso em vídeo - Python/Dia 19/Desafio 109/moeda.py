def aumentar(valor, taxa, formatar=False):
    aumento = valor * (taxa / 100)
    resultado = valor + aumento
    return moeda(resultado) if formatar else resultado


def diminuir(valor, taxa, formatar=False):
    desconto = valor * (taxa / 100)
    resultado = valor - desconto
    return moeda(resultado) if formatar else resultado


def dobro(valor, formatar=False):
    resultado = valor * 2
    return moeda(resultado) if formatar else resultado


def metade(valor, formatar=False):
    resultado = valor / 2
    return moeda(resultado) if formatar else resultado


def moeda(valor):
    return f"R${valor:.2f}".replace(".", ",")
