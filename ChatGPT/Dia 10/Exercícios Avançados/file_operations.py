# Vamos ler um arquivo e escrever em outro arquivo

# Vamos abrir o arquivo de origem para leitura
with open("ChatGPT\Dia 10\Exercícios Avançados\origem.txt", "r") as file:
    # Vamos ler o conteúdo do arquivo de origem
    content = file.read()

# Vamos abrir o arquivo de destino para escrita
with open("ChatGPT\Dia 10\Exercícios Avançados\destino.txt", "w") as file:
    # Vamos escrever o conteúdo no arquivo de destino
    file.write(content)

# Pronto! O conteúdo do arquivo de origem foi copiado para o arquivo de destino
