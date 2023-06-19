try:
    # Tentativa de executar um bloco de código que pode gerar exceções

    arquivo = open(r"ChatGPT\arquivo.txt", "r")
    # Abre o arquivo "dados.txt" em modo de leitura ("r") e o associa à variável "arquivo"

    conteudo = arquivo.read()
    # Lê o conteúdo do arquivo e armazena na variável "conteudo"

    print(conteudo)
    # Exibe o conteúdo do arquivo na saída padrão

finally:
    # Bloco de código que sempre será executado, independentemente se ocorreram exceções ou não

    arquivo.close()
    # Fecha o arquivo, garantindo que ele seja liberado corretamente
