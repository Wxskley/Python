import re

# Importação do módulo re para trabalhar com expressões regulares

texto = "Eu tenho 3 maçãs e 2 bananas na minha cesta."

# Definição do texto a ser analisado

padrao = r"\d+"

# Definição do padrão de busca utilizando uma expressão regular
# O padrão "\d+" busca uma ou mais ocorrências de dígitos

numeros = re.findall(padrao, texto)

# Utilização da função findall() do módulo re para encontrar todas as correspondências do padrão no texto
# Retorna uma lista com os números encontrados

print(numeros)

# Impressão da lista de números encontrados na saída
