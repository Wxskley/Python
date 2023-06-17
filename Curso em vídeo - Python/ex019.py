import random

# Solicita ao usuário que digite o nome dos alunos
aluno1 = input("Digite o nome do primeiro aluno:")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno:")
aluno4 = input("Digite o nome do quarto aluno: ")

# Armazena os nomes dos alunos em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Escolhe aleatoriamente um aluno da lista
alunoEscolhido = random.choice(alunos)

# Exibe o nome do aluno escolhido
print(f"O aluno escolhido foi: {alunoEscolhido}")
