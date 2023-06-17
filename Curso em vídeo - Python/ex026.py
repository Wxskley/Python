frase = input(
    "Digite uma frase: "
)  # Solicita ao usuário que digite uma frase e armazena na variável "frase"

quantidade_a = frase.lower().count(
    "a"
)  # Calcula a quantidade de vezes que a letra 'a' aparece na frase
primeira_posicao = (
    frase.lower().find("a") + 1
)  # Encontra a primeira posição em que a letra 'a' aparece na frase
ultima_posicao = (
    frase.lower().rfind("a") + 1
)  # Encontra a última posição em que a letra 'a' aparece na frase

# Exibe as informações para o usuário
print("Quantidade de vezes que a letra 'a' aparece: ", quantidade_a)
print("Posição da primeira ocorrência da letra 'a': ", primeira_posicao)
print("Posição da última ocorrência da letra 'a': ", ultima_posicao)
