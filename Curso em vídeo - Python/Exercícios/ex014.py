temperatura_celsius = float(
    input("Digite a temperatura em Celsius: ")
)  # Lê a temperatura em Celsius fornecida pelo usuário

temperatura_fahrenheit = (
    temperatura_celsius * 9 / 5
) + 32  # Converte a temperatura de Celsius para Fahrenheit utilizando a fórmula de conversão

print(
    "A temperatura em Fahrenheit é: {:.2f} °F".format(temperatura_fahrenheit)
)  # Exibe a temperatura convertida em Fahrenheit com duas casas decimais
