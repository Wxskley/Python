numero1 = float(
    input("Digite o primeiro número: ")
)  # Lê o primeiro número digitado pelo usuário
numero2 = float(
    input("Digite o segundo número: ")
)  # Lê o segundo número digitado pelo usuário
numero3 = float(
    input("Digite o terceiro número: ")
)  # Lê o terceiro número digitado pelo usuário

maior = max(
    numero1, numero2, numero3
)  # Encontra o maior número entre os três valores fornecidos
menor = min(
    numero1, numero2, numero3
)  # Encontra o menor número entre os três valores fornecidos

print("O maior número é:", maior)  # Exibe na tela o maior número
print("O menor número é:", menor)  # Exibe na tela o menor número
