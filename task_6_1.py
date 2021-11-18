# with open('nginx_logs.txt', 'w+', encoding='utf-8') as file:
#     ext = file.read()
#     print(ext)
# print(file.closed)

f_obj = open('nginx_logs.txt', 'r', encoding='utf-8')
lines = f_obj.readlines()
print(lines)