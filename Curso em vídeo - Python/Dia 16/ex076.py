# Tupla com nomes de produtos e preços
produtos = (
    ("Notebook", 2500.00),
    ("Celular", 1500.00),
    ("Headset", 200.00),
    ("Mouse", 50.00),
    ("Teclado", 100.00),
)

# Exibição da listagem de preços
print("Listagem de Preços")
print("------------------")
print("Produto\t\tPreço")
print("------------------")
for produto, preco in produtos:
    print(f"{produto:10s}\tR$ {preco:.2f}")
print("------------------")
