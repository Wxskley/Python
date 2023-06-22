import calendar

# Solicita ao usuário que insira o número do mês e o ano
mes = int(input("Digite o número do mês: "))
ano = int(input("Digite o ano: "))

# Exibe o calendário do mês
print(calendar.month(ano, mes))
