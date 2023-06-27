valor_casa = float(
    input("Qual o valor da casa desejada: R$")
)  # Solicita o valor da casa
valor_salario = float(input("Qual é o seu salário: R$"))  # Solicita o valor do salário
tempo_casa = int(
    input("Em quantos anos deseja pagar a casa: ")
)  # Solicita o prazo de pagamento em anos

calculo_valor_prestacao = valor_casa / (
    tempo_casa * 12
)  # Calcula o valor da prestação mensal

if (
    calculo_valor_prestacao <= valor_salario * 0.30
):  # Verifica se a prestação é menor ou igual a 30% do salário
    print("Empréstimo aprovado!")  # Exibe mensagem de aprovação do empréstimo
else:
    print("Empréstimo negado!")  # Exibe mensagem de negação do empréstimo
    print(
        "O valor da parcela ultrapassa 30% do valor do salário!"
    )  # Informa o motivo da negação

print(
    f"O valor da parcela ficou {calculo_valor_prestacao:.2f}"
)  # Exibe o valor da prestação formatado com duas casas decimais
