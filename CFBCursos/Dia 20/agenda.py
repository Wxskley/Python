import os
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


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com sucesso")
        # conexao.close()


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res


def menuPrincipal():
    os.system("cls")
    print("1 - Inserior Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por ID")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")


def menuInserir():
    os.system("cls")
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    vsql = f"INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('{vnome}','{vtelefone}','{vemail}')"
    query(vcon, vsql)


def menuDeletar():
    os.system("cls")
    vid = input("Digite o ID do registro a ser deletado: ")
    vsql = f"DELETE FROM tb_contatos WHERE N_IDCONTATO = {vid}"
    query(vcon, vsql)


def menuAtualizar():
    os.system("cls")
    vid = input("Digite o ID do registro a ser alterado: ")
    r = consultar(vcon, f"SELECT * FROM tb_contatos WHERE N_IDCONTATO = {vid}")
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    if len(vnome) == 0:
        vnome = rnome
    if len(vtelefone) == 0:
        vtelefone = rtelefone
    if len(vemail) == 0:
        vemail = remail
    vsql = f"UPDATE tb_contatos SET T_NOMECONTATO = '{vnome}', T_TELEFONECONTATO = '{vtelefone}', T_EMAILCONTATO = '{vemail}' WHERE N_IDCONTATO = {vid}"
    query(vcon, vsql)


def menuConsultarId():
    print()


def menuConsultarNomes():
    print()


opc = 0
while opc != 6:
    menuPrincipal()
    opc = int(input("Digite uma opção: "))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultarId()
    elif opc == 5:
        menuConsultarNomes()
    elif opc == 6:
        os.system("cls")
        print("Programa finalizado")
    else:
        os.system("cls")
        print("Opção inválida")
        os.system("pause")
vcon.close()
os.system("pause")
