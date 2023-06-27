cidade = input("Digite o nome da cidade: ")

# Verifica se o nome da cidade contém a palavra "Santo" no início
if cidade[:5].lower() == "santo":
    print("A cidade começa com o nome 'Santo'.")
else:
    print("A cidade não começa com o nome 'Santo'.")
