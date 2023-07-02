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


def resumo(valor, taxa_aumento, taxa_desconto):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"Aumento de {taxa_aumento}%: \t{aumentar(valor, taxa_aumento, True)}")
    print(f"Desconto de {taxa_desconto}%: \t{diminuir(valor, taxa_desconto, True)}")
    print("-" * 30)
