# Criando uma tupla
tupla = (1, 2, 3, "a", "b", "c")

# Acessando elementos da tupla
print(tupla[0])  # Exibe 1
print(tupla[3])  # Exibe "a"

# Iterando sobre uma tupla
for elemento in tupla:
    print(elemento)

# Verificando o tamanho da tupla
tamanho = len(tupla)
print(tamanho)  # Exibe 6

# Concatenando tuplas
outra_tupla = (4, 5, 6)
tupla_concatenada = tupla + outra_tupla
print(tupla_concatenada)  # Exibe (1, 2, 3, "a", "b", "c", 4, 5, 6)
