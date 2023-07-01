def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")

    if passo > 0:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ")
    else:
        for i in range(inicio, fim - 1, passo):
            print(i, end=" ")

    print("\n")


# Contagem de 1 até 10, de 1 em 1
contador(1, 10, 1)

# Contagem de 10 até 0, de 2 em 2
contador(10, 0, -2)

# Contagem personalizada
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor do passo: "))

contador(inicio, fim, passo)
