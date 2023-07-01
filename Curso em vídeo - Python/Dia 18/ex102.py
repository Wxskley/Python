def fatorial(num, show=False):
    """
    Função para calcular o fatorial de um número.
    :param num: O número a ser calculado o fatorial.
    :param show: Valor lógico opcional indicando se será mostrado o processo de cálculo.
    :return: O valor do fatorial do número.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(f"{i}", end="")
            if i > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
    if show:
        print(f)
    return f


# Exemplo de uso da função
n = int(input("Digite um número: "))
mostrar_processo = input("Deseja mostrar o processo de cálculo? [S/N] ").upper() == "S"

resultado = fatorial(n, mostrar_processo)
print(f"O fatorial de {n} é {resultado}.")
