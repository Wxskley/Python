from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        # Criação do layout principal, um BoxLayout vertical
        layout_principal = BoxLayout(orientation="vertical")

        # Criação do layout secundário, um BoxLayout horizontal
        layout_secundario = BoxLayout(orientation="horizontal")

        # Criação dos rótulos
        label1 = Label(text="Rótulo 1")
        label2 = Label(text="Rótulo 2")
        label3 = Label(text="Rótulo 3")

        # Adição dos rótulos ao layout secundário
        layout_secundario.add_widget(label1)
        layout_secundario.add_widget(label2)

        # Adição do layout secundário ao layout principal
        layout_principal.add_widget(layout_secundario)
        layout_principal.add_widget(label3)

        # Retorno do layout principal como widget raiz do aplicativo
        return layout_principal


if __name__ == "__main__":
    MeuApp().run()
