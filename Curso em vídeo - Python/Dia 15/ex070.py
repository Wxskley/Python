# Inicialização das variáveis
total_gasto = 0
produtos_mais_1000 = 0
nome_mais_barato = ""
preco_mais_barato = float("inf")

while True:
    # Solicita o nome e o preço do produto
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))

    # Atualiza o total gasto na compra
    total_gasto += preco_produto

    # Verifica se o produto custa mais de R$1000
    if preco_produto > 1000:
        produtos_mais_1000 += 1

    # Verifica se o produto é o mais barato até o momento
    if preco_produto < preco_mais_barato:
        nome_mais_barato = nome_produto
        preco_mais_barato = preco_produto

    # Pergunta ao usuário se deseja continuar cadastrando produtos
    opcao = input("Deseja continuar? [S/N]: ").upper()
    if opcao == "N":
        break

# Exibe os resultados finais
print(f"Total gasto na compra: R${total_gasto:.2f}")
print(f"Quantidade de produtos que custam mais de R$1000: {produtos_mais_1000}")
print(f"Nome do produto mais barato: {nome_mais_barato}")
