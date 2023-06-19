texto = "Este é um exemplo\npara processamento de\ntexto em Python."

# Definição do texto a ser processado, contendo quebras de linha ("\n")

linhas = texto.split("\n")

# Utilização do método split() para dividir o texto em uma lista de linhas, utilizando a quebra de linha como separador

for linha in linhas:
    print(linha)

# Laço de repetição que percorre cada linha da lista e imprime a linha na saída
