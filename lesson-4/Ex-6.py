#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 4 Exercise 6
#
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.


from itertools import count, cycle


start_num = int(input('Введите начальное число: '))
stop_num = int(input('Введите конечное число: '))
my_lst = []

# а)
for num in count(start_num):
    if num <= stop_num:
        my_lst.append(num)
        print(num)
    else:
        break

# б)
cycle_num = int(input('Сколько раз повторить? '))
n = 0
for i in cycle(my_lst):
    n += 1 / (len(my_lst))
    if n <= cycle_num:
        print(i)
    else:
        break
