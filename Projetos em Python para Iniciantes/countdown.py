import time

t = input(
    "Digite o tempo (em segundos): "
)  # Solicita ao usuário que digite o tempo desejado em segundos e armazena na variável 't'

if t.isdigit():  # Verifica se o valor digitado é um número inteiro
    t = int(t)  # Converte o valor para um número inteiro
else:
    print(
        "Entrada inválida!"
    )  # Exibe uma mensagem de erro se a entrada não for um número
    quit()  # Encerra o programa

while t:  # Loop enquanto o valor de 't' for verdadeiro (diferente de zero)
    minutes, seconds = divmod(t, 60)  # Divide o tempo em minutos e segundos
    timer = "{:02d}:{:02d}".format(
        minutes, seconds
    )  # Formata a string do timer com dois dígitos para minutos e segundos
    print(
        timer, end="\r"
    )  # Exibe o timer na tela, utilizando o caractere especial '\r' para substituir a linha anterior
    time.sleep(1)  # Aguarda 1 segundo
    t = t - 1  # Reduz o valor de 't' em 1 segundo

print("Tempo acabou!")  # Exibe uma mensagem informando que o tempo acabou
