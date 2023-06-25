from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        # Criação do layout principal
        layout = BoxLayout(orientation="vertical")

        # Criação do botão personalizado
        botao_personalizado = Button(
            text="Clique-me!",
            background_color=(0.2, 0.7, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size=20,
        )

        # Criação do rótulo personalizado
        rotulo_personalizado = Label(
            text="Sou um rótulo personalizado!",
            font_size=24,
            color=(0.9, 0.1, 0.3, 1),
            size_hint=(None, None),
            size=(300, 100),
            pos=(100, 200),
        )

        # Adição dos widgets ao layout principal
        layout.add_widget(botao_personalizado)
        layout.add_widget(rotulo_personalizado)

        # Retorno do layout como widget raiz do aplicativo
        return layout


if __name__ == "__main__":
    MeuApp().run()
