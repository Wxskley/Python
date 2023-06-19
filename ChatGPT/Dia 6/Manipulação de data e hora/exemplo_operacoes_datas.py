from datetime import datetime, timedelta

# Importação dos módulos datetime e timedelta para trabalhar com datas e tempos

data_atual = datetime.now()
# Obtenção da data e hora atual utilizando o método now() da classe datetime

data_futura = data_atual + timedelta(days=7)
# Adição de um intervalo de tempo de 7 dias à data atual utilizando o objeto timedelta

print(data_futura)
# Impressão da data e hora futura resultante
