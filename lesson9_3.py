# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
purchases_sum = [0]  # сумма покупок
with open('test_file/task_3.txt', mode='r', encoding='utf-8') as price_list:
    # вызываем менеджер контекста для открытия на чтение и последующего закрытия файла
    price = price_list.readlines()  # прочитать строки файла, вернуть список из цен товаров(выведутся с \n)
    sum_price_idx = 0  # нулевой индекс первой цены в суммировании
    for i in price:  # проитерироваться по каждой цене (строке) товаров
        if i[:-1].isdigit():  # если в строке - все числа
            purchases_sum[sum_price_idx] += int(i[:-1])  # покупка=сумма таких строк(где все числа, по срезу от 0 до -1)
        else:
            sum_price_idx += 1  # иначе строке присваиваем индекс 1
            purchases_sum.append(0)  # покупка=0

three_most_expensive_purchases = sum(sorted(purchases_sum, reverse=True)[:3])  # сумма 3 самых дорогих покупок

assert three_most_expensive_purchases == 202346
