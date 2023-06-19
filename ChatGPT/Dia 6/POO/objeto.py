# Definição da classe "Carro"
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


# Criação de objetos da classe "Carro"
carro1 = Carro("Ford", "Fiesta")
carro2 = Carro("Chevrolet", "Cruze")

# Acesso aos atributos dos objetos
print("Marca do Carro 1:", carro1.marca)
print("Modelo do Carro 2:", carro2.modelo)
