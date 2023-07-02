def leiaDinheiro(mensagem):
    while True:
        valor = input(mensagem).replace(",", ".").strip()
        if valor.isnumeric():
            return float(valor)
        else:
            print("Valor inválido. Digite um valor monetário válido.")
