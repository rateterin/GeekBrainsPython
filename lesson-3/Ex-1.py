#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 3 Exercise 1
#
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_div(dividend, divider):
    try:
        quotient = dividend / divider
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    else:
        return quotient


n1 = int(input('Введите делимое: '))
n2 = int(input('Введите делитель: '))
print(my_div(n1, n2))
