from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider


class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        # Criação do Spinner
        spinner = Spinner(
            text="Selecione uma opção", values=("Opção 1", "Opção 2", "Opção 3")
        )
        spinner.bind(text=self.on_spinner_select)
        # Criação do Slider
        slider = Slider(min=0, max=100, value=50)
        slider.bind(value=self.on_slider_change)
        layout.add_widget(spinner)
        layout.add_widget(slider)
        return layout

    def on_spinner_select(self, spinner, text):
        print(f"Opção selecionada: {text}")

    def on_slider_change(self, slider, value):
        print(f"Valor do Slider: {value}")


# Executa o aplicativo
if __name__ == "__main__":
    MeuApp().run()
