# Função para verificar se duas palavras são anagramas
# Dificuldade: 35%
def verificar_anagramas(palavra1, palavra2):
    # Remove os espaços em branco das palavras e as converte para letras minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    # Verifica se as palavras têm o mesmo tamanho
    if len(palavra1) != len(palavra2):
        return False
    # Verifica se as palavras têm as mesmas letras (desconsiderando a ordem)
    if sorted(palavra1) == sorted(palavra2):
        return True
    else:
        return False


# Palavras de exemplo
palavra1 = "roma"
palavra2 = "amor"
# Chama a função para verificar se as palavras são anagramas e imprime o resultado
print(verificar_anagramas(palavra1, palavra2))
