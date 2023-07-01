def leiaInt(msg):
    """
    Função para ler um valor inteiro digitado pelo usuário.
    :param msg: Mensagem para solicitar a entrada do valor.
    :return: Valor inteiro digitado pelo usuário.
    """
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")


# Exemplo de uso da função
n = leiaInt("Digite um número inteiro: ")
print(f"O número digitado foi: {n}")
