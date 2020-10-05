#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 2 Exercise 2

my_list = []
tmp = 1
while tmp != '':
    tmp = input('Введите очередной элемент списка или пустое значение для завершения списка: ')
    if tmp != '':
        my_list.append(tmp)
print(my_list)
for n in range(0, len(my_list) - 1, 2):
    if n == len(my_list):
        break
    n1 = my_list[n]
    n2 = my_list[n + 1]
    my_list[n] = n2
    my_list[n + 1] = n1
print(my_list)
