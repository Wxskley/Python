from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MeuApp(App):
    def build(self):
        # Criação do layout BoxLayout vertical
        layout = BoxLayout(orientation="vertical")

        # Criação dos widgets (botões)
        botao1 = Button(text="Botão 1")
        botao2 = Button(text="Botão 2")
        botao3 = Button(text="Botão 3")

        # Adição dos botões ao layout
        layout.add_widget(botao1)
        layout.add_widget(botao2)
        layout.add_widget(botao3)

        # Retorno do layout como widget raiz do aplicativo
        return layout


if __name__ == "__main__":
    MeuApp().run()
