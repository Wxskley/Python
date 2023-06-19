# Abrir um arquivo para escrita
arquivo = open(r"ChatGPT\arquivo.txt", "w")

# Escrever dados no arquivo
arquivo.write("Olá, mundo!\n")
arquivo.write("Este é um exemplo de escrita em arquivo. ")

# Fechar o arquivo
arquivo.close()

# Abrir o arquivo para leitura
arquivo = open(r"ChatGPT\arquivo.txt", "r")

# Ler o conteúdo do arquivo
conteudo = arquivo.read()
print(conteudo)

# Fechar o arquivo
arquivo.close()
