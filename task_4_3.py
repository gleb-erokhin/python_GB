import requests
from datetime import datetime


def currency_rates_d(money):
    try:
        money = money.upper()  # регистр кода валюты будет всегда верхний
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        r = response.text  # выводим строку из которой будем искать курс

        find_money = r.find(money)  # ищем вхождение по совпадению переданного кода валюты
        find_value_start = r.find('<Value>', find_money)  # ищем начало тега указывающего на курс в указанной валюте
        find_value_end = r.find('</Value>', find_money)  # ищем конец тега указывающего на курс в указанной валюте

        sum_money = r[find_value_start + 7:find_value_end]  # делаем срез, показываем курс
        sum_f = sum_money.replace(',', '.')  # заменим запятую на точку

        date_raw_start = r.find('Date="')
        date_raw_fin = r.find('"', date_raw_start + 6)
        date_show = r[date_raw_start + 6:date_raw_fin].split('.')
        day, month, year = map(int, date_show)

        return f'{float(sum_f)}, {datetime(day=day, month=month, year=year)}'  # преобразуем во флоат, выводим дату
    except ValueError:
        money = None


if __name__ == '__main__':
    print(currency_rates_d('usd'))
    print(currency_rates_d('AMD'))
    print(currency_rates_d('gbp'))