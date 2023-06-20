import sqlite3

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("ChatGPT\Dia 7\Banco de dados\exemplo.db")
cursor = conexao.cursor()

# Inserir um novo registro na tabela
cursor.execute("INSERT INTO alunos (nome, idade) VALUES ('João', 20)")

# Confirmar as alterações e fechar a conexão
conexao.commit()
conexao.close()
