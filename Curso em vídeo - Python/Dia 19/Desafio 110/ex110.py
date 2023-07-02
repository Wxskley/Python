from moeda import resumo

valor = float(input("Digite o valor: "))
taxa_aumento = float(input("Digite a taxa de aumento (%): "))
taxa_desconto = float(input("Digite a taxa de desconto (%): "))

resumo(valor, taxa_aumento, taxa_desconto)
