import random

print(
    "Seja muito bem vindo ao Guess Number do Weskley!"
)  # Exibe uma mensagem de boas-vindas ao jogo
choice_number = input(
    "Digite o número teto do desafio: "
)  # Solicita ao usuário o número máximo para o desafio e armazena na variável choice_number

if choice_number.isdigit():  # Verifica se o valor digitado é numérico
    choice_number = int(choice_number)  # Converte o valor para inteiro
else:
    print(
        "Erro: valor informado não é numérico. Favor execute novamente e informe um número!"
    )  # Exibe uma mensagem de erro se o valor não for numérico
    quit()  # Encerra o programa

random_number = random.randint(
    0, choice_number
)  # Gera um número aleatório entre 0 e o número máximo informado
n_choices = 0  # Inicializa o contador de tentativas como 0

while True:  # Loop infinito para permitir múltiplas tentativas
    answer_user = input(
        "Adivinhe o número: "
    )  # Solicita ao usuário que adivinhe o número
    if answer_user.isdigit():  # Verifica se o valor digitado é numérico
        answer_user = int(answer_user)  # Converte o valor para inteiro
    else:
        print(
            "Erro: valor informado não é numérico. Favor informe um número!"
        )  # Exibe uma mensagem de erro se o valor não for numérico
        continue  # Volta para o início do loop

    n_choices = n_choices + 1  # Incrementa o contador de tentativas

    if answer_user == random_number:  # Verifica se a resposta do usuário está correta
        print("Acertou!")  # Exibe uma mensagem informando que o usuário acertou
        break  # Encerra o loop

    elif (
        answer_user > random_number
    ):  # Verifica se o número fornecido é maior que o número aleatório
        print(
            "Chutou alto, o número aleatório é menor que isso..."
        )  # Exibe uma mensagem informando que o número é alto

    else:  # Caso contrário, o número fornecido é menor que o número aleatório
        print(
            "Chutou baixo, o número aleatório é maior que isso..."
        )  # Exibe uma mensagem informando que o número é baixo

print(
    "Número de tentativas: " + str(n_choices)
)  # Exibe o número de tentativas realizadas pelo usuário
