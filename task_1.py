# Task 1
duration = int(input('Введите время в секундах: '))
days = duration // 86400  # один день, 24 часа * 60 минут в часе * 60 чек в 1 минуте
# тут я пробовал сделать это с помощью цикла, но все равно не пойму смысл именно
# каким образом вообще отделять часы минуты, на основании какого принципе это делатся
# почему что то делать через % а что то через //. целочисленные и с остатком в чем разница.
if duration < 60:              # если указанны маленькие секунды до 60, не включительно
    print(duration, 'сек')     # выводим секунды
elif 3600 < duration >= 60:    # диапазон секунд от 60 до 3600
    minute = ((duration % 86400) % 3600) // 60
    seconds = (((duration % 86400) % 3600) % 60) % 60
    print(minute, 'мин.', seconds, 'сек.')
elif 86400 < duration >= 3600:
    hours = (duration % 86400) // 3600
    minute = ((duration % 86400) % 3600) // 60
    seconds = (((duration % 86400) % 3600) % 60) % 60
    print(hours, 'час.', minute, 'мин.', seconds, 'сек.')
elif duration > 86400:
    hours = (duration % 86400) // 3600
    minute = ((duration % 86400) % 3600) // 60
    seconds = (((duration % 86400) % 3600) % 60) % 60
    print(days, 'дни', hours, 'час.', minute, 'мин.', seconds, 'сек.')


# days = duration // 24 * 60 * 60
# print(days)
# hour = (duration - days) /
# print(hour)

# print(days)
#
# # делим duration на 86400 значение чтобы вычесть сутки, после чего делим на
# # 3600 = это 60 минут в 1 часе и 60 сек в 1 минуте чтобы найти часы
# hours = (duration % 86400) // 3600
# print(hours)
# # minute = (duration % 3600) // 60  # непойму что делать с минутам
# minute = ((duration % 86400) % 3600) // 60
# print(minute)
# seconds = (((duration % 86400) % 3600) % 60) % 60                           # как добавить секунды ведь из считать ненадо они дожны идти остатком?
# print(seconds)