import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load(r"Curso em vídeo - Python\ex021\barulhoMiranhaEx021.mp3")


# Reproduz o áudio
pygame.mixer.music.play()

# Aguarda até que a reprodução termine
while pygame.mixer.music.get_busy():
    pass
