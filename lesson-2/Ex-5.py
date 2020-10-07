#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 2 Exercise 5

my_list = [7, 5, 3, 3, 2]
r = int(input('Введите рейтинг (целое число): '))
my_list.append(r)
my_list.sort(reverse=True)
print(my_list)
