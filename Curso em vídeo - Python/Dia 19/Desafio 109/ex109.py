from moeda import aumentar, diminuir, dobro, metade, moeda

valor = float(input("Digite um valor: "))
print(f"Aumento de 10%: {aumentar(valor,10,True)}")
print(f"Desconto de 5%: {diminuir(valor,5,True)}")
print(f"Dobro: {dobro(valor,True)}")
print(f"Metade: {metade(valor,True)}")
