viagem_km = float(
    input("Digite a distância da sua viagem em km: ")
)  # Solicita ao usuário a distância da viagem em km

passagem_menos_200km = 0.50  # Valor da passagem para viagens de até 200 km
passagem_mais_longa = 0.45  # Valor da passagem para viagens acima de 200 km

if viagem_km > 200:
    # Se a distância da viagem for maior que 200 km, calcula o preço da passagem multiplicando a distância pelo valor da passagem mais longa
    print(f"Sua viagem custa R${viagem_km * passagem_mais_longa}")
else:
    # Caso contrário, a distância da viagem é igual ou menor que 200 km, então calcula o preço da passagem multiplicando a distância pelo valor da passagem para viagens até 200 km
    print(f"Sua viagem custa R${viagem_km * passagem_menos_200km}")
