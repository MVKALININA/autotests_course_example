# Задание1
a = 2  # Сторона квадрата
P = 4 * a  # Периметр квадрата
S = a ** 2  # Площадь квадрата
d = a * (2 ** (1/2))  # Диагональ квадрата
print(f'Периметр квадрата со стороной 2 равен {P}')
print(f'Площадь квадрата со стороной 2 равна {S}')
print(f'Диагональ квадрата со стороной 2 равна {d}')
print()
# Задание2
# a * x ** 2 + b * x + c = 0
# Вычисление корней по формуле для квадратного уравнения с дискриминантом > 0
a = 1
b = 5
c = 5
D = b ** 2 - 4 * a * c  # Считаем дискриминант
x1 = (-b + D ** 0.5) / 2 * a  # первый корень
x2 = (-b - D ** 0.5) / 2 * a  # второй корень
print(f'Дискриминант уравнения равен: {D}')
print(f'Значение первого корня:  {x1}')
print(f'Значение второго корня: {x2}')
print()
# Задание3
string1 = "РАша"
string2 = "наША"
space = " "
string12 = string1.replace(string1[:2], string2[:2]) + space + string2.replace(string2[:2], string1[:2])
print(string12)
print()
# Задание4
# C:\Users\mv.kalinina\AppData\Local\Programs\Opera\opera.exe
name = r'C:\Users\mv.kalinina\AppData\Local\Programs\Opera\opera.exe'
name_split = name.split('\\')
file = name_split[-1].split('.')[0]  # Название файла без расширения
disk = name_split[0][0]  # Название диска
root_folder = name_split[1]  # Название корневой папки
print(f'Название файла без расширения - {file}, Название диска - {disk}, Название корневой папки - {root_folder}')
print()
# Задание5
a = 8
b = 5
c1 = a + b
c2 = a * b
string_c1 = f'{a} + {b} = {c1}'
string_c2 = f'{a} * {b} = {c2}'
print(string_c1, type(string_c1))
print(string_c2, type(string_c2))
print()
# Задание6
a = "1234567"
c = a[::2]
print(c)
print()
# Задание7
# срез минимальной длины: ‘t whangs f’
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
# Первая строка посимвольно:
first_string_1 = first_string[0]
first_string_2 = first_string[1]
first_string_3 = first_string[2]
# Определяем положение каждого символа во второй строке:
symbol1 = second_string.find(first_string_1)
symbol2 = second_string.find(first_string_2)
symbol3 = second_string.find(first_string_3)
# Определяем мин. и макс. среди трех значений:
max_value = max(symbol1, symbol2, symbol3)
min_value = min(symbol1, symbol2, symbol3)
# Выводим вторую строку в срезе от мин. к макс. значению:
print(second_string[min_value:max_value + 1])
