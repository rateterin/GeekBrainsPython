#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 4 Exercise 5
#
# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

lst = [x for x in range(100, 105) if x % 2 == 0]
print(f'Список: {lst}')
print(f'Произведение всех элементов: {reduce(lambda x,y: x * y, lst)}')
