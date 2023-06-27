# Função para calcular o fatorial
def calcular_fatorial(numero):
    fatorial = 1

    # Caso especial para o fatorial de 0 e 1
    if numero == 0 or numero == 1:
        return fatorial

    # Calcula o fatorial para números maiores que 1
    i = 2
    while i <= numero:
        fatorial *= i
        i += 1

    return fatorial


# Programa principal
numero = int(input("Digite um número: "))

# Chama a função para calcular o fatorial do número digitado
resultado = calcular_fatorial(numero)

print("O fatorial de", numero, "é:", resultado)
