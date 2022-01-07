import  json
from itertools import zip_longest

dic = {}
with open('users.csv', encoding='utf-8') as file_users:
    with open('hobby.csv', encoding='utf-8') as file_hobby:

        """ прочитываем файл, получаем строку и сразу делим ее по знаку переноса строки """
        users = file_users.read().split('\n')
        users_hobby = file_hobby.read().split('\n')

        """ если добавить еще один элемент списка то программа на уровне проверки завершится """
        # users_hobby.append('Сергей Сергеевич Сергеев')
        # print(users, len(users))
        # print(users_hobby, len(users_hobby))

        """ сравниваем длинну списков, если не равны, то выходим из программы """
        if len(users) != len(users_hobby):
            print('Списки не равны')
            exit(1)

        """ наполняем словарь связкой имени и хобби """
        for line_users, line_users_hobby in zip_longest(users, users_hobby):
            dic[line_users.strip()] = line_users_hobby.strip()

""" сохраняем словарь в файл json """
with open('task_6_3.json', 'w', encoding='utf-8') as f_dic:
    json.dump(dic, f_dic, ensure_ascii=False)
print(dic)