def ajuda(comando):
    """
    Função para exibir o manual do comando especificado.
    :param comando: Comando a ser consultado.
    """
    help(comando)


def cor(texto, cor):
    """
    Função para formatar o texto com a cor especificada.
    :param texto: Texto a ser formatado.
    :param cor: Cor a ser aplicada.
    :return: Texto formatado com a cor.
    """
    cores = {
        "limpa": "\033[m",
        "azul": "\033[34m",
        "vermelho": "\033[31m",
        "verde": "\033[32m",
        "amarelo": "\033[33m",
    }

    if cor in cores:
        return f"{cores[cor]}{texto}{cores['limpa']}"
    else:
        return texto


# Programa principal
comando = ""
while comando != "fim":
    comando = input(cor("Digite um comando ou 'fim' para sair: ", "azul"))
    if comando != "fim":
        ajuda(comando)
    print()

print(cor("Programa encerrado.", "vermelho"))
