from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder

# Definição do estilo personalizado para o botão
Builder.load_string(
    """
<ButtonStyle@Button>:
    background_color: 0.2, 0.6, 1, 1
    color: 1, 1, 1, 1
    font_size: 20
"""
)


class MeuApp(App):
    def build(self):
        # Criação de um botão usando o estilo personalizado
        botao = Button(
            text="Botão Personalizado",
            size_hint=(None, None),
            size=(200, 100),
            style_button="ButtonStyle",
        )

        return botao


# Executa o aplicativo
if __name__ == "__main__":
    MeuApp().run()
