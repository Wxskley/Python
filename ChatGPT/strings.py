# Exemplo de código para manipular strings em Python
mensagem = "Olá, mundo!"

comprimento = len(mensagem)
primeiro_caractere = mensagem[0]
outra_mensagem = " Como você está?"
mensagem_completa = mensagem + outra_mensagem
esta_presente = "mundo" in mensagem
palavras = mensagem.split(", ")

print(comprimento)
print(primeiro_caractere)
print(mensagem_completa)
print(esta_presente)
print(palavras)
