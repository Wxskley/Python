import random
import string


def password_generator(len_pass=8):
    # Define as opções de caracteres para a geração da senha
    ascii_options = string.ascii_letters  # Letras maiúsculas e minúsculas
    number_options = string.digits  # Números de 0 a 9
    punt_options = string.punctuation  # Caracteres especiais
    options = ascii_options + number_options + punt_options

    password_user = ""  # Variável para armazenar a senha gerada

    for i in range(0, len_pass):  # Loop para gerar cada dígito da senha
        digit = random.choice(
            options
        )  # Escolhe um caractere aleatório das opções disponíveis
        password_user = password_user + digit  # Adiciona o caractere à senha

    return password_user  # Retorna a senha gerada


choice_user = input(
    "Quantos dígitos na senha?"
)  # Solicita ao usuário o comprimento desejado da senha
if choice_user.isdigit():  # Verifica se a entrada é um número inteiro
    choice_user = int(choice_user)  # Converte a entrada para um número inteiro
else:
    print(
        "Entrada inválida!"
    )  # Exibe uma mensagem de erro se a entrada não for um número
    quit()  # Encerra o programa

response = password_generator(
    len_pass=choice_user
)  # Chama a função password_generator() passando o comprimento escolhido
print(f"Senha gerada:\n{response}")  # Exibe a senha gerada na tela
