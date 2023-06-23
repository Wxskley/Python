# Vamos começar com um nó inicial vazio
root = None


# Criamos uma classe chamada Node (Nó) que representa um nó na nossa árvore
class Node:
    def __init__(self, value):
        # Cada nó tem um valor e duas referências, uma para o nó esquerdo e outra para o nó direito
        self.value = value
        self.left = None
        self.right = None


# Vamos criar uma função chamada insert (inserir) para adicionar valores à nossa árvore
def insert(root, value):
    # Se o nó atual for vazio, significa que estamos adicionando o primeiro valor à árvore
    if root is None:
        # Então criamos um novo nó com o valor e o tornamos a raiz da árvore
        return Node(value)

    # Se o valor que queremos adicionar for menor que o valor do nó atual
    if value < root.value:
        # Vamos verificar se o nó esquerdo está vazio, se estiver, criamos um novo nó com o valor
        # e o definimos como o nó esquerdo do nó atual
        root.left = insert(root.left, value)
    else:
        # Caso contrário, se o valor que queremos adicionar for maior ou igual ao valor do nó atual
        # Vamos verificar se o nó direito está vazio, se estiver, criamos um novo nó com o valor
        # e o definimos como o nó direito do nó atual
        root.right = insert(root.right, value)

    # Retornamos o nó atualizado
    return root


# Vamos criar uma função chamada inorder_traversal (percurso em ordem) para percorrer a árvore em ordem
def inorder_traversal(root):
    # Se o nó atual não for vazio
    if root:
        # Vamos primeiro percorrer o nó esquerdo
        inorder_traversal(root.left)
        # Em seguida, vamos imprimir o valor do nó atual
        print(root.value)
        # Por fim, vamos percorrer o nó direito
        inorder_traversal(root.right)


# Agora vamos inserir alguns valores na nossa árvore
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 2)
root = insert(root, 4)

# Vamos percorrer a árvore em ordem e imprimir os valores
inorder_traversal(root)
