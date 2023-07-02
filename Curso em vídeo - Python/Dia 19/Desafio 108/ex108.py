from moeda import aumentar, diminuir, dobro, metade, moeda

valor = float(input("Digite um valor: "))

print(f"Aumento de 10%: {moeda(aumentar(valor, 10))}")
print(f"Desconto de 5%: {moeda(diminuir(valor, 5))}")
print(f"Dobro: {moeda(dobro(valor))}")
print(f"Metade: {moeda(metade(valor))}")
