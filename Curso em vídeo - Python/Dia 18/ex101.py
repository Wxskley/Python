def voto(ano_nascimento):
    from datetime import date

    idade = date.today().year - ano_nascimento

    if idade < 16:
        return "NEGADO"
    elif 16 <= idade < 18 or idade >= 65:
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"


# Exemplo de uso da função
ano = int(input("Digite o ano de nascimento: "))
resultado = voto(ano)
print(f"Situação do voto: {resultado}")
