import sqlite3

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("ChatGPT\Dia 7\Banco de dados\exemplo.db")
cursor = conexao.cursor()

# Consultar todos os registros da tabela
cursor.execute("SELECT * FROM alunos")
registros = cursor.fetchall()

# Exibir os registros encontrados
for registro in registros:
    print(registro)

# Fechar a conexão
conexao.close()
