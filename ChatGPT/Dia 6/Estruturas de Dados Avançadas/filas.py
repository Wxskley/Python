from collections import deque

# Criando uma fila
fila = deque()

# Adicionando elementos à fila
fila.append(1)
fila.append(2)
fila.append(3)

# Removendo elementos da fila
primeiro_elemento = fila.popleft()

# Verificando o tamanho da fila
tamanho = len(fila)

# Iterando sobre uma fila
for elemento in fila:
    print(elemento)

# Verificando se a fila está vazia
vazia = len(fila) == 0
print(vazia)  # Exibe True
