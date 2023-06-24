print("\033[1;30;45mOlá, Mundo!\033[m")
a = 3
b = 5
print(f"Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m")
nome = "Weskley"
cores = {
    "Limpa": "\033[m",
    "Azul": "\033[34m",
    "Amarelo": "\033[33m",
    "Pretoebranco": "\033[7;30m",
}
print(
    "Olá! Muito prazer em te conhecer, {}{}{}!!!".format(
        cores["Pretoebranco"], nome, cores["Limpa"]
    )
)