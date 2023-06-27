from datetime import date

ano_atual = date.today().year  # Obtém o ano atual

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade < 18:
    anos_restantes = 18 - idade
    print(
        f"Você ainda vai se alistar ao serviço militar daqui a {anos_restantes} anos."
    )
elif idade == 18:
    print("É hora de se alistar ao serviço militar!")
else:
    anos_passados = idade - 18
    print(f"Já passou do tempo do alistamento militar há {anos_passados} anos.")
