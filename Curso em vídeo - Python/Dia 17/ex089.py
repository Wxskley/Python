alunos = []  # Lista composta para armazenar os dados dos alunos

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    aluno = [nome, nota1, nota2]  # Lista com nome e notas do aluno
    alunos.append(aluno)  # Adiciona o aluno à lista de alunos

# Exibição do boletim
print("\nBoletim:")
for aluno in alunos:
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2

    print(f"\nAluno: {nome}")
    print(f"Média: {media}")

    opcao = input("Deseja ver as notas individuais? (s/n): ")
    if opcao.lower() == "s":
        nota1 = aluno[1]
        nota2 = aluno[2]
        print(f"Nota 1: {nota1}")
        print(f"Nota 2: {nota2}")
