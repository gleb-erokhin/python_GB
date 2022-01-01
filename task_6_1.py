f_obj = open('nginx_logs.txt', 'r', encoding='utf-8')
my_l = []
for line in f_obj:
    str_my = line.split()
    my_l.append((str_my[0], str_my[5].replace('"', ''), str_my[6]))
f_obj.close()
print(my_l)