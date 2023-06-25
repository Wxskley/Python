# Função para verificar se um número é um número de Harshad
# Dificuldade: 65%
def verificar_numero_harshad(numero):
    # Calcula a soma dos dígitos do número
    soma_digitos = sum(int(digito) for digito in str(numero))
    # Verifica se o número é divisível pela soma dos dígitos
    if numero % soma_digitos == 0:
        return True
    else:
        return False


# Número de exemplo
numero = 18
# Chama a função para verificar se o número é um número de Harshad e imprime o resultado
print(verificar_numero_harshad(numero))
