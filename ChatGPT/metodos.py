# Definição da classe "Calculadora"
class Calculadora:
    def __init__(self):
        self.resultado = 0

    def somar(self, num1, num2):
        self.resultado = num1 + num2

    def subtrair(self, num1, num2):
        self.resultado = num1 - num2


# Criação de um objeto da classe "Calculadora"
calculadora = Calculadora()

# Chamada dos métodos do objeto
calculadora.somar(5, 3)
print("Resultado da soma:", calculadora.resultado)

calculadora.subtrair(10, 7)
print("Resultado da subtração:", calculadora.resultado)
