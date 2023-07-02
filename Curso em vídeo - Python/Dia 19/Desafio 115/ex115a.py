from cadastro import cadastrar_pessoa, listar_pessoas

while True:
    print("\nOpções:")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        listar_pessoas()
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Digite novamente.")
