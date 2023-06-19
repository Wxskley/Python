import csv

# Abrir o arquivo CSV no modo de leitura
with open(
    "ChatGPT\Dia 6\Manipulação de arquivos CSV e JSON\CSV\dados.csv", "r"
) as arquivo:
    # Criar um leitor de CSV
    leitor = csv.reader(arquivo)

    # Iterar pelas linhas do arquivo
    for linha in leitor:
        # Imprimir cada linha
        print(linha)
