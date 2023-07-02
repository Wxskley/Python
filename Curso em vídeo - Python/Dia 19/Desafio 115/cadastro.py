def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade da pessoa: ")

    # Abrir o arquivo em modo de escrita (append) e adicionar os dados da pessoa
    with open(r"Curso em vídeo - Python\Dia 19\Desafio 115\pessoas.txt", "a") as arquivo:
        arquivo.write(f"{nome},{idade}\n")

    print("Pessoa cadastrada com sucesso!")


def listar_pessoas():
    # Abrir o arquivo em modo de leitura e exibir os dados das pessoas
    with open(r"Curso em vídeo - Python\Dia 19\Desafio 115\pessoas.txt", "r") as arquivo:
        pessoas = arquivo.readlines()

    if pessoas:
        print("Pessoas cadastradas:")
        for pessoa in pessoas:
            nome, idade = pessoa.strip().split(",")
            print(f"Nome: {nome} | Idade: {idade}")
    else:
        print("Não há pessoas cadastradas.")
