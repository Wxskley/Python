# Função para calcular o MDC entre dois números
# Dificuldade: 45%
def calcular_mdc(numero1, numero2):
    # Inicializa o maior divisor comum como o menor dos números
    mdc = min(numero1, numero2)
    # Enquanto o mdc não for encontrado, decrementa o valor do mdc
    while True:
        # Verifica se ambos os números são divisíveis pelo mdc atual
        if numero1 % mdc == 0 and numero2 % mdc == 0:
            # Se sim, encontramos o mdc
            break
        # Se não, decrementa o mdc e continua a verificação
        mdc -= 1
    # Retorna o valor do mdc encontrado
    return mdc


# Números de exemplo
numero1 = 24
numero2 = 36
# Chama a função para calcular o MDC entre os números e imprime o resultado
print(calcular_mdc(numero1, numero2))
