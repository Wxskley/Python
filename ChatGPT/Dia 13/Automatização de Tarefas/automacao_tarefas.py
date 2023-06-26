import os

# Exemplo de automação de tarefas usando Python


# Executa um comando do sistema operacional
def executar_comando(comando):
    print(f"Executando o comando: {comando}")
    os.system(comando)


# Exemplo de uso
executar_comando("dir")  # Executa o comando 'dir' no Windows
executar_comando("ls")  # Executa o comando 'ls' no Linux ou macOS
