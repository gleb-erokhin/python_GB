from itertools import zip_longest

dic = {}
with open('usershobby.txt', 'w', encoding='utf-8') as file_ext:
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
            """ циклом наполняем файл usershobby.txt связкой имени и хобби """
            for line_users, line_users_hobby in zip_longest(users, users_hobby):
                file_ext.write(f'{line_users.strip()}: '
                               f'{line_users_hobby.strip() if line_users_hobby is not None else line_users_hobby}\n')
