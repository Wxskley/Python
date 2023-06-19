try:
    # Código que pode gerar exceções
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    resultado = numero1 / numero2
    print("O resultado da divisão é:", resultado)

except ZeroDivisionError:
    # Tratamento específico para o erro de divisão por zero
    print("Erro: divisão por zero não é permitida!")

except ValueError:
    # Tratamento específico para o erro de entrada inválida
    print("Erro: valor inválido fornecido!")

except Exception as e:
    # Tratamento genérico para outras exceções não tratadas
    print("Ocorreu um erro:", str(e))

finally:
    # Código a ser executado independentemente de ocorrer exceção ou não
    print("Fim do programa")
