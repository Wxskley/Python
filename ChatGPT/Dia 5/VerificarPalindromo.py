def verifica_palindromo(palavra):
    palavra = palavra.lower()  # Converte a palavra para minúsculas
    palavra_invertida = palavra[::-1]  # Inverte a palavra

    if palavra == palavra_invertida:
        return True
    else:
        return False


# Exemplos de uso
print(verifica_palindromo("arara"))  # True
print(verifica_palindromo("python"))  # False
