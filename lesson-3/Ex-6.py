#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 3 Exercise 6
#
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(world):
    if len(world) % 2:
        return world.capitalize()
    else:
        return world[0].upper() + world[1:].lower()


print(int_func('cheese'))
print(int_func('smile'))


print(' '.join(list(map(int_func, input('Введите несколько слов, разделенных пробелами: ').split()))))

