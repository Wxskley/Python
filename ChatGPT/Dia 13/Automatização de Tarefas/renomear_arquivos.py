import os


# Função para renomear arquivos em um diretório
def renomear_arquivos(diretorio, prefixo):
    # Obtém a lista de arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Itera sobre cada arquivo
    for arquivo in arquivos:
        # Verifica se é um arquivo regular
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            # Obtém o novo nome do arquivo com o prefixo adicionado
            novo_nome = prefixo + arquivo

            # Renomeia o arquivo
            os.rename(
                os.path.join(diretorio, arquivo), os.path.join(diretorio, novo_nome)
            )


# Exemplo de uso
diretorio = "ChatGPT\Dia 13\Automatização de Tarefas\Teste Renomeação de arquivos"
prefixo = "novo_"

renomear_arquivos(diretorio, prefixo)
