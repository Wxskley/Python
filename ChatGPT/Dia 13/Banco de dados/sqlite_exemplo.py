import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("ChatGPT\Dia 13\Banco de dados\dados.db")

# Criação da tabela
conn.execute(
    """CREATE TABLE IF NOT EXISTS usuarios
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL);"""
)

# Inserção de dados
conn.execute(
    "INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("João", "joao@example.com")
)
conn.execute(
    "INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("Maria", "maria@example.com")
)
conn.commit()

# Consulta de dados
cursor = conn.execute("SELECT * FROM usuarios")
for row in cursor:
    print(f"ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}")

# Atualização de dados
conn.execute(
    "UPDATE usuarios SET email = ? WHERE nome = ?", ("joao_novo@example.com", "João")
)
conn.commit()

# Exclusão de dados
conn.execute("DELETE FROM usuarios WHERE nome = ?", ("Maria",))
conn.commit()

# Consulta de dados atualizados
cursor = conn.execute("SELECT * FROM usuarios")
for row in cursor:
    print(f"ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}")

# Fechamento da conexão
conn.close()
