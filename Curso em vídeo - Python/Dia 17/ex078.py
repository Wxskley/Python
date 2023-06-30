# Lista para armazenar os valores
numeros = []

# Loop para ler os valores
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    numeros.append(valor)

# Encontrar o maior e o menor valor
maior_valor = max(numeros)
menor_valor = min(numeros)

# Encontrar as posições do maior e do menor valor
posicao_maior = numeros.index(maior_valor)
posicao_menor = numeros.index(menor_valor)

# Mostrar os resultados
print(
    f"O maior valor digitado foi {maior_valor} e sua posição na lista é {posicao_maior}."
)
print(
    f"O menor valor digitado foi {menor_valor} e sua posição na lista é {posicao_menor}."
)
