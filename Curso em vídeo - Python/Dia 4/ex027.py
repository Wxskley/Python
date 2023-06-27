nome_completo = input(
    "Digite seu nome completo: "
)  # Solicita ao usuário que digite o nome completo e armazena na variável "nome_completo"

nomes = (
    nome_completo.split()
)  # Separa o nome completo em uma lista de palavras (nomes). Cada palavra é um elemento da lista.

primeiro_nome = nomes[0]  # O primeiro nome é o primeiro elemento da lista
ultimo_nome = nomes[-1]  # O último nome é o último elemento da lista

print("Primeiro nome: ", primeiro_nome)  # Exibe na tela o primeiro nome
print("Último nome: ", ultimo_nome)  # Exibe na tela o último nome
