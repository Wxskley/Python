def fatorial(n):
    # Função para calcular o fatorial de um número

    if n == 0:
        # Se o número for igual a 0, retornamos 1, pois 0! = 1
        return 1
    else:
        # Caso contrário, calculamos o fatorial recursivamente
        return n * fatorial(n - 1)


resultado_fatorial = fatorial(5)
# Chamada da função fatorial para o número 5

print(resultado_fatorial)
# Exibe o resultado do fatorial
