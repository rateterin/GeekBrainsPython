#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 5 Exercise 1

"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open('Ex-1.txt', 'w', encoding='utf-8') as my_file:
    while True:
        str_to_write = input('Введите строку для записи в файл или оставьте пусто для завершения:\n')
        if str_to_write == '':
            break
        else:
            if my_file.tell() > 0:
                my_file.write('\n')
            my_file.write(f'{str_to_write}')
