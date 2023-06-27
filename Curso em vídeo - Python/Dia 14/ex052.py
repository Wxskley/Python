numero = int(
    input("Digite um número inteiro: ")
)  # Solicita ao usuário para digitar um número inteiro

# Verifica se o número é maior que 1
if numero > 1:
    # Loop para verificar se o número é divisível por algum número além de 1 e ele mesmo
    for i in range(2, numero):
        if numero % i == 0:
            print("O número não é primo.")
            break
    else:
        print("O número é primo.")
else:
    print("O número não é primo.")
