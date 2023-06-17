print(
    """
    Seja bem-vindo ao jogo de perguntas e respostas.
    
    Você responderá 5 perguntas e saberá quanto
    entende do assunto.
"""
)  # Exibe uma mensagem de boas-vindas e instruções do jogo na tela

print("Vamos começar.")  # Exibe uma mensagem indicando o início do jogo
print("Qual é o Dinossauro mais feroz do planeta?")
print(
    "a) Triceratops\nb) T Rex\nc) Velociraptor\nd) Ramon Dino"
)  # Exibe a pergunta e as opções de resposta

resposta = input(
    "Digite uma das opções: "
).lower()  # Solicita ao usuário que digite sua resposta e a armazena na variável "resposta", convertendo-a para letras minúsculas

pontos = 0  # Variável para armazenar a pontuação do jogador

if resposta == "d":  # Verifica se a resposta do jogador está correta (opção "d")
    print("Você acertou!")  # Exibe uma mensagem informando que o jogador acertou
    pontos = pontos + 20  # Adiciona 20 pontos à pontuação do jogador
else:
    print("Você errou!")  # Exibe uma mensagem informando que o jogador errou
