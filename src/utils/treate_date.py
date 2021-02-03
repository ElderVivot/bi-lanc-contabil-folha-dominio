import datetime

def returnAsDate(dateString, formatDate=1):
    """
    :param dateString: Informar o campo string que será transformado para DATA
    :param formatDate: 1 = 'DD/MM/YYYY' ; 2 = 'YYYY-MM-DD' ; 3 = 'YYYY/MM/DD' ; 4 = 'DDMMYYYY'
    :return: retorna como uma data. Caso não seja uma data válida irá retornar None
    """
    if type(dateString) == 'datetime.date':
        return dateString

    dateString = str(dateString).strip()

    lengthField = 10 # tamanho padrão da data são 10 caracteres, só muda se não tiver os separados de dia, mês e ano

    if formatDate == 1:
        formatDateStr = "%d/%m/%Y"
    elif formatDate == 2:
        formatDateStr = "%Y-%m-%d"
    elif formatDate == 3:
        formatDateStr = "%Y/%m/%d"
    elif formatDate == 4:
        formatDateStr = "%d%m%Y"
        lengthField = 8
    elif formatDate == 5:
        formatDateStr = "%d/%m/%Y"
        dateString = dateString[0:6] + '/20' + dateString[6:]

    try:
        return datetime.datetime.strptime(dateString[:lengthField], formatDateStr).date()
    except ValueError:
        return None