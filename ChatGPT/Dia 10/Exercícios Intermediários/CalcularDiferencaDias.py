# Este algoritmo calcula o número de dias entre duas datas.

from datetime import datetime


def days_between_dates(date1, date2):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(
        date1, date_format
    )  # Convertendo a string em objeto de data
    end_date = datetime.strptime(date2, date_format)
    delta = end_date - start_date  # Calculando a diferença entre as datas
    return delta.days  # Atributo days retorna o número de dias


print(
    days_between_dates("2022-01-01", "2022-12-31")
)  # Exemplo de uso: Calcula o número de dias entre 2022-01-01 e 2022-12-31
