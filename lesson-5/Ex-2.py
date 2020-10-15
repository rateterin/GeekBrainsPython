#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 5 Exercise 2

"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('Ex-2.txt', 'r', encoding='utf-8') as my_file:
    for num, line in enumerate(my_file.readlines(), start=1):
        print(f'{line.strip()}')
        print(f'Строка {num}, содержит слов {len(line.split())}')
