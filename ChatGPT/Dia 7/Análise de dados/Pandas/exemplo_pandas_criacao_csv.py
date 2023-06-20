import pandas as pd

# Dados a serem gravados no arquivo CSV
dados = {
    "Nome": ["João", "Maria", "Pedro"],
    "Idade": [25, 30, 28],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
}

# Criação de um DataFrame com os dados
df = pd.DataFrame(dados)

# Salvando o DataFrame em um arquivo CSV
nome_arquivo = "ChatGPT\Dia 7\Análise de dados\Pandas\dados.csv"
df.to_csv(nome_arquivo, index=False)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
