def thesaurus_adv(*names_surnames):
    res = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()  # разделяем имя и фамиляю для определения буквы имени и фамилии
        name = name[0].capitalize()  # буква имени в верхний регистр
        surname = surname[0].capitalize()  # буква фамилии в верхний регистр
        res.setdefault(surname[0], {})  # наполняем словарь по первой буквы фамилии
        res[surname[0]][name[0]] = []  # создаем список внутри словаря
        res[surname[0]][name[0]].append(name_surname)  # добавляем в список данные
    return res


tera = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Глеб Ерохин", \
                     "Глеб Ерохин1")
print(tera)
