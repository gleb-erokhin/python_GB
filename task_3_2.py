def num_translate_adv(key):
    # создаем переменную для сброса регистра в нижний
    # чтобы проверить есть ли число в словаре
    word = word_list.get(key.lower(), 'Такого числа нет')
    # циклом проверяем по индексу первая буква слова большая или маленькая
    # затем возвращаем нужный результат
    if key[0].isupper():
        return word.capitalize()
    else:
        return word


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

a = num_translate_adv('Six')
print(a)
