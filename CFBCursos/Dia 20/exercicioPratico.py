import os

carros = []  # Lista vazia para armazenar os carros

class Carro:
    nome = ""  # Nome do carro
    pot = 0  # Potência do carro
    velMax = 0  # Velocidade máxima do carro (calculada como o dobro da potência)
    ligado = False  # Indica se o carro está ligado

    def __init__(self, nome, pot):
        # Inicializa as características do carro
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        # Exibe as informações do carro
        print("Nome..............:", self.nome)
        print("Potência..........:", self.pot)
        print("Velocidade Máxima.:", self.velMax)
        print("Ligado............:", ("Sim" if self.ligado == True else "Não"))

def Menu():
    # Exibe o menu e retorna a opção escolhida
    os.system("cls") or None
    print("1 - Novo carro")
    print("2 - Informações do carro")
    print("3 - Excluir carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair")
    print("Quantidade de carros:", len(carros))
    opc = input("Digite uma opção: ")
    return opc

def NovoCarro():
    # Cria um novo carro e o adiciona à lista
    os.system("cls") or None
    n = input("Nome do Carro.....: ")
    p = input("Potência do Carro.: ")
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro criado")
    os.system("pause")

def informacoes():
    # Exibe informações de um carro específico
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja ver as informações: "))
    try:
        carros[n].info()
    except:
        print("Carro não existe na lista")
    os.system("pause")

def excluirCarro():
    # Exclui um carro da lista
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja excluir: "))
    try:
        del carros[n]
        print("Carro excluído")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def ligarCarro():
    # Liga um carro específico
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja ligar: "))
    try:
        carros[n].ligar()
        print("Carro ligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def desligarCarro():
    # Desliga um carro específico
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja desligar: "))
    try:
        carros[n].desligar()
        print("Carro desligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def listarCarros():
    # Lista todos os carros presentes na lista
    os.system("cls") or None
    p = 0
    for c in carros:
        print(p, " - ", c.nome)
        p += 1
    os.system("pause")

ret = Menu()  # Exibe o menu pela primeira vez e recebe a opção escolhida

while ret < "7":
    if ret == "1":
        NovoCarro()
    elif ret == "2":
        informacoes()
    elif ret == "3":
        excluirCarro()
    elif ret == "4":
        ligarCarro()
    elif ret == "5":
        desligarCarro()
    elif ret == "6":
        listarCarros()
    ret = Menu()  # Exibe o menu novamente e recebe a nova opção escolhida

os.system("cls") or None
print("Programa finalizado")
