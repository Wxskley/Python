from PySimpleGUI import PySimpleGUI as sg

sg.theme("Reddit")  # Define o tema visual da janela como "Reddit"

layout = [
    [
        sg.Text("Usuário"),
        sg.Input(key="usuario", size=(20, 1)),
    ],  # Campo de entrada para o nome de usuário
    [
        sg.Text("Senha"),
        sg.Input(key="senha", password_char="*", size=(20, 1)),
    ],  # Campo de entrada para a senha
    [sg.Checkbox("Salvar o Login?")],  # Checkbox para opção de salvar o login
    [sg.Button("Entrar")],  # Botão para fazer login
]

janela = sg.Window(
    "Tela de login", layout
)  # Cria uma janela com o título "Tela de login" e o layout definido anteriormente

while True:
    (
        eventos,
        valores,
    ) = (
        janela.read()
    )  # Aguarda por eventos na janela e obtém os valores dos elementos do layout

    if eventos == sg.WINDOW_CLOSED:  # Verifica se a janela foi fechada
        break

    if eventos == "Entrar":  # Verifica se o botão "Entrar" foi clicado
        if (
            valores["usuario"] == "Weskley" and valores["senha"] == "123"
        ):  # Verifica se o nome de usuário e senha informados estão corretos
            print("Seja muito bem-vindo!")  # Exibe uma mensagem de boas-vindas
