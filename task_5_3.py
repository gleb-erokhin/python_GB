from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
gen = ((t, k) for t, k in zip(tutors, klasses))
# создание картежа из элементов двух списков
# для каждого элемента списка генерируем картеж из списков в значениях аргументов

# циклом фор пробегаемся по каждому картежу в генераторе
for i in gen:
    print(i)
# докажем что gen это генератор
print(type(gen))

# //////////////////
# если списки разной длинны используем zip_longest
gen_long = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
for i in gen_long:
    print(i)

