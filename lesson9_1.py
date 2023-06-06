# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
with open('test_file/task1_data.txt', encoding='utf-8') as our_list:
    # вызываем менеджер контекста для открытия и последующего закрытия файла
    res = ''
    our_list = our_list.readlines()  # прочитать строки файла, вернуть список из строк
    for i in our_list:  # проитерироваться по каждому элементу строки
        res += ''.join(j for j in i if not j.isdigit())
        # проитерироваться по каждому элементу подстроки, если элемент не число
        # вывести в результат: собрать строку из элементов
with open('test_file/task1_answer.txt', mode='w', encoding='utf-8') as res_file:
    # вызываем менеджер контекста для открытия, перезаписи и последующего закрытия файла
    res_file.writelines(res)  # добавить построчно

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
