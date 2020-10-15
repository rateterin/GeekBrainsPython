#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 5 Exercise 3

"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('Ex-3.txt', 'r', encoding='utf-8') as my_file:
    my_lst = [line.strip().split() for line in my_file.readlines()]
low_salary_names_lst = [elem[0] for elem in my_lst if int(elem[1]) < 20000]
avg_salary = sum([int(elem[1]) for elem in my_lst]) / len(my_lst)
print(f'Зарплата меньше 30000 рублей: {low_salary_names_lst}')
print(f'Средняя зарплата: {round(avg_salary, 2)}')
