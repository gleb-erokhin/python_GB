def gen_odd(n):                # создаем функцию
    for i in range(1, n+1):    # создаем генератор
        if i % 2 != 0:         # создаем условие только нечетные числа
            yield i            # останавливаем вывод генератора


# пробегаем по каждому значению i в генераторе
# в диапазоне до 15, выводим принтом значение i
for i in gen_odd(15):
    print(i)







