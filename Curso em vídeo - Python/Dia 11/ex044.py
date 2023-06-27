preco_produto = float(input("Digite o preço do produto: R$ "))
condicao_pagamento = input(
    "Digite a condição de pagamento (à vista dinheiro/cheque, à vista no cartão, em até 2x no cartão, 3x ou mais no cartão): "
)

if condicao_pagamento == "à vista dinheiro/cheque":
    valor_pago = preco_produto - (preco_produto * 0.1)
elif condicao_pagamento == "à vista no cartão":
    valor_pago = preco_produto - (preco_produto * 0.05)
elif condicao_pagamento == "em até 2x no cartão":
    valor_pago = preco_produto
else:
    valor_pago = preco_produto + (preco_produto * 0.2)

print(f"O valor a ser pago é R$ {valor_pago:.2f}")
