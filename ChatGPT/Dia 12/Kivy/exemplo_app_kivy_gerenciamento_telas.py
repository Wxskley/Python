from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


# Definição da classe da tela inicial
class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super(TelaInicial, self).__init__(**kwargs)
        botao = Button(text="Ir para a próxima tela")
        botao.bind(on_press=self.ir_para_tela_secundaria)
        self.add_widget(botao)

    def ir_para_tela_secundaria(self, instance):
        self.manager.current = "tela_secundaria"


# Definição da classe da tela secundária
class TelaSecundaria(Screen):
    def __init__(self, **kwargs):
        super(TelaSecundaria, self).__init__(**kwargs)
        botao = Button(text="Voltar para a tela inicial")
        botao.bind(on_press=self.ir_para_tela_inicial)
        self.add_widget(botao)

    def ir_para_tela_inicial(self, instance):
        self.manager.current = "tela_inicial"


# Definição da classe do aplicativo
class MeuApp(App):
    def build(self):
        # Criação do gerenciador de telas
        gerenciador_telas = ScreenManager()

        # Adição das telas ao gerenciador de telas
        gerenciador_telas.add_widget(TelaInicial(name="tela_inicial"))
        gerenciador_telas.add_widget(TelaSecundaria(name="tela_secundaria"))

        # Retorno do gerenciador de telas como o widget raiz do aplicativo
        return gerenciador_telas


# Execução do aplicativo
if __name__ == "__main__":
    MeuApp().run()
