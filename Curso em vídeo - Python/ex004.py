algo = input(
    "Digite algo: "
)  # Solicita ao usuário que digite algo e armazena na variável 'algo'.
print(
    "O tipo primitivo desse valor é {}".format(type(algo))
)  # Imprime o tipo primitivo do valor digitado.

# Verifica se o valor consiste apenas de espaços em branco e imprime o resultado.
print("Só tem espaços? {}".format(algo.isspace()))

# Verifica se o valor é numérico e imprime o resultado.
print("É um número? {}".format(algo.isnumeric()))

# Verifica se o valor é composto apenas por caracteres alfabéticos e imprime o resultado.
print("É alfabético? {}".format(algo.isalpha()))

# Verifica se o valor é alfanumérico, ou seja, se é composto por letras e números, e imprime o resultado.
print("É alfanumérico? {}".format(algo.isalnum()))

# Verifica se o valor está em maiúsculas e imprime o resultado.
print("Está em maiúsculas? {}".format(algo.isupper()))

# Verifica se o valor está em minúsculas e imprime o resultado.
print("Está em minúsculas? {}".format(algo.islower()))

# Verifica se o valor está capitalizado, ou seja, se a primeira letra de cada palavra está em maiúscula, e imprime o resultado.
print("Está capitalizada? {}".format(algo.istitle()))
