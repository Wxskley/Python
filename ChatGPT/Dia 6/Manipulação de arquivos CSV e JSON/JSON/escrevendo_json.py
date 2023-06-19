import json

# Dados a serem gravados no arquivo JSON
dados = {"nome": "João", "idade": "30", "profissao": "Engenheiro"}

# Abre o arquivo "dados.json" para escrita
with open(
    "ChatGPT\Dia 6\Manipulação de arquivos CSV e JSON\JSON\dados.json", "w"
) as arquivo:
    # Usa a função json.dump() para escrever os dados no arquivo
    json.dump(dados, arquivo)

# Exibe uma mensagem informando que o arquivo foi criado com sucesso
print("Arquivo JSON criado com sucesso!")
