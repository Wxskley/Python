import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
)


# Definição da classe do aplicativo
class ListaTarefasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tarefas")

        # Criação do layout principal
        self.layout = QVBoxLayout()

        # Criação da caixa de entrada de tarefas
        self.input_tarefa = QLineEdit()
        self.layout.addWidget(self.input_tarefa)

        # Criação do botão "Adicionar" e conexão com o método adicionar_tarefa
        self.btn_adicionar = QPushButton("Adicionar")
        self.btn_adicionar.clicked.connect(self.adicionar_tarefa)
        self.layout.addWidget(self.btn_adicionar)

        # Criação da lista de tarefas
        self.lista_tarefas = QListWidget()
        self.layout.addWidget(self.lista_tarefas)

        # Definição do layout principal para o aplicativo
        self.setLayout(self.layout)

    # Método para adicionar uma nova tarefa à lista
    def adicionar_tarefa(self):
        tarefa = self.input_tarefa.text()
        self.lista_tarefas.addItem(tarefa)
        self.input_tarefa.clear()


# Criação da aplicação
app = QApplication(sys.argv)

# Criação e exibição do aplicativo
lista_tarefas_app = ListaTarefasApp()
lista_tarefas_app.show()

# Execução da aplicação
sys.exit(app.exec_())
