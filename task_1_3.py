percent = int(input('Введите значение %: '))
if 5 <= percent % 100 <= 20:
    print(percent, 'процентов')
elif 2 <= percent % 10 <= 4:
    print(percent, 'процента')
elif percent % 10 == 1:
    print(percent, 'процент')
else:
    print(percent, 'процентов')

# ///////////////////////////////////

# percent = 0
# while percent < 100:             # с использованием цикла, прописывает все цифры от 1 до 100
#     percent = percent + 1
#     if 5 <= percent % 100 <= 20:
#         print(percent, 'процентов')
#     elif 2 <= percent % 10 <= 4:
#         print(percent, 'процента')
#     elif percent % 10 == 1:
#         print(percent, 'процент')
#     else:
#         print(percent, 'процентов')
