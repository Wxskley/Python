from kivy.app import App
from kivy.uix.button import Button


class MeuApp(App):
    def build(self):
        # Criação do botão
        botao = Button(text="Clique-me!")

        # Definição da função de tratamento do evento
        def on_button_press(instance):
            print("Botão pressionado!")

        # Vinculação da função ao evento de pressionar o botão
        botao.bind(on_press=on_button_press)

        # Retorno do botão como widget raiz do aplicativo
        return botao


if __name__ == "__main__":
    MeuApp().run()
