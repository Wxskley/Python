import json

with open(
    "ChatGPT\Dia 6\Manipulação de arquivos CSV e JSON\JSON\dados.json", "r"
) as arquivo:
    # Abrindo o arquivo "dados.json" para leitura usando o modo "r"
    # Certifique-se de fornecer o caminho correto para o arquivo no seu sistema
    # Isso inclui a estrutura de diretórios e o nome do arquivo

    conteudo = json.load(arquivo)
    # Carregando o conteúdo do arquivo JSON usando a função json.load()
    # O conteúdo é armazenado em uma variável chamada "conteudo"

    print(conteudo)
    # Imprimindo o conteúdo do arquivo JSON

# O bloco "with" garante que o arquivo seja fechado automaticamente após o uso
# Isso é importante para garantir que recursos do sistema sejam liberados adequadamente
# O modo "r" indica que o arquivo será aberto para leitura
