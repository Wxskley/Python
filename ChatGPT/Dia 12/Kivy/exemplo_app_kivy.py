from kivy.app import App
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        return Label(text="Olá, Kivy!")


if __name__ == "__main__":
    MeuApp().run()
