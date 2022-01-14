import re

"""
в 9 строке подаем регулярное выражение
в 10 строке используя регулярное выражение обрабатываем переменную в которой подаем почту на вход функции
в строке 12 с помощью цикла if возвращаем значение валидного ящика в словарь
в 18 строке создаем исключение если адрес не валидный
"""

def name_is_valid(email):
    re_email = re.compile(r"^([a-z\d\.-]+)@([a-z\d-]+\.[a-z]{2,8})")
    parts = re_email.findall(email)
    if parts:
        return {
                    'username': parts[0][0],
                    'domain': parts[0][1]
                }
    else:
        raise ValueError(f'wrong email: {parts}')


email = name_is_valid('someone@geekbrains.ru')
# name = name_is_valid('someone@geekbrainsru')
print(email)
