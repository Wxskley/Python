from datetime import datetime

# Importa a classe datetime do módulo datetime


def today():
    # Função que retorna a data atual
    today = datetime.now()
    return today


def verify_date(date):
    # Função que verifica se a data fornecida está no formato correto e a converte para o formato datetime
    try:
        date_format = datetime.strptime(date, "%d-%m-%Y")
        return date_format
    except:
        # Caso a data fornecida não esteja no formato correto, uma exceção é lançada
        raise Exception(
            "Entrada inválida! Formato sugerido: D-M-Y. Exemplo: 22-03-2002"
        )


def verify_due(date_ref):
    # Função que verifica se a data de vencimento fornecida é posterior à data atual
    due_date = verify_date(date=date_ref)
    if today() > due_date:
        return "Data expirou..."
    else:
        return "Data não expirou..."
