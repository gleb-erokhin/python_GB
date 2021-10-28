def thesaurus_adv(*names):
    res = {}
    print(res, 'сделали словарь имя')
    for name in names:
        key = name[0].capitalize()
        name, surname = name.split()
        res.setdefault(surname, {})
        res[surname[0]].setdefault(key, [])
        res[surname[0]][key].append(name)
    return res


tera = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(tera)
