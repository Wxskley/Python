nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2  # Calcula a média das notas

if media < 5.0:
    print("Reprovado")
elif media < 7.0:
    print("Recuperação")
else:
    print("Aprovado")
