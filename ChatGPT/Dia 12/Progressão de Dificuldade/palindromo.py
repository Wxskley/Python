# Função para verificar se uma palavra é um palíndromo
# Dificuldade: 40%
def verificar_palindromo(palavra):
    # Remove os espaços em branco da palavra e a converte para letras minúsculas
    palavra = palavra.replace(" ", "").lower()
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    # Verifica se a palavra é igual à sua versão invertida
    if palavra == palavra_invertida:
        return True
    else:
        return False


# Palavra de exemplo
palavra = "arara"
# Chama a função para verificar se a palavra é um palíndromo e imprime o resultado
print(verificar_palindromo(palavra))
