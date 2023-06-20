import sqlite3

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("ChatGPT\Dia 7\Banco de dados\exemplo.db")
cursor = conexao.cursor()

# Criar a tabela "alunos" se ela não existir
cursor.execute(
    "CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER)"
)

# Fechar a conexão
conexao.close()
