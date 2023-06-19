# Definição da classe "Cachorro"
class Cachorro:
    # Método construtor da classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método da classe para latir
    def latir(self):
        print("Au au!")


# Criação de um objeto da classe "Cachorro"
meuCachorro = Cachorro("Rex", 3)

# Acesso aos atributos e chamada de método do objeto
print("Nome do cachorro:", meuCachorro.nome)
print("Idade do cachorro:", meuCachorro.idade)
meuCachorro.latir()
