#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 2 Exercise 3

test_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
             10: 'Осень', 11: 'Осень', 12: 'Зима'}
test_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
month = int(input('Введите месяц (целое число от 1 до 12): '))
print(f'Определение времени года по номеру месяца, используя словарь: {test_dict[month]}')
print(f'Определение времени года по номеру месяца, используя список: {test_list[month]}')
