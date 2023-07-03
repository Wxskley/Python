import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = r"C:\Users\Weskley\Documents\Programação\Python\CFBCursos\Dia 20\banco de dados\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()
createTable = """
    CREATE TABLE tb_contatos(
    N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOMECONTATO VARCHAR(30),
    T_TELEFONECONTATO VARCHAR(14),
    T_EMAILCONTATO VARCHAR(30)
    )
"""


def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)


criarTabela(vcon, createTable)
# nome = input("Digite o nome: ")
# telefone = input("Digite o telefone: ")
# email = input("Digite o email: ")
# insertTable = f"""INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
#           VALUES('{nome}','{telefone}','{email}')
#        """


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registo inserido")
    except Error as ex:
        print(ex)


# inserir(vcon, insertTable)


def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registo removido")


deleteInTable = "DELETE FROM tb_contatos WHERE N_IDCONTATO=2"


# deletar(vcon, deleteInTable)
def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registo atualizado")


atualizarInTable = "UPDATE tb_contatos SET T_NOMECONTATO = 'Bruno', T_TELEFONECONTATO = '(88)98888-8888',T_EMAILCONTATO = 'bruno@email.com.br' WHERE N_IDCONTATO=1"


# atualizar(vcon, atualizarInTable)
def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado


consultar = "SELECT * FROM tb_contatos"
res = consulta(vcon, consultar)
for r in res:
    print(r)
vcon.close()
