# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer


# class MeuApp(App):
#     def build(self):
#         # Criação do BoxLayout vertical
#         box_layout = BoxLayout(orientation="vertical")

#         # Criação do chatbot
#         chatbot = ChatBot("Meu ChatBot")

#         # Treinamento do chatbot usando o corpus pré-existente
#         trainer = ChatterBotCorpusTrainer(chatbot)
#         trainer.train("chatterbot.corpus.portuguese")

#         # Função para enviar a mensagem e obter a resposta do chatbot
#         def enviar_mensagem(instance):
#             mensagem = input_text.text
#             resposta = chatbot.get_response(mensagem)
#             output_label.text = str(resposta)

#         # Criação dos elementos da interface
#         input_text = TextInput(multiline=False)
#         enviar_button = Button(text="Enviar")
#         output_label = Label(text="")

#         # Definição da função de callback do botão
#         enviar_button.bind(on_release=enviar_mensagem)

#         # Adição dos elementos ao BoxLayout
#         box_layout.add_widget(input_text)
#         box_layout.add_widget(enviar_button)
#         box_layout.add_widget(output_label)

#         return box_layout


# # Executa o aplicativo
# if __name__ == "__main__":
#     MeuApp().run()
