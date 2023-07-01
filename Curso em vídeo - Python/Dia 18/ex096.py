def area(largura, comprimento):
    area_terreno = largura * comprimento
    return area_terreno


largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))

area_terreno = area(largura, comprimento)

print(f"A área do terreno é de {area_terreno} metros quadrados.")
