# Definição da classe "Pessoa"
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# Criação de um objeto da classe "Pessoa"
pessoa1 = Pessoa("João", 30)

# Acesso aos atributos do objeto
print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
