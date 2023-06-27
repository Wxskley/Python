nome = input("Digite o seu nome completo: ")

# Lê o nome completo da pessoa

nome_maiusculo = nome.upper()
# Converte o nome para letras maiúsculas

nome_minusculo = nome.lower()
# Converte o nome para letras minúsculas

quantidade_letras_total = len(nome.replace(" ", ""))
# Remove os espaços em branco do nome e conta a quantidade de letras

primeiro_nome = nome.split()[0]
# Divide o nome completo em partes separadas pelo espaço em branco e seleciona o primeiro nome

quantidade_letras_primeiro_nome = len(primeiro_nome)
# Conta a quantidade de letras no primeiro nome

# Exibe os resultados
print("Nome em maiúsculas:", nome_maiusculo)
print("Nome em minúsculas:", nome_minusculo)
print("Quantidade de letras (sem espaços):", quantidade_letras_total)
print("Quantidade de letras no primeiro nome:", quantidade_letras_primeiro_nome)
