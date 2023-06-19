# Solicita ao usuário que digite um texto ou frase
texto = input("Digite um texto ou frase: ")

# Remove os espaços em branco no início e no final do texto usando o método strip()
# Divide o texto em palavras usando o método split() e armazena as palavras em uma lista chamada palavras
palavras = texto.strip().split()

# Imprime o número de palavras contidas na lista palavras usando a função len()
print(len(palavras))
