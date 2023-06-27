primeiro_termo = int(
    input("Digite o primeiro termo da PA: ")
)  # Solicita ao usuário o primeiro termo da PA
razao = int(input("Digite a razão da PA: "))  # Solicita ao usuário a razão da PA

print("Os termos da PA são:")

i = 0  # Variável de controle para o número de termos exibidos
opcao = "s"  # Inicializa a opção com "s" para entrar no loop

while opcao != "n":
    termo = primeiro_termo + (i * razao)  # Calcula o termo da PA
    print(termo)  # Exibe o termo

    i += 1  # Incrementa o contador de termos

    opcao = input(
        "Deseja mostrar mais um termo? (s/n): "
    )  # Pergunta ao usuário se deseja mostrar mais um termo

    if opcao == "n":
        break  # Sai do loop caso a opção seja "n"
