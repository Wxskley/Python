from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class MeuApp(App):
    def build(self):
        # Cria um botão que exibirá o pop-up
        botao = Button(text="Exibir Pop-up")
        botao.bind(on_press=self.exibir_popup)

        # Cria a interface principal do aplicativo com o botão
        interface = botao

        return interface

    def exibir_popup(self, instance):
        # Cria um pop-up
        popup = Popup(
            title="Pop-up de Exemplo",
            size_hint=(None, None),
            size=(300, 200),
            auto_dismiss=True,
        )

        # Cria o conteúdo do pop-up
        conteudo = Label(text="Este é um pop-up de exemplo!")

        # Adiciona o conteúdo ao pop-up
        popup.content = conteudo

        # Abre o pop-up
        popup.open()


if __name__ == "__main__":
    MeuApp().run()
