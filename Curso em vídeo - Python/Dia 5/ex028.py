import random

# O computador "pensa" em um número aleatório entre 0 e 5
numero_pensado = random.randint(0, 5)

# Solicita ao usuário que tente adivinhar o número pensado pelo computador
numero_usuario = int(
    input("Tente adivinhar o número que estou pensando (entre 0 e 5): ")
)

# Verifica se o número fornecido pelo usuário é igual ao número pensado pelo computador
if numero_usuario == numero_pensado:
    # Se os números forem iguais, exibe a mensagem de acerto
    print("Parabéns! Você acertou o número.")
else:
    # Caso contrário, exibe a mensagem de erro e revela o número correto
    print("Você errou. O número correto era", numero_pensado)
