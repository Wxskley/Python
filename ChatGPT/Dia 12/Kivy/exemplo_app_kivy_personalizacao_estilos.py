from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder


# Definição do estilo personalizado
kv = """
<MyButton>:
    background_normal: 'button_normal.png'
    background_down: 'button_down.png'
    color: (1, 1, 1, 1)
    font_size: 20
"""

# Carrega o estilo personalizado definido no arquivo KV
Builder.load_string(kv)


# Definição da classe para o botão personalizado
class MyButton(Button):
    pass


class MeuApp(App):
    def build(self):
        # Cria um botão personalizado
        botao = MyButton(text="Botão Personalizado")

        # Cria a interface principal do aplicativo com o botão
        interface = botao

        return interface


if __name__ == "__main__":
    MeuApp().run()
