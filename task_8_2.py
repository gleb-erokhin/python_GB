import re
import requests


def regular(url):
    """обрабатываем полученную ссылку в переменной"""
    data = requests.get(url).text
    """применяем рег. выражение"""
    pattern = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                         r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                         r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
    """проходим циклом по искомым данным из ссылки применяя pattern и назначаем значения 
    в кортеже"""
    for arg in pattern.findall(data):
        addr, datetime, r_type, resource, code, size = arg
        print(addr, datetime, r_type, resource, code, size)


regular('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
