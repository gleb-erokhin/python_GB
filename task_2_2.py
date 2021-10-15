my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for elm in my_list:
    # elm.isdigit()
    if elm.isdigit():
        # print(elm, 'цифра')
        new_list.extend(['"', f'{int(elm):02}', '"'])
    elif elm.startswith('+'):
        # print(elm, 'цифра')
        new_list.extend(['"', f'{elm[0]}{int(elm[1:]):02}', '"'])
    else:
        new_list.append(elm)

print(' '.join(new_list))

