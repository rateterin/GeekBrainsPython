#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 4 Exercise 4
#
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.


from random import randint

src_lst = []
for i in range(randint(10, 50)):
    src_lst.append(randint(1, 100))
dst_lst = [x for x in src_lst if src_lst.count(x) == 1]
print(f'Исходный список:\n{src_lst}')
print(f'Результирующий список:\n{dst_lst}')
