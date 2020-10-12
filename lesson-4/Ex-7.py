#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 4 Exercise 7
#
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел, начиная с 1! и до n!.


from math import factorial


def fact(arg_1):
    num = 1
    while num < arg_1:
        yield factorial(num)
        num += 1


for el in fact(6):
    print(el)
