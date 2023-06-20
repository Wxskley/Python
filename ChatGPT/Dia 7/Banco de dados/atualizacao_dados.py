import sqlite3

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("ChatGPT\Dia 7\Banco de dados\exemplo.db")
cursor = conexao.cursor()

# Atualizar um registro na tabela
cursor.execute("UPDATE alunos SET idade = 21 WHERE nome = 'João'")

# Confirmar as alterações e fechar a conexão
conexao.commit()
conexao.close()
