# Lê quatro valores pelo teclado e armazena em uma tupla
valores = tuple(int(input("Digite um valor: ")) for _ in range(4))

# Conta quantas vezes o valor 9 aparece na tupla
qtd_nove = valores.count(9)

# Verifica em que posição foi digitado o primeiro valor 3
posicao_tres = valores.index(3) if 3 in valores else None

# Filtra os números pares presentes na tupla
numeros_pares = tuple(valor for valor in valores if valor % 2 == 0)

# Exibe os resultados
print("Quantidade de vezes que o valor 9 apareceu:", qtd_nove)
print("Posição do primeiro valor 3:", posicao_tres)
print("Números pares:", numeros_pares)
