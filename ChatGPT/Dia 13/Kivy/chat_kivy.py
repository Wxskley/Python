from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import threading


class ChatApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.websocket_thread = None

    def build(self):
        # Configuração da interface gráfica do chat
        self.layout = BoxLayout(orientation="vertical")
        self.title_label = Label(
            text="Chat em Tempo Real", font_size=20, size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.title_label)

        self.chat_history = TextInput(multiline=True, readonly=True)
        self.layout.add_widget(self.chat_history)

        self.input_text = TextInput(multiline=False, size_hint=(1, 0.1))
        self.layout.add_widget(self.input_text)

        self.send_button = Button(
            text="Enviar", on_release=self.send_message, size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.send_button)

        return self.layout

    def send_message(self, instance):
        message = self.input_text.text
        if message:
            # Envia a mensagem para o servidor WebSocket
            # Aqui você pode implementar a lógica para enviar a mensagem
            self.chat_history.text += f"Você: {message}\n"
            self.input_text.text = ""

    def websocket_handler(self):
        # Código para conectar ao servidor WebSocket e receber mensagens em tempo real
        # Aqui você pode usar uma biblioteca ou implementação específica para WebSocket, como o asyncio

        while True:
            if self.websocket_thread is None or not self.websocket_thread.is_alive():
                # Verifica se a thread deve ser parada
                break

            # Aqui você pode receber as mensagens do servidor WebSocket
            # Vamos simular as mensagens recebidas com valores aleatórios
            messages = ["Olá!", "Tudo bem?", "Como posso ajudar?"]

            # Atualiza a interface gráfica na thread principal usando o método schedule_once()
            Clock.schedule_once(lambda dt: self.update_chat(messages), 0)

            # Aguarda 2 segundos antes de receber as próximas mensagens
            threading.Event().wait(2)

    def update_chat(self, messages):
        # Atualiza o histórico de chat com as mensagens recebidas
        for message in messages:
            self.chat_history.text += f"Servidor: {message}\n"


if __name__ == "__main__":
    ChatApp().run()
