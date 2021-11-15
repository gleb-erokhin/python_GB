import sys
from time import perf_counter

# работа с циклом фор
# print('Цикл for')
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()  # старт времени работы кода
result = []  # создаем пустой словарь

for i in src:   # пробегаем циком по элементам списка
    if src.count(i) == 1:   # проверям вхождения элемената по индексу и сравниваем что он 1 есть
        result.append(i)  # наполняем список
print(result)  # выводим результат

print(sys.getsizeof(result), 'количество использованной памяти')
end = perf_counter()  # окончание работы кода
print(end - start, 'время работы при использовании цикла фор')
print()

print('List comprehension')
# решение с оптимизацией по скорости
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()

result_g = [i for i in src if src.count(i) == 1]  # создаем List comprehension для прохода по списку
print(result_g)  # выводим результат

print(sys.getsizeof(result_g), 'количество использованной памяти')
end = perf_counter()
print(end - start, 'время работы при использовании генератора')

