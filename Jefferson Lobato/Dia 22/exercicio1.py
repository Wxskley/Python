cont = 1
convidados = []
while cont <= 10:
    nome = input(f"Digite o nome do {cont} convidado: ")
    convidados.append(nome)
    cont += 1
print("Os convidados em ordem alfabética:")
convidados.sort()
print(convidados)
