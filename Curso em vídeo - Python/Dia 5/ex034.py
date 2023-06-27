salario = float(input("Informe o seu salário: "))

aumento_10 = salario * 1.10  # Cálculo do novo salário com aumento de 10%
aumento_15 = salario * 1.15  # Cálculo do novo salário com aumento de 15%

if salario > 1250:
    print(f"Seu salário teve um aumento de 10% passando a ser {aumento_10:.2f}")
else:
    print(f"Seu salário teve um aumento de 15% passando a ser {aumento_15:.2f}")
