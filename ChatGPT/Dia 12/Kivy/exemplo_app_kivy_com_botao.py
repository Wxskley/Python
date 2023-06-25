from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.label = Label(text="Olá, Kivy!")
        button = Button(text="Clique aqui", on_press=self.alterar_texto)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def alterar_texto(self, instance):
        if self.label.text == "Olá, Kivy!":
            self.label.text = "Texto alterado!"
        else:
            self.label.text = "Olá, Kivy!"


if __name__ == "__main__":
    MeuApp().run()
