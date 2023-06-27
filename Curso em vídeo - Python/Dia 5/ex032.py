ano = int(
    input("Digite um ano: ")
)  # Solicita ao usuário que digite um ano e converte o valor para inteiro

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    # Verifica se o ano é divisível por 4 e se não é divisível por 100, ou se é divisível por 400
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
