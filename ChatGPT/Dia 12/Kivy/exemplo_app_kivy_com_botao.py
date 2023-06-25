from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MeuApp(App):
    def build(self):
        # Criação de um layout BoxLayout com orientação vertical
        layout = BoxLayout(orientation="vertical")

        # Criação de um rótulo com o texto "Olá, Kivy!"
        self.label = Label(text="Olá, Kivy!")

        # Criação de um botão com o texto "Clique aqui" e vinculação ao método alterar_texto()
        button = Button(text="Clique aqui", on_press=self.alterar_texto)

        # Adição do rótulo e do botão ao layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        # Retorno do layout como widget raiz do aplicativo
        return layout

    def alterar_texto(self, instance):
        # Verificação do texto atual do rótulo e alteração do texto
        if self.label.text == "Olá, Kivy!":
            self.label.text = "Texto alterado!"
        else:
            self.label.text = "Olá, Kivy!"


if __name__ == "__main__":
    # Execução do aplicativo
    MeuApp().run()
