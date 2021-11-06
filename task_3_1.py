def num_translate(key):
    # запрос get для работы со словарем по ключу,
    # так же указываем параметр если не будет слова в словаречтобы не вызвать ошибку
    return print(word_list.get(key, 'Такого числа нет'))


word_list = {
    'one': 'один',
    'two': 'два',
    'tree': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'night': 'девять',
    'ten': 'десять',
}

num_translate('One')
num_translate('one')
