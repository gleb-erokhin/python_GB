# my_list = list(range(1, 50, 2))  # создаем последовательность от 1 до 1000
# print(my_list)
# my_list2 = [i**3 for i in my_list]
# print(my_list2)

num = int(input("Введите целое: "))
sum = 0
while num != 0:
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)

