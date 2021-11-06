import random


def get_jokes():
    joke = []  # создаем пустой словарь
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    # берем случайный элемент из кадого списка
    list_1 = random.choice(nouns)
    list_2 = random.choice(adverbs)
    list_3 = random.choice(adjectives)
    # добавляем в список для вывода
    joke.append(f'{list_1} {list_2} {list_3}')
    return joke


print(get_jokes())
