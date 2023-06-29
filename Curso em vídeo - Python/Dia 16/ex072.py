# Tupla com os números por extenso
numeros_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

# Solicita o número ao usuário
numero = int(input("Digite um número entre 0 e 20: "))

# Verifica se o número está dentro do intervalo válido
if 0 <= numero <= 20:
    # Exibe o número por extenso
    print(f"O número {numero} por extenso é: {numeros_extenso[numero]}")
else:
    print("Número inválido. Digite um número entre 0 e 20.")
