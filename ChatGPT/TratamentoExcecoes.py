try:
    # Tentativa de executar um bloco de código que pode gerar exceções

    resultado = 10 / 0
    # Tenta realizar uma operação de divisão por zero, que irá gerar a exceção ZeroDivisionError

except ZeroDivisionError:
    # Bloco de código a ser executado caso ocorra a exceção ZeroDivisionError

    print("Erro: Divisão por zero!")
    # Exibe a mensagem de erro informando que houve uma divisão por zero
