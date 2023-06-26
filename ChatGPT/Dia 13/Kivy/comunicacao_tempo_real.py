from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.list import OneLineListItem
from kivy.clock import Clock
import requests
import json
import threading


class ExemploApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.websocket_thread = None

    def build(self):
        # Configuração da interface gráfica da aplicação
        self.layout = BoxLayout(orientation="vertical")
        self.title_label = Label(
            text="Exemplo de Comunicação em Tempo Real",
            font_size=20,
            size_hint=(1, 0.1),
        )
        self.layout.add_widget(self.title_label)

        self.status_label = Label(
            text="Status: Desconectado", font_size=16, size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.status_label)

        self.data_label = Label(
            text="Últimos dados recebidos:", font_size=16, size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.data_label)

        self.data_list = MDTextField(
            hint_text="Nenhum dado recebido", size_hint=(1, 0.5)
        )
        self.layout.add_widget(self.data_list)

        self.connect_button = MDFlatButton(
            text="Conectar", on_release=self.connect_to_websocket, size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.connect_button)

        return self.layout

    def connect_to_websocket(self, instance):
        if self.websocket_thread is None or not self.websocket_thread.is_alive():
            # Inicia a thread para lidar com a comunicação em tempo real
            self.websocket_thread = threading.Thread(target=self.websocket_handler)
            self.websocket_thread.start()
            self.status_label.text = "Status: Conectado"
            self.connect_button.text = "Desconectar"
        else:
            # Para a thread e atualiza o status e o texto do botão
            self.websocket_thread.join()
            self.websocket_thread = None
            self.status_label.text = "Status: Desconectado"
            self.connect_button.text = "Conectar"

    def websocket_handler(self):
        # Código para conectar ao servidor WebSocket e receber dados em tempo real
        # Aqui você pode usar uma biblioteca ou implementação específica para WebSocket, como o asyncio

        while True:
            if self.websocket_thread is None or not self.websocket_thread.is_alive():
                # Verifica se a thread deve ser parada
                break

            # Aqui você pode obter os dados do servidor WebSocket e atualizar a interface gráfica
            # Vamos simular os dados recebidos com um valor aleatório
            data = {"timestamp": "2023-06-28 10:30:00", "value": 42}

            # Atualiza a interface gráfica na thread principal usando o método schedule_once()
            Clock.schedule_once(lambda dt: self.update_data(data), 0)

            # Aguarda 2 segundos antes de receber o próximo dado
            threading.Event().wait(2)

    def update_data(self, data):
        # Atualiza o campo de texto com os últimos dados recebidos
        self.data_list.text += f'\n{data["timestamp"]}: {data["value"]}'


if __name__ == "__main__":
    ExemploApp().run()
