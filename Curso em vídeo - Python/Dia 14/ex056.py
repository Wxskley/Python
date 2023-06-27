soma_idades = 0  # Variável para armazenar a soma das idades
maior_idade_homem = 0  # Variável para armazenar a maior idade entre os homens
nome_homem_velho = ""  # Variável para armazenar o nome do homem mais velho
mulheres_menos_vinte = (
    0  # Variável para contar a quantidade de mulheres com menos de 20 anos
)

for i in range(1, 5):  # Loop para ler os dados das 4 pessoas
    print(f"\n--- Pessoa {i} ---")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ")

    soma_idades += idade  # Adiciona a idade à soma total das idades

    if sexo.upper() == "M" and idade > maior_idade_homem:
        maior_idade_homem = idade  # Atualiza a maior idade entre os homens
        nome_homem_velho = nome  # Armazena o nome do homem mais velho

    if sexo.upper() == "F" and idade < 20:
        mulheres_menos_vinte += (
            1  # Incrementa o contador de mulheres com menos de 20 anos
        )

media_idades = soma_idades / 4  # Calcula a média de idade

# Imprime o resultado
print(f"\nMédia de idade do grupo: {media_idades:.1f} anos")
print(f"Nome do homem mais velho: {nome_homem_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_vinte}")
