import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect("ChatGPT\Dia 7\Banco de dados\meu_banco_de_dados.db")

# Criação de um cursor
cursor = conexao.cursor()

# Execução de uma consulta SQL
cursor.execute("SELECT * FROM usuarios")

# Recuperação dos resultados
resultados = cursor.fetchall()

# Impressão dos resultados
for resultado in resultados:
    print(resultado)

# Fechamento da conexão
conexao.close()
