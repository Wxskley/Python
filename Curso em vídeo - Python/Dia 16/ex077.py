# Tupla com várias palavras
palavras = ("python", "programação", "computador", "internet", "desenvolvimento")


# Função para verificar as vogais em uma palavra
def mostrar_vogais(palavra):
    vogais = ""
    for letra in palavra:
        if letra.lower() in "aeiou":
            vogais += letra
    return vogais


# Mostrar as vogais de cada palavra
for palavra in palavras:
    vogais = mostrar_vogais(palavra)
    print(f"Vogais de {palavra}: {vogais}")
