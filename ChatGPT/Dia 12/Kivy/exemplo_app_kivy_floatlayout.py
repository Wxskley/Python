from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class MeuApp(App):
    def build(self):
        # Criação do layout FloatLayout
        layout = FloatLayout()

        # Criação do botão
        botao = Button(
            text="Clique-me!",
            size_hint=(0.2, 0.2),  # Define o tamanho relativo do botão
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )  # Define a posição relativa do botão

        # Adição do botão ao layout
        layout.add_widget(botao)

        # Retorno do layout como widget raiz do aplicativo
        return layout


if __name__ == "__main__":
    MeuApp().run()
