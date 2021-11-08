import task_4_3
import sys


money = sys.argv[1]  # передаем в параметр для типа валюты для ввода в командной строке
if isinstance(money, str):
    print(task_4_3.currency_rates_d(money))  # обращение к функции через модуль task_4_3.py
else:
    print('Ошибка ввода')
