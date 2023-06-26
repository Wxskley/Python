from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation


class MeuApp(App):
    def build(self):
        # Criação do BoxLayout vertical
        box_layout = BoxLayout(orientation="vertical")

        # Criação do botão
        button = Button(text="Clique para animar")
        button.bind(on_release=self.animar_botao)

        # Adiciona o botão ao BoxLayout
        box_layout.add_widget(button)

        # Retorna a raiz da interface gráfica
        return box_layout

    def animar_botao(self, button):
        # Criação da animação
        anim = Animation(opacity=0, duration=1)

        # Inicia a animação no botão
        anim.start(button)


# Instancia e executa o aplicativo
if __name__ == "__main__":
    MeuApp().run()
