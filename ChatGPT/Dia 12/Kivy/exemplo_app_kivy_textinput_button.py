from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MeuApp(App):
    def build(self):
        # Criação do layout principal, um BoxLayout vertical
        layout_principal = BoxLayout(orientation="vertical")

        # Criação do TextInput
        self.input_texto = TextInput(multiline=False)

        # Criação do botão
        botao = Button(text="Clique aqui", on_press=self.exibir_texto)

        # Adição do TextInput e do botão ao layout principal
        layout_principal.add_widget(self.input_texto)
        layout_principal.add_widget(botao)

        # Retorno do layout principal como widget raiz do aplicativo
        return layout_principal

    def exibir_texto(self, instance):
        # Obtém o texto inserido no TextInput e exibe-o no console
        texto = self.input_texto.text
        print(texto)


if __name__ == "__main__":
    MeuApp().run()
