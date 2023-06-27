maior_peso = float(
    "-inf"
)  # Variável para armazenar o maior peso, inicializada com um valor muito baixo
menor_peso = float(
    "inf"
)  # Variável para armazenar o menor peso, inicializada com um valor muito alto

for i in range(1, 6):  # Loop para ler os cinco pesos
    peso = float(input(f"Digite o peso da pessoa {i}: "))

    if peso > maior_peso:
        maior_peso = peso  # Atualiza o maior peso, se necessário

    if peso < menor_peso:
        menor_peso = peso  # Atualiza o menor peso, se necessário

# Imprime o resultado
print(f"\nMaior peso lido: {maior_peso}")
print(f"Menor peso lido: {menor_peso}")
