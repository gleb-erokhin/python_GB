# Task 1
duration = int(input('Введите время в секундах: '))
# тут я пробовал сделать это с помощью цикла, но все равно не пойму смысл именно
# каким образом вообще отделять часы минуты, на основании какого принципе это делатся
# почему что то делать через % а что то через //. целочисленные и с остатком в чем разница.
if duration < 60:
    print(duration, 'сек')
elif duration > 60:
    days = duration // 86400
    hours = duration % 3600
    print(days, hours)

days = duration // 24 * 60 * 60
print(days)
hour = (duration - days) /
print(hour)


