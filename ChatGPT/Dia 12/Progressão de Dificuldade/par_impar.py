# Função para verificar se um número é par ou ímpar
# Dificuldade: 30%
def verificar_par_impar(numero):
    # Verifica se o resto da divisão do número por 2 é igual a zero
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


# Número de exemplo
numero = 17
# Chama a função para verificar se o número é par ou ímpar e imprime o resultado
print(verificar_par_impar(numero))
