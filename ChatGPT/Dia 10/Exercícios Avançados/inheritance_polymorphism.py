# Vamos criar algumas formas e calcular suas áreas usando programação orientada a objetos


# Começamos com uma classe base chamada Shape (Forma)
class Shape:
    def area(self):
        # Essa função retorna a área da forma, mas vamos deixar que as subclasses implementem
        # sua própria versão dessa função
        pass


# Vamos criar uma subclasse de Shape chamada Square (Quadrado)
class Square(Shape):
    def __init__(self, side_length):
        # O construtor recebe o comprimento do lado do quadrado
        self.side_length = side_length

    def area(self):
        # Aqui, calculamos a área do quadrado multiplicando o comprimento do lado por ele mesmo
        return self.side_length**2


# Vamos criar outra subclasse de Shape chamada Circle (Círculo)
class Circle(Shape):
    def __init__(self, radius):
        # O construtor recebe o raio do círculo
        self.radius = radius

    def area(self):
        # Aqui, calculamos a área do círculo usando a fórmula π * raio * raio
        return 3.14 * self.radius**2


# Vamos criar objetos das classes Square e Circle
square = Square(5)
print(square.area())  # Imprime a área do quadrado

circle = Circle(3)
print(circle.area())  # Imprime a área do círculo
