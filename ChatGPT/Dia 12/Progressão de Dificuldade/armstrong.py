# Função para verificar se um número é um número de Armstrong
# Dificuldade: 40%
def verificar_armstrong(numero):
    # Converte o número em uma string
    numero_str = str(numero)
    # Calcula o número de dígitos do número
    num_digitos = len(numero_str)
    # Inicializa a soma como zero
    soma = 0
    # Percorre cada dígito do número
    for digito in numero_str:
        # Eleva o dígito à potência do número de dígitos e adiciona à soma
        soma += int(digito) ** num_digitos
    # Verifica se a soma dos dígitos elevados é igual ao número
    if soma == numero:
        return True
    else:
        return False


# Número de exemplo
numero = 153
# Chama a função para verificar se o número é um número de Armstrong e imprime o resultado
print(verificar_armstrong(numero))
