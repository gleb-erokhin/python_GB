import os

# тут указан Windows слешь, в Linux по другому, можно заменить raw строкой
path = 'C:\\GeekBrains'
project_name = 'my_project'
folders = \
    ['settings',
     'mainapp',
     'adminapp',
     'authapp']


# проверку существования папки убираем в функцию
def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


# соединяем пути в полный путь для создания папки
fullPath = os.path.join(path, project_name)
create_folder(fullPath)


# создаем вложенные папки
for f in folders:
    folder = os.path.join(fullPath, f)
    create_folder(folder)
