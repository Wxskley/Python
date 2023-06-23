# Este algoritmo verifica se duas palavras ou frases são anagramas.
# Dois anagramas possuem as mesmas letras, mas em ordem diferente.


def is_anagram(s1, s2):
    s1 = s1.lower().replace(
        " ", ""
    )  # Convertemos as strings para minúsculas e removemos os espaços em branco
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)  # Comparamos as strings ordenadas


print(
    is_anagram("listen", "silent")
)  # Exemplo de uso: Verifica se as palavras "listen" e "silent" são anagramas
