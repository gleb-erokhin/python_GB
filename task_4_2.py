import requests


def currency_rates(money):
    try:
        money = money.upper()  # регистр кода валюты будет всегда верхний
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        r = response.text  # выводим строку из которой будем искать курс
        find_money = r.find(money)  # ищем вхождение по совпадению переданного кода валюты
        find_value_start = r.find('<Value>', find_money)  # ищем начало тега указывающего на курс в указанной валюте
        find_value_end = r.find('</Value>', find_money)  # ищем конец тега указывающего на курс в указанной валюте
        sum_money = r[find_value_start + 7:find_value_end]  # делаем срез, показываем курс
        sum_f = sum_money.replace(',', '.')  # заменим запятую на точку
        return float(sum_f)  # преобразуем во флоат
    except ValueError:
        money = None


x = currency_rates('eur')
print(x)