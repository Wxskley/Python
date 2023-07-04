import os
import sqlite3
from sqlite3 import Error


# Função para estabelecer conexão com o banco de dados SQLite
def ConexaoBanco():
    caminho = r"C:\Users\Weskley\Documents\Programação\Python\CFBCursos\Dia 20\banco de dados\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


# Estabelece a conexão com o banco de dados
vcon = ConexaoBanco()


# Função para executar uma consulta SQL sem retorno de dados
def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com sucesso")


# Função para executar uma consulta SQL com retorno de dados
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res


# Função para exibir o menu principal
def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")


# Função para exibir o menu de inserção de registros
def menuInserir():
    os.system("cls")
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    vsql = f"INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('{vnome}','{vtelefone}','{vemail}')"
    query(vcon, vsql)


# Função para exibir o menu de exclusão de registros
def menuDeletar():
    os.system("cls")
    vid = input("Digite o ID do registro a ser deletado: ")
    vsql = f"DELETE FROM tb_contatos WHERE N_IDCONTATO = {vid}"
    query(vcon, vsql)


# Função para exibir o menu de atualização de registros
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


# Função para exibir todos os registros
def menuConsultar():
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(
            "ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} Email:{3:_<30}".format(
                r[0], r[1], r[2], r[3]
            )
        )
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("pause")


# Função para consultar registros por nome
def menuConsultarNomes():
    vnome = input("Digite o nome: ")
    vsql = f"SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%{vnome}%'"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(
            "ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} Email:{3:_<30}".format(
                r[0], r[1], r[2], r[3]
            )
        )
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("pause")


# Variável para armazenar a opção escolhida pelo usuário
opc = 0

# Loop para exibir o menu principal e executar as opções selecionadas
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
        menuConsultar()
    elif opc == 5:
        menuConsultarNomes()
    elif opc == 6:
        os.system("cls")
        print("Programa finalizado")
    else:
        os.system("cls")
        print("Opção inválida")
        os.system("pause")

# Fecha a conexão com o banco de dados ao final do programa
vcon.close()
os.system("pause")
