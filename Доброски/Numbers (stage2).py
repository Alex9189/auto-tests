a = '45'
b = '3.14'
string1 = 'нельзя просто так взять и начать писать автотесты'
string3 = r'python\name'
string2 = 'Все получится' \
          '\'Летс Гоу\'\n'

our_org = 'JJJ Watt'
adressee = 'Хьюстон, Техас'
nom_name = 'Дилайн_Лайнбэк_Дифенс'
result = f""" Поставить  в %s, на позицию %s, в команду %s
""" % (our_org, adressee, nom_name)
result2 = """ Поставить  в {2}, на позицию {0}, в команду {1}
""" .format (our_org, adressee, nom_name)
result3 = f"""Поставить  в {our_org}, на позицию {adressee}, в команду {nom_name}
"""
print(result2, result, result3)
# c = string1[0:6]
# d = string1.replace('нельзя', 'Можно')
# g = string1.replace('а', 'о')
# print(d)
# print(string1)
# print(g)
# print(string1.find('я'))
# print(string1.upper())
# print(string1.lower())
# print(c)
# print(our_org[4:])
# print(our_org[-4:])
# print('Можно' + string1[6:])
# print(string1[0:6])
# print(string1[0], string1[-1])
# # print(string1, string2*5)
# # print(string3, a, b, type(a), type(b))

a = 5 * 4 ** 2 / (4-2)
b = 0.5
c = a + b
b += a  # оператор присваивания - записываем значение не в новую переменную а в уже существующую
d = int(1.2)
f = int(1.2)
g = round(1.7)
# print(a + b)
# print(a * b)
# print(a - b)
# print(a / b)
# print(a ** b)  # степень
# print(a % b)  # остаток от деления
# print(a // b)  # целое число от деления
# print(b)
# print(c, d, f, g)
# print(string1, string2*5)


