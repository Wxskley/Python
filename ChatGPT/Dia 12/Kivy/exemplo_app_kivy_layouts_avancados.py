from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class MeuApp(App):
    def build(self):
        # Criação do BoxLayout vertical
        box_layout = BoxLayout(orientation="vertical")

        # Criação dos botões usando o BoxLayout
        button1 = Button(text="Botão 1")
        button2 = Button(text="Botão 2")
        button3 = Button(text="Botão 3")

        # Adiciona os botões ao BoxLayout
        box_layout.add_widget(button1)
        box_layout.add_widget(button2)
        box_layout.add_widget(button3)

        # Criação do GridLayout
        grid_layout = GridLayout(cols=2)

        # Criação dos botões usando o GridLayout
        for i in range(1, 7):
            button = Button(text=f"Botão {i}")
            grid_layout.add_widget(button)

        # Criação do BoxLayout principal para envolver os layouts
        main_layout = BoxLayout(orientation="vertical")

        # Adiciona os layouts ao BoxLayout principal
        main_layout.add_widget(box_layout)
        main_layout.add_widget(grid_layout)

        # Retorna o BoxLayout principal como raiz da interface gráfica
        return main_layout


# Executa o aplicativo
if __name__ == "__main__":
    MeuApp().run()
