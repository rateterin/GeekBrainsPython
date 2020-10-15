#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 5 Exercise 4

"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

from functools import reduce

new_lines = []
with open('Ex-4.txt', 'r', encoding='utf-8') as src_file:
    lines = [line.strip() for line in src_file.readlines()]
with open('Ex-4_1.txt', 'w', encoding='utf-8') as dst_file:
    for num, line in enumerate(lines):
        line = line.replace('One', 'Один')
        line = line.replace('Two', 'Два')
        line = line.replace('Three', 'Три')
        line = line.replace('Four', 'Четыре')
        if num > 0:
            line = '\n' + line
        dst_file.writelines(line)
