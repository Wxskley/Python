# Função para calcular a área de um círculo
# Dificuldade: 55%
def calcular_area_circulo(raio):
    # Importa a constante pi do módulo math
    from math import pi

    # Calcula a área utilizando a fórmula pi * raio^2
    area = pi * raio**2
    # Retorna a área
    return area


# Raio de exemplo
raio = 5
# Chama a função para calcular a área do círculo e imprime o resultado
print(calcular_area_circulo(raio))
