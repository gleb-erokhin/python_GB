def thesaurus_adv(*names):
    res = {}
    print(res, 'сделали словарь имя')
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
print(tera)

# ", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева