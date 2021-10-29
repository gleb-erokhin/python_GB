def thesaurus_adv(*names_surnames):
    res = {}
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
print(tera)
