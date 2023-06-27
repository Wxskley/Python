n = int(input("Digite um número inteiro: "))

# Verifica se o número digitado é negativo ou zero
if n <= 0:
    print("O número deve ser positivo e diferente de zero.")
else:
    # Caso contrário, calcula e exibe os n primeiros elementos da sequência de Fibonacci
    primeiro_termo = 0
    segundo_termo = 1
    contador = 0

    while contador < n:
        print(primeiro_termo)

        proximo_termo = primeiro_termo + segundo_termo
        primeiro_termo = segundo_termo
        segundo_termo = proximo_termo

        contador += 1
