# Importando as bibliotecas necessárias para a interface gráfica
from tkinter import *
from tkinter import ttk

# Definindo as cores utilizadas na interface
co0 = "#ffffff"  # Branco
co1 = "#444466"  # Azul escuro
co2 = "#4065a1"  # Azul claro

# Criando a janela da calculadora de IMC
janela = Tk()
janela.title("")  # Define o título da janela
janela.geometry("295x230")  # Define o tamanho da janela
janela.configure(bg=co0)  # Define a cor de fundo da janela

# Criando os frames (áreas) dentro da janela
frame_cima = Frame(janela, width=295, height=50, bg=co0, pady=0, padx=0, relief="flat")
frame_baixo = Frame(
    janela, width=295, height=180, bg=co0, pady=0, padx=0, relief="flat"
)

# Posicionando os frames na janela
frame_cima.grid(row=0, column=0, sticky=NSEW)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Criando o rótulo para o nome da aplicação
app_nome = Label(
    frame_cima,
    text="Calculadora de IMC",
    width=23,
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 16 bold"),
    bg=co0,
    fg=co1,
)
app_nome.place(x=0, y=0)

# Criando uma linha para separar visualmente a parte superior da inferior
app_linha = Label(
    frame_cima,
    text="",
    width=400,
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 1"),
    bg=co2,
    fg=co1,
)
app_linha.place(x=0, y=35)


# Função para calcular o IMC
def calcular():
    # Obtenção do peso e altura informados pelo usuário
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    # Cálculo do IMC
    imc = peso / altura**2

    # Exibição do resultado do IMC e sua classificação
    resultado = imc
    if resultado < 18.5:
        l_resultado_texto["text"] = "Seu IMC é: Abaixo do peso"
    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto["text"] = "Seu IMC é: Normal"
    elif resultado >= 25 and resultado < 30:
        l_resultado_texto["text"] = "Seu IMC é: Sobrepeso"
    else:
        l_resultado_texto["text"] = "Seu IMC é: Obesidade"

    l_resultado["text"] = "{:.{}f}".format(resultado, 2)


# Criação dos elementos da interface: rótulos, campos de entrada e botões
l_peso = Label(
    frame_baixo,
    text="Insira seu peso",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 10 bold"),
    bg=co0,
    fg=co1,
)
e_peso = Entry(
    frame_baixo, width=5, relief="solid", font=("Ivy 10 bold"), justify="center"
)
l_altura = Label(
    frame_baixo,
    text="Insira sua altura",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 10 bold"),
    bg=co0,
    fg=co1,
)
e_altura = Entry(
    frame_baixo, width=5, relief="solid", font=("Ivy 10 bold"), justify="center"
)
l_resultado = Label(
    frame_baixo,
    text="---",
    width=5,
    height=1,
    padx=6,
    pady=12,
    relief="flat",
    anchor="center",
    font=("Ivy 24 bold"),
    bg=co2,
    fg=co0,
)
l_resultado_texto = Label(
    frame_baixo,
    text="",
    width=37,
    height=1,
    padx=0,
    pady=12,
    relief="flat",
    anchor="center",
    font=("Ivy 10 bold"),
    bg=co0,
    fg=co1,
)
b_calcular = Button(
    frame_baixo,
    command=calcular,
    text="Calcular",
    width=34,
    height=1,
    overrelief=SOLID,
    relief="raised",
    anchor="center",
    font=("Ivy 10 bold"),
    bg=co2,
    fg=co0,
)

# Posicionando os elementos na interface
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)
l_resultado.place(x=175, y=10)
l_resultado_texto.place(x=0, y=90)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

# Iniciando a execução da interface
janela.mainloop()
