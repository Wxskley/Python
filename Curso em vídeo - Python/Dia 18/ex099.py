def maior(*valores):
    maior_valor = None

    for valor in valores:
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor

    return maior_valor


# Exemplo de uso da função
resultado = maior(10, 5, 8, 12, 3)
print(f"O maior valor é: {resultado}")

# Outro exemplo
resultado = maior(7, 2, 9, 4)
print(f"O maior valor é: {resultado}")
