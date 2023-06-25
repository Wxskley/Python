from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        # Criação do layout GridLayout com duas colunas
        layout = GridLayout(cols=2)

        # Criação dos widgets (rótulos e botões)
        label1 = Label(text="Rótulo 1")
        label2 = Label(text="Rótulo 2")
        label3 = Label(text="Rótulo 3")
        button1 = Button(text="Botão 1")
        button2 = Button(text="Botão 2")
        button3 = Button(text="Botão 3")

        # Adição dos widgets ao layout
        layout.add_widget(label1)
        layout.add_widget(button1)
        layout.add_widget(label2)
        layout.add_widget(button2)
        layout.add_widget(label3)
        layout.add_widget(button3)

        # Retorno do layout como widget raiz do aplicativo
        return layout


if __name__ == "__main__":
    MeuApp().run()
