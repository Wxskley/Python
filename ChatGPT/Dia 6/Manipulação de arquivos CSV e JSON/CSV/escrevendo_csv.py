import csv

dados = [
    [
        "Nome",
        "Idade",
        "Profissão",
    ],  # Lista com os cabeçalhos e dados a serem escritos no arquivo CSV
    ["João", "30", "Engenheiro"],
    ["Maria", "25", "Designer"],
]

# Abre o arquivo "dados.csv" no modo de escrita
with open(
    "ChatGPT\Dia 6\Manipulação de arquivos CSV e JSON\CSV\dados.csv", "w", newline=""
) as arquivo:
    escritor = csv.writer(
        arquivo
    )  # Cria um objeto escritor para escrever no arquivo CSV
    escritor.writerows(dados)  # Escreve os dados no arquivo CSV

print(
    "Arquivo CSV criado com sucesso!"
)  # Exibe uma mensagem indicando que o arquivo foi criado
