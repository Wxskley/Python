from datetime import date

ano_atual = date.today().year  # Obtém o ano atual

ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
idade = ano_atual - ano_nascimento

if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Júnior"
elif idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"

print(f"A categoria do atleta é: {categoria}")
