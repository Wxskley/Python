from datetime import date

# Obtém o ano atual
ano_atual = date.today().year


# Função para calcular a idade e o ano de aposentadoria
def calcular_idade_e_aposentadoria(ano_nascimento, ano_contratacao, salario):
    idade = ano_atual - ano_nascimento
    aposentadoria = (
        ano_contratacao + 35
    )  # Considerando aposentadoria após 35 anos de trabalho
    return idade, aposentadoria


# Criação do dicionário para armazenar as informações
pessoa = {}
pessoa["Nome"] = input("Digite o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
pessoa["Idade"], pessoa["Ano de Aposentadoria"] = calcular_idade_e_aposentadoria(
    ano_nascimento, 0, 0
)

carteira_trabalho = int(
    input("Digite o número da carteira de trabalho (0 se não possui): ")
)
if carteira_trabalho != 0:
    pessoa["CTPS"] = carteira_trabalho
    pessoa["Ano de Contratação"] = int(input("Digite o ano de contratação: "))
    pessoa["Salário"] = float(input("Digite o salário: "))
    pessoa["Idade"], pessoa["Ano de Aposentadoria"] = calcular_idade_e_aposentadoria(
        ano_nascimento, pessoa["Ano de Contratação"], pessoa["Salário"]
    )

# Exibição dos dados
print("\nDados da Pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
