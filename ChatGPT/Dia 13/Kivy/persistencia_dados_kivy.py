from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore


class MeuApp(App):
    def build(self):
        # Criação do BoxLayout vertical
        box_layout = BoxLayout(orientation="vertical")

        # Criação do botão de salvar
        button_salvar = Button(text="Salvar")
        button_salvar.bind(on_release=self.salvar_dados)

        # Criação do botão de carregar
        button_carregar = Button(text="Carregar")
        button_carregar.bind(on_release=self.carregar_dados)

        # Adiciona os botões ao BoxLayout
        box_layout.add_widget(button_salvar)
        box_layout.add_widget(button_carregar)

        # Retorna a raiz da interface gráfica
        return box_layout

    def salvar_dados(self, button):
        # Criação do objeto de armazenamento JSON
        store = JsonStore("ChatGPT\Dia 13\Kivy\dados.json")

        # Salva os dados no objeto de armazenamento
        store.put("chave", valor="valor")

        # Exibe mensagem de sucesso
        print("Dados salvos com sucesso!")

    def carregar_dados(self, button):
        # Criação do objeto de armazenamento JSON
        store = JsonStore("ChatGPT\Dia 13\Kivy\dados.json")

        # Verifica se a chave existe no objeto de armazenamento
        if "chave" in store:
            # Obtém o valor associado à chave
            valor = store.get("chave")["valor"]

            # Exibe o valor na saída
            print(f"Valor carregado: {valor}")
        else:
            print("Chave não encontrada no armazenamento.")


# Instancia e executa o aplicativo
if __name__ == "__main__":
    MeuApp().run()
