# Criando um conjunto
conjunto = {1, 2, 3, 4, 5}

# Adicionando elementos ao conjunto
conjunto.add(6)
conjunto.add(7)

# Verificando se um elemento pertence ao conjunto
print(3 in conjunto)  # Exibe True
print(8 in conjunto)  # Exibe False

# Removendo elementos do conjunto
conjunto.remove(4)

# Iterando sobre um conjunto
for elemento in conjunto:
    print(elemento)

# Realizando operações entre conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
diferenca = conjunto1.difference(conjunto2)
print(uniao)  # Exibe {1, 2, 3, 4, 5}
print(intersecao)  # Exibe {3}
print(diferenca)  # Exibe {1, 2}
