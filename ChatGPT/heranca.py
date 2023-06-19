# Classe base "Animal"
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("O animal faz um som.")


# Classe derivada "Cachorro" herda de "Animal"
class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late.")


# Criação de objetos das classes
animal = Animal("Animal")
animal.fazer_som()

cachorro = Cachorro("Rex")
cachorro.fazer_som()
