#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 2 Exercise 4

my_string = input('Введите несколько слов разделенных пробелами: ')
worlds = my_string.split(' ')
n = 1
for world in worlds:
    print(f'{n} {world[:10]}')
    n += 1
