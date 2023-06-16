from functions import *

# Importa todas as funções definidas no arquivo "functions.py"

print("##########################\n")
print("Qual a data de vencimento?")
print("Formato: DIA-MES-ANO. Exemplo: 22-03-2002\n")
print("##########################\n")

# Solicita ao usuário que insira a data de vencimento no formato DIA-MES-ANO

due_date = input("")

# Verifica o tamanho da entrada do usuário

if len(due_date) == 10:
    # Chama a função "verify_due" do arquivo "functions.py" e passa a data de vencimento como argumento
    print(verify_due(due_date))
else:
    print("Entrada inválida!")
