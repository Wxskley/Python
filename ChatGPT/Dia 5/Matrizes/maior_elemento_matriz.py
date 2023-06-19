# Receber a matriz como entrada
matriz = []  # Lista vazia para armazenar os elementos da matriz
linhas = int(
    input("Digite o número de linhas da matriz: ")
)  # Solicita ao usuário o número de linhas da matriz
colunas = int(
    input("Digite o número de colunas da matriz: ")
)  # Solicita ao usuário o número de colunas da matriz

print("Digite os elementos da matriz:")
for i in range(linhas):
    linha = []  # Lista vazia para armazenar os elementos da linha atual
    for j in range(colunas):
        elemento = int(
            input(f"Digite o elemento da posição ({i+1}, {j+1}): ")
        )  # Solicita ao usuário o elemento na posição atual
        linha.append(elemento)  # Adiciona o elemento à lista da linha atual
    matriz.append(linha)  # Adiciona a lista da linha à matriz

# Inicializar a variável com o menor valor possível
maior_elemento = float(
    "-inf"
)  # Variável para armazenar o maior elemento inicializada com um valor muito baixo

# Percorrer a matriz
for linha in matriz:
    for elemento in linha:
        # Verificar se o elemento atual é maior que o valor armazenado em maior_elemento
        if elemento > maior_elemento:
            maior_elemento = elemento  # Atualiza o valor de maior_elemento se o elemento atual for maior

# Imprimir o maior elemento encontrado
print("O maior elemento da matriz é:", maior_elemento)
