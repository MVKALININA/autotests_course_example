# Повторяшки
# Напишите функцию repeats, которая принимает на вход строку our_str,
# смотрит, сколько раз каждый символ уже встречался, и добавляет количество к символам с помощью постфикса формата _n.
# Возвращается новая строка
# Например (Ввод --> Вывод):
# 'letter' --> l_1e_1t_1t_2e_2_r_1


def repeats(our_str):
    """
    Функция принимает в себя строку.
    Возвращает новую строку по маске х_n, где х-символ строки, n-количество повторений символа в предыдущих итерациях
    :param our_str: исходная строка
    :return: отформатированная строка
    """
    our_str_dict = {}
    new_str = ''
    for j in our_str:  # проходимся по каждому элементу строки списка
        if our_str_dict.get(j) is None:  # если в строке элемента еще нет
            our_str_dict.update({j: 1})  # пишем в словарь пару: "ключ:значение":"буква:1"
            new_str = new_str + f'{j}_1'  # в строке на выходе будет "буква_1"
        else:
            k = our_str_dict.get(j) + 1  # если есть повторение буквы, прибавляем +1 при каждой итерации
            our_str_dict.update({j: k})  # пишем в словарь пару: "ключ:значение с прибавлением":"буква:кол-во повторов"
            new_str = new_str + f'{j}_{k}'  # в строке на выходе будет "буква_кол-во повторов"
    return new_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = ['letter', "карабасбарабас", "околоводопроводного", "еженедельное", "Караганда", "контрреформатор",
        'аббревиатура', '', 'чечевичечка', 'колокольчик', 'контрреволюционер', 'длинношеее']

test_data = ['l_1e_1t_1t_2e_2r_1',
             'к_1а_1р_1а_2б_1а_3с_1б_2а_4р_2а_5б_3а_6с_2',
             'о_1к_1о_2л_1о_3в_1о_4д_1о_5п_1р_1о_6в_2о_7д_2н_1о_8г_1о_9',
             'е_1ж_1е_2н_1е_3д_1е_4л_1ь_1н_2о_1е_5',
             'К_1а_1р_1а_2г_1а_3н_1д_1а_4',
             'к_1о_1н_1т_1р_1р_2е_1ф_1о_2р_3м_1а_1т_2о_3р_4',
             'а_1б_1б_2р_1е_1в_1и_1а_2т_1у_1р_2а_3',
             '',
             'ч_1е_1ч_2е_2в_1и_1ч_3е_3ч_4к_1а_1',
             'к_1о_1л_1о_2к_2о_3л_2ь_1ч_1и_1к_3',
             'к_1о_1н_1т_1р_1р_2е_1в_1о_2л_1ю_1ц_1и_1о_3н_2е_2р_3',
             'д_1л_1и_1н_1н_2о_1ш_1е_1е_2е_3'
             ]

for i, d in enumerate(data):
    assert repeats(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
