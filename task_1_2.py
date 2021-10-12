my_list = list(range(1, 1001, 2))  # создаем последовательность от 1 до 1000
my_list2 = [i ** 3 for i in my_list] # создадим кубы из элементов списков

final_sum = 0
for i in my_list2:      # перебираем последовательность списка
    my_str = str(i)     # каждый элемент списка переводим в строку
    my_lst = list(my_str)    # каждый элемент строки переводим в список
    full_sum = [int(item) for item in my_lst]  # создаем сумму всех чисел в выводе каждого элемента куба
    if sum(full_sum) % 7 == 0:     # проверяем делится ли сумма на 7 нацело
        final_sum += i
print(final_sum)


# попробованные варианты ранее
# print(len(my_list2))
# print(check_list.append(3333))
# print(type(check_list))
# print(check_list.pop())
# print(check_list)

# for i in my_list2:
#     my_str = str(i)
#     print(my_str)

# for i in my_list2:
#     my_list3.append(i)
# print(my_list3)



