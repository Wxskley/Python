aluno = {}  # Dicionário para armazenar os dados do aluno

aluno["nome"] = input("Digite o nome do aluno: ")  # Lê o nome do aluno
aluno["media"] = float(
    input("Digite a média do aluno: ")
)  # Lê a média do aluno como um número decimal

# Verifica a situação do aluno com base na média
if aluno["media"] >= 7.0:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

# Exibe na tela os dados do aluno
print("\nDados do Aluno:")
print(f"Nome: {aluno['nome']}")
print(f"Média: {aluno['media']}")
print(f"Situação: {aluno['situacao']}")
