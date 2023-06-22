from tkinter import *
from tkinter import messagebox

# Definindo as cores utilizadas na interface
co0 = "#f0f3f5"  # Cor preta
co1 = "#feffff"  # Cor branca
co2 = "#3fb5a3"  # Cor verde
co3 = "#38576b"  # Cor valor
co4 = "#403d3d"  # Cor letra

# Criando a janela de login
janela = Tk()
janela.title("")  # Define o título da janela
janela.geometry("310x300")  # Define o tamanho da janela
janela.configure(background=co1)  # Define a cor de fundo da janela

# Criando os frames (áreas) dentro da janela
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief="flat")

# Posicionando os frames na janela
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Criando o rótulo para exibir o texto "LOGIN" na parte superior da janela
l_nome = Label(
    frame_cima,
    text="LOGIN",
    anchor=NE,
    font=("Ivy 25"),
    bg=co1,
    fg=co4,
)
l_nome.place(x=5, y=5)

# Criando uma linha para separar visualmente a parte superior da inferior
l_linha = Label(
    frame_cima,
    text="",
    width=275,
    anchor=NW,
    font=("Ivy 1"),
    bg=co2,
    fg=co4,
)
l_linha.place(x=10, y=45)

# Definindo as credenciais de login
credenciais = ["weskley", "1234"]


# Função para verificar o nome de usuário e senha
def verifica_senha():
    nome = e_nome.get()  # Obtém o nome de usuário informado
    senha = e_pass.get()  # Obtém a senha informada

    # Verifica se as credenciais de login estão corretas
    if nome == "admin" and senha == "admin":
        messagebox.showinfo(
            "Login", "Seja bem-vindo Admin!"
        )  # Exibe uma mensagem de boas-vindas para o administrador
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo(
            "Login", "Seja bem-vindo de volta! " + credenciais[0]
        )  # Exibe uma mensagem de boas-vindas personalizada
        # Limpa os widgets (elementos visuais) do frame_baixo e do frame_cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_cima.winfo_children():
            widget.destroy()
        nova_janela()  # Chama a função para criar a nova janela de boas-vindas ao usuário
    else:
        messagebox.showwarning(
            "Erro", "Verifique o nome e a senha!"
        )  # Exibe uma mensagem de erro se as credenciais estiverem incorretas


# Função para criar a nova janela de boas-vindas ao usuário
def nova_janela():
    l_nome = Label(
        frame_cima,
        text="Usuário: " + credenciais[0],
        anchor=NE,
        font=("Ivy 20"),
        bg=co1,
        fg=co4,
    )
    l_nome.place(x=5, y=5)
    l_linha = Label(
        frame_cima,
        text="",
        width=275,
        anchor=NW,
        font=("Ivy 1"),
        bg=co2,
        fg=co4,
    )
    l_linha.place(x=10, y=45)
    l_nome = Label(
        frame_baixo,
        text="Seja bem-vindo " + credenciais[0],
        anchor=NE,
        font=("Ivy 20"),
        bg=co1,
        fg=co4,
    )
    l_nome.place(x=5, y=105)


# Rótulo e campo de entrada para o nome de usuário
l_nome = Label(
    frame_baixo,
    text="Nome *",
    anchor=NW,
    font=("Ivy 10"),
    bg=co1,
    fg=co4,
)
l_nome.place(x=10, y=20)
e_nome = Entry(
    frame_baixo,
    width=25,
    justify="left",
    font=("", 15),
    highlightthickness=1,
    relief="solid",
)
e_nome.place(x=14, y=50)

# Rótulo e campo de entrada para a senha
l_pass = Label(
    frame_baixo,
    text="Senha *",
    anchor=NW,
    font=("Ivy 10"),
    bg=co1,
    fg=co4,
)
l_pass.place(x=10, y=95)
e_pass = Entry(
    frame_baixo,
    width=25,
    justify="left",
    show="*",
    font=("", 15),
    highlightthickness=1,
    relief="solid",
)
e_pass.place(x=14, y=130)

# Botão para confirmar o login
b_confirmar = Button(
    frame_baixo,
    command=verifica_senha,
    text="Entrar",
    width=39,
    height=2,
    font=("Ivy 8 bold"),
    bg=co2,
    fg=co1,
    relief=RAISED,
    overrelief=RIDGE,
)
b_confirmar.place(x=15, y=180)

janela.mainloop()
