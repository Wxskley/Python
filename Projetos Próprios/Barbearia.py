from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class CadastroClientes(Screen):
    def __init__(self, **kwargs):
        super(CadastroClientes, self).__init__(**kwargs)

        # Layout principal
        main_layout = BoxLayout(orientation="vertical", padding=50)

        # Layout do título
        titulo_layout = AnchorLayout(anchor_x="center", anchor_y="top")
        titulo = Label(text="Cadastro de Clientes", font_size=18)
        titulo_layout.add_widget(titulo)
        main_layout.add_widget(titulo_layout)

        # Campos de cadastro
        campos_layout = BoxLayout(orientation="vertical", spacing=10)

        # Campo Nome completo
        campo_nome = TextInput(
            multiline=False, hint_text="Digite o nome completo", input_type="text"
        )
        campos_layout.add_widget(campo_nome)

        # Campo Ano de nascimento
        campo_nascimento = TextInput(
            multiline=False, hint_text="Digite o ano de nascimento", input_type="number"
        )
        campos_layout.add_widget(campo_nascimento)

        # Campo Número de telefone
        campo_telefone = TextInput(
            multiline=False,
            hint_text="Digite o número de telefone",
            input_type="number",
        )
        campos_layout.add_widget(campo_telefone)

        # Campo Observações
        campo_observacoes = TextInput(multiline=True, hint_text="Digite as observações")
        campos_layout.add_widget(campo_observacoes)

        # Espaçamento
        campos_layout.add_widget(Label())

        main_layout.add_widget(campos_layout)

        # Botão de voltar
        btn_voltar = Button(
            text="Voltar", size_hint=(1, None), height=50, padding=(10, 5, 10, 5)
        )
        btn_voltar.bind(on_release=self.voltar_para_tela_inicial)
        main_layout.add_widget(btn_voltar)

        self.add_widget(main_layout)

    def voltar_para_tela_inicial(self, instance):
        self.manager.current = "tela_inicial"


class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super(TelaInicial, self).__init__(**kwargs)

        # Layout principal
        main_layout = BoxLayout(orientation="vertical", padding=50)

        # Layout do título
        titulo_layout = AnchorLayout(anchor_x="center", anchor_y="top")
        titulo = Label(text="Bem-vindo à Barbearia!", font_size=18)
        titulo_layout.add_widget(titulo)
        main_layout.add_widget(titulo_layout)

        # Botão de cadastro de clientes
        btn_cadastro = Button(
            text="Cadastro de Clientes",
            size_hint=(1, None),
            height=50,
            padding=(10, 5, 10, 5),
        )
        btn_cadastro.bind(on_release=self.ir_para_tela_cadastro)
        main_layout.add_widget(btn_cadastro)

        # Botão de sair
        btn_sair = Button(
            text="Sair", size_hint=(1, None), height=50, padding=(10, 5, 10, 5)
        )
        btn_sair.bind(on_release=self.fechar_aplicativo)
        main_layout.add_widget(btn_sair)

        self.add_widget(main_layout)

    def ir_para_tela_cadastro(self, instance):
        self.manager.current = "tela_cadastro"

    def fechar_aplicativo(self, instance):
        App.get_running_app().stop()


class BarbeariaApp(App):
    def build(self):
        # Gerenciador de telas
        screen_manager = ScreenManager()

        # Adiciona as telas ao gerenciador de telas
        screen_manager.add_widget(TelaInicial(name="tela_inicial"))
        screen_manager.add_widget(CadastroClientes(name="tela_cadastro"))

        Window.size = (400, 800)
        Window.minimum_height = Window.height  # Define a altura mínima da janela

        return screen_manager


if __name__ == "__main__":
    BarbeariaApp().run()
