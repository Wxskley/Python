from kivy.app import App
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        # Criação de um rótulo com o texto "Olá, Kivy!"
        return Label(text="Olá, Kivy!")


if __name__ == "__main__":
    # Execução do aplicativo
    MeuApp().run()
