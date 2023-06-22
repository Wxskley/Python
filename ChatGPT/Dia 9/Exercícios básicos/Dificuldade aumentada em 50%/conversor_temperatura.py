# Solicita ao usuário que insira a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))

# Converte a temperatura para Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Converte a temperatura para Kelvin
kelvin = celsius + 273.15

# Exibe as temperaturas convertidas
print("Temperatura em Fahrenheit:", fahrenheit)
print("Temperatura em Kelvin:", kelvin)
