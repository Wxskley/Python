expressao = input(
    "Digite uma expressão com parênteses: "
)  # Solicita ao usuário a expressão a ser verificada

pilha = []  # Cria uma pilha vazia para armazenar os parênteses

for caractere in expressao:
    if caractere == "(":  # Verifica se o caractere é um parêntese de abertura
        pilha.append(caractere)  # Adiciona o parêntese na pilha
    elif caractere == ")":  # Verifica se o caractere é um parêntese de fechamento
        if len(pilha) == 0:  # Verifica se a pilha está vazia
            pilha.append(caractere)  # Adiciona o parêntese na pilha, indicando um erro
            break  # Encerra o loop
        else:
            pilha.pop()  # Remove o parêntese de abertura correspondente da pilha

if len(pilha) == 0:  # Verifica se a pilha está vazia ao final do loop
    print("Expressão válida: os parênteses estão corretamente balanceados.")
else:
    print("Expressão inválida: os parênteses não estão corretamente balanceados.")
