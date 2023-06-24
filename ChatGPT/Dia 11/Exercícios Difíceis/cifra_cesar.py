# Algoritmo de Cifra de César
# Este algoritmo cifra e decifra mensagens usando a Cifra de César.


def cifra_cesar(mensagem, chave):
    mensagem_cifrada = ""

    for caractere in mensagem:
        if caractere.isalpha():
            ascii_base = ord("a") if caractere.islower() else ord("A")
            indice = (ord(caractere) - ascii_base + chave) % 26
            novo_caractere = chr(indice + ascii_base)
            mensagem_cifrada += novo_caractere
        else:
            mensagem_cifrada += caractere

    return mensagem_cifrada


# Exemplo de uso:
mensagem_original = "Olá, mundo!"
mensagem_cifrada = cifra_cesar(mensagem_original, 3)
print(mensagem_cifrada)

mensagem_decifrada = cifra_cesar(mensagem_cifrada, -3)
print(mensagem_decifrada)
