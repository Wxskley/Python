from exercicio3.matematico import soma, par_impar

continuar = ""
while True:
    continuar = input("Deseja jogar par ou ímpar? s/n")
    if continuar.lower() == "n":
        break
    else:
        jogador1 = input("Digite o nome do jogador 1: ")
        jogador2 = input("Digite o nome do jogador 2: ")
        escolha_jogador = input(f"{jogador1} Digite 1 para ímpar e 2 para par: ")
        if escolha_jogador != "1" and escolha_jogador != "2":
            print("Você digitou uma opção inválida.")
            continue
        else:
            num_jog1 = int(input(f"{jogador1} Digite um número qualquer: "))
            num_jog2 = int(input(f"{jogador2} Digite um número qualquer: "))
            resultado = soma(num_jog1, num_jog2)
            resultado_final = par_impar(num_jog1, num_jog2)
            print(
                f"O {jogador1} escolheu {num_jog1} e o {jogador2} escolheu {num_jog2}"
            )
            print(f"E a soma da {resultado} que é {resultado_final}")
            if resultado_final == "par":
                if escolha_jogador == "1":
                    print(f"Parabéns ao {jogador2}, você é o vencedor!")
                else:
                    print(f"Parabéns ao {jogador1}, você é o vencedor!")
            else:
                if escolha_jogador == "1":
                    print(f"Parabéns ao {jogador1}, você é o vencedor!")
                else:
                    print(f"Parabéns ao {jogador2}, você é o vencedor!")
print("Fim da execução")
