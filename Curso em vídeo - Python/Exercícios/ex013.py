salario = float(
    input("Digite o seu salário: ")
)  # Solicita ao usuário para digitar o seu salário e converte a entrada em um número de ponto flutuante (float)

aumento = 1.15  # Define o fator de aumento como 1.15, que representa um aumento de 15%

novoSalario = (
    salario * aumento
)  # Calcula o novo salário multiplicando o salário atual pelo fator de aumento

print(
    "Seu salário com aumento de 15% fica {:.2f}".format(novoSalario)
)  # Exibe a mensagem informando o novo salário com duas casas decimais, substituindo o espaço reservado pelo valor de 'novoSalario'
