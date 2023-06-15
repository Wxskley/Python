produto = float(
    input("Qual o preço do produto? ")
)  # Solicita ao usuário para digitar o preço do produto e converte a entrada em um número de ponto flutuante (float)

novoPreco = (
    produto * 0.95
)  # Calcula o novo preço do produto aplicando um desconto de 5%, multiplicando o preço do produto por 0.95

print(
    "O seu produto agora está custando {}".format(novoPreco)
)  # Exibe a mensagem informando o novo preço do produto, substituindo o espaço reservado pelo valor de 'novoPreco'
