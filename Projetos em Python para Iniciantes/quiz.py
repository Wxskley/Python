print(
    "Seja muito bem vindo ao quiz do Weskley!"
)  # Exibe uma mensagem de boas-vindas ao quiz

answer_user = input(
    "Quer começar? (S/N) "
)  # Solicita ao usuário se ele quer começar o quiz e armazena a resposta na variável answer_user

if (
    answer_user.lower() != "s"
):  # Verifica se a resposta do usuário é diferente de "S" (iniciais de "Sim")
    quit()  # Encerra o programa se o usuário não quiser começar o quiz

score = 0  # Inicializa a pontuação do jogador como 0

print("Começando...")  # Exibe uma mensagem indicando que o quiz está começando

print(
    "Quem desenvolveu o jogo Grand Theft Auto (GTA)?"
)  # Exibe a pergunta do primeiro questionário
print("(A) Rockstar Games")
print("(B) Ubisoft")
print("(C) Activision")
print("(D) EA")
answer_1 = input(
    "Resposta: "
)  # Solicita ao usuário a resposta para a pergunta do primeiro questionário e armazena na variável answer_1

if answer_1 == "A":  # Verifica se a resposta do usuário está correta
    print("Correto!")  # Exibe uma mensagem informando que a resposta está correta
    score = score + 1  # Aumenta a pontuação do jogador em 1 ponto
else:
    print("Incorreto!")  # Exibe uma mensagem informando que a resposta está incorreta

print(
    "Qual o nome do protagonista do jogo GTA San Andreas?"
)  # Exibe a pergunta do segundo questionário
print("(A) Carlos Jonh")
print("(B) Carl Jonhson")
print("(C) Carl Jaqueline")
print("(D) Carlos Jonhson")
answer_2 = input(
    "Resposta: "
)  # Solicita ao usuário a resposta para a pergunta do segundo questionário e armazena na variável answer_2

if answer_2 == "B":  # Verifica se a resposta do usuário está correta
    print("Correto!")  # Exibe uma mensagem informando que a resposta está correta
    score = score + 1  # Aumenta a pontuação do jogador em 1 ponto
else:
    print("Incorreto!")  # Exibe uma mensagem informando que a resposta está incorreta

print(
    f"Quiz acabou... Pontuação: {score}/2"
)  # Exibe uma mensagem informando que o quiz acabou e mostra a pontuação final do jogador
