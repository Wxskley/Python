import sqlite3

# Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("ChatGPT\Dia 7\Banco de dados\exemplo.db")
cursor = conexao.cursor()

# Excluir um registro da tabela
cursor.execute("DELETE FROM alunos WHERE nome = 'João'")

# Confirmar as alterações e fechar a conexão
conexao.commit()
conexao.close()
