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


def menuPrincipal():
    os.system("cls")
    print("1 - Inserior Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por ID")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")


def menuInserir():
    print()


def menuDeletar():
    print()


def menuAtualizar():
    print()


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
os.system("pause")
