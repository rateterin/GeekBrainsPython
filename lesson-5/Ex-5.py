#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 5 Exercise 5

"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randint

with open('Ex-5.txt', 'w+', encoding='utf-8') as f:
    for i in range(1, randint(10, 100)):
        f.writelines(f"{('', ' ')[i > 1]}{randint(1, 100)}")
    f.seek(0)
    print(sum([int(x) for x in f.read().split()]))
