def thesaurus_adv(*names_surnames):
    res = {}
    print(res, 'сделали словарь имя')
<<<<<<< HEAD
    for name in names:
        key = name[0].capitalize()
        print(key, 'создаем ключ первая буква')
        name, surname = name.split()
        print(name, surname, 'делим на имя и фамилию')
        res.setdefault(surname[0], {})
        # print(res, 'добавляем в словарь')
        # res[name[0]].setdefault(key, [])
        # res[surname[0]][key].append(name)
    return res



tera = thesaurus_adv("Иван Сергеев")
=======
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        name = name[0].capitalize()
        surname = surname[0].capitalize()
        res.setdefault(surname[0], {})
        res[surname[0]][name[0]] = []
        res[surname[0]][name[0]].append(name_surname)
    return res


tera = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Глеб Ерохин", \
                     "Глеб Ерохин1")
>>>>>>> d2c8af76aef21897acae8c461e1b6f7475d9ab76
print(tera)

# ", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева