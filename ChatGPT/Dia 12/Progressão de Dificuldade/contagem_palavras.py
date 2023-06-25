# Função para contar palavras em um texto
# Dificuldade: 15%
def contar_palavras(texto):
    # Divide o texto em palavras usando o espaço como separador
    palavras = texto.split()
    # Retorna a quantidade de palavras encontradas
    return len(palavras)


# Texto de exemplo
texto = "Este é um exemplo de texto"
# Chama a função para contar as palavras e imprime o resultado
print(contar_palavras(texto))
