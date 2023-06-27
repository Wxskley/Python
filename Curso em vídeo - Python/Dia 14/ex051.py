primeiro_termo = int(
    input("Digite o primeiro termo da PA: ")
)  # Solicita ao usuário para digitar o primeiro termo da PA
razao = int(
    input("Digite a razão da PA: ")
)  # Solicita ao usuário para digitar a razão da PA

print("Os 10 primeiros termos da PA são:")

for i in range(10):  # Loop para calcular e exibir os 10 primeiros termos
    termo = primeiro_termo + (i * razao)  # Fórmula para calcular o termo da PA
    print(termo)  # Exibe o termo da PA
