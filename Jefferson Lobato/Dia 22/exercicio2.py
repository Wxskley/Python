dicio = {}
dicio["violão"] = "Instrumento usado para tocar"
dicio[
    "tecnologia"
] = "qualquer ferramenta, dispositivo ou processo que seja criado para resolver problemas ou melhorar a vida das pessoas."
continuar = ""
while True:
    continuar = input("Deseja saber o significado de alguma palavra? (s/n)")
    if continuar.lower() == "n":
        break
    else:
        palavra = input("Digite uma palavra: ")
        if palavra.lower() in dicio:
            print(dicio[palavra.lower()])
        else:
            print(
                f"A palavra {palavra} não existe e nosso banco de dados, tente novamente."
            )
