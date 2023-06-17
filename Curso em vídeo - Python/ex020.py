import random

# Solicita o nome dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Armazena os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralha a ordem dos alunos na lista
random.shuffle(alunos)

# Exibe a ordem de apresentação
print("A ordem de apresentação será: ")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")
