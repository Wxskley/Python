from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MeuApp(App):
    def build(self):
        # Criação de um layout GridLayout com duas colunas e espaçamento de 10 pixels
        layout = GridLayout(cols=2, spacing=10)

        # Loop para criar cinco botões numerados
        for i in range(1, 6):
            # Criação de um botão com texto dinâmico e plano de fundo azul
            button = Button(text=f"Botão {i}", background_color=(0, 0, 1, 1))

            # Adição do botão ao layout
            layout.add_widget(button)

        # Retorno do layout como widget raiz do aplicativo
        return layout


if __name__ == "__main__":
    # Execução do aplicativo
    MeuApp().run()
