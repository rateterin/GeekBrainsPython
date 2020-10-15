#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 4 Exercise 2
#
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.


from random import randint

src_lst = []
for i in range(randint(10, 50)):
    src_lst.append(randint(1, 500))
dst_lst = [x for i, x in enumerate(src_lst) if i > 0 and src_lst[i] > src_lst[i - 1]]
print(f'Исходный список:\n{src_lst}')
print(f'Результирующий список:\n{dst_lst}')
