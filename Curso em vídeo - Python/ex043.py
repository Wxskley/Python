peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura**2)  # Calcula o IMC

if imc < 18.5:
    status = "Abaixo do peso"
elif 18.5 <= imc < 25:
    status = "Peso ideal"
elif 25 <= imc < 30:
    status = "Sobrepeso"
elif 30 <= imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade mórbida"

print(f"O seu IMC é {imc:.2f}")
print(f"Status: {status}")
