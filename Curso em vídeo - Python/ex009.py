numero = int(
    input("Digite um número para obter sua tabuada: ")
)  # Solicita ao usuário para digitar um número inteiro e o converte para inteiro

print(
    "Tabuada de {}".format(numero)
)  # Exibe a mensagem informando a tabuada do número digitado

for i in range(1, 11):  # Loop de 1 a 10
    resultado = numero * i  # Calcula a multiplicação do número pelo valor atual do loop
    print(
        numero, "x", i, "=", resultado
    )  # Exibe a multiplicação na forma "numero x i = resultado"
