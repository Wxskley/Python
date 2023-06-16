import json
import random

# Abre o arquivo "words.json" contendo as palavras para o jogo
f = open("Projetos em Python para Iniciantes\Termoo\words.json", encoding="utf8")

# Carrega o conteúdo do arquivo JSON em um dicionário
words = json.load(f)

# Escolhe aleatoriamente uma chave do dicionário
choice_c = random.choice(list(words.keys()))

# Imprime uma mensagem de boas-vindas
print("Ola, seja bem vindo!")
print("#################################")

# Define o número de tentativas disponíveis e uma variável para verificar se o jogador venceu
n_choices = 5
win = False

# Loop principal do jogo
while n_choices > 0 and win is not True:
    # Exibe a dica correspondente à chave escolhida
    print("Dica: " + words[choice_c])
    # Solicita ao jogador que insira uma resposta (data no formato DDMMAAAA)
    answer_user = input("Data: DDMMAAAA\n")
    print("################## \n")

    # Verifica se a resposta tem o tamanho correto (8 dígitos)
    if len(answer_user) != 8:
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue

    # Verifica se a resposta contém apenas dígitos
    if answer_user.isdigit():
        check = []
        pontuation = 0

        # Compara cada dígito da resposta com o dígito correspondente da chave escolhida
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("✅")  # Marca um acerto com um símbolo de check
                pontuation = pontuation + 1
            else:
                check.append("💢")  # Marca um erro com um símbolo de cross

        print("Resposta: \n")
        print("|".join(check))  # Exibe os símbolos de acerto e erro separados por '|'
        print(" |".join(answer_user))  # Exibe a resposta digitada pelo jogador
        print("#######################\n")

        # Verifica se todas as posições da resposta estão corretas (pontuação máxima)
        if pontuation == 8:
            win = True
    else:
        print("Erro na entrada. A resposta deve ser uma data!")
        continue

    n_choices = n_choices - 1

# Verifica se o jogador venceu ou perdeu e exibe a mensagem correspondente
if win == True:
    print("VITÓRIA!!!")
else:
    print("DERROTA!")
    print("A resposta era: " + choice_c)
