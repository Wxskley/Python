sexo = input("Digite o sexo (M/F): ")  # Solicita ao usuário que digite o sexo

# Enquanto o sexo não for "M" nem "F", continua solicitando a digitação
while sexo.upper() != "M" and sexo.upper() != "F":
    print("Valor incorreto! Digite novamente.")  # Exibe mensagem de valor incorreto
    sexo = input("Digite o sexo (M/F): ")  # Solicita novamente a digitação do sexo

print("Sexo registrado: ", sexo)  # Imprime o sexo registrado
