#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 3 Exercise 3
#
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.


def my_func(arg_1, arg_2, arg_3):
    return int(arg_1) + int(arg_2) + int(arg_3) - min(arg_1, arg_2, arg_3)


print(my_func(5, 3, 7))
