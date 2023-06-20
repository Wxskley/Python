import tkinter as tk


# Função para realizar o cálculo
def calcular():
    # Obtém os valores inseridos nas entradas
    valor1 = float(entry_valor1.get())
    valor2 = float(entry_valor2.get())
    operador = entry_operador.get()

    # Verifica o operador e realiza o cálculo correspondente
    if operador == "+":
        resultado = valor1 + valor2
    elif operador == "-":
        resultado = valor1 - valor2
    elif operador == "*":
        resultado = valor1 * valor2
    elif operador == "/":
        resultado = valor1 / valor2
    else:
        resultado = "Operador inválido"

    # Atualiza o texto do rótulo com o resultado
    label_resultado.config(text=f"Resultado: {resultado}")


# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Entradas para os valores e o operador
entry_valor1 = tk.Entry(janela)
entry_valor1.pack()

entry_operador = tk.Entry(janela)
entry_operador.pack()

entry_valor2 = tk.Entry(janela)
entry_valor2.pack()

# Botão de cálculo
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack()

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela)
label_resultado.pack()

# Execução da janela
janela.mainloop()
