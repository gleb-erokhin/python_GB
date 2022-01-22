from time import sleep


class TrafficLight:
    """Создаем защищенную переменную с цветами светофора"""
    __color = ['Красный', 'Желтый', 'Зеленый']

    """Создаем метод класса для работы светофора"""
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1
            """реализуем цикл работы светофора с запросом о продолжении"""
            if i == 3:
                stop = input('Stop trafficlight? yes / no: ')
                if stop == 'yes':
                    print('Светофор выключен!')
                else:
                    i = 0


TrafficLight = TrafficLight()
TrafficLight.running()