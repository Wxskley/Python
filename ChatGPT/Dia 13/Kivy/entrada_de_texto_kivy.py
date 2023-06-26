from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MeuApp(App):
    def build(self):
        # Criação do BoxLayout vertical
        box_layout = BoxLayout(orientation="vertical")

        # Criação da entrada de texto
        entrada_texto = TextInput(multiline=False)

        # Adiciona a entrada de texto ao BoxLayout
        box_layout.add_widget(entrada_texto)

        # Retorna o layout principal
        return box_layout


# Executa o aplicativo
if __name__ == "__main__":
    MeuApp().run()
