from itertools import count

# f_obj = open('nginx_logs.txt', 'r', encoding='utf-8')
# my_l = []
# unique = []
# for line in f_obj:
#     str_my = line.split()
#     my_l.append(str_my[0])
#     #unique_numbers = list(set(my_l))
#     #print(unique_numbers)
#     for numbers in my_l:
#         unique.append(numbers)
# print(unique)
# f_obj.close()
# print(my_l)

f_obj = open('nginx_logs.txt', 'r', encoding='utf-8')
my_l = []
unique = []
for line in f_obj:
    str_my = line.split()
    my_l.append(str_my[0])
for i in my_l:
    curr_frequency = my_l.count(i)
print(curr_frequency, i)