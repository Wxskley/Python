# Classe base "Animal"
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass


# Classes derivadas com diferentes comportamentos
class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late.")


class Gato(Animal):
    def fazer_som(self):
        print("O gato mia.")


# Função que recebe objetos de diferentes classes e chama o método fazer_som()
def emitir_som(animal):
    animal.fazer_som()


# Criação de objetos das classes e chamada da função emitir_som()
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

emitir_som(cachorro)
emitir_som(gato)
