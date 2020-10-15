#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 4 Exercise 1
#
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

err = False
try:
    script_name, worked_hours, price_hour, premium = argv
    worked_hours = int(worked_hours)
    price_hour = int(price_hour)
    premium = int(premium)
except (ValueError, TypeError):
    err = True
    print(f'''Script must run with 3 arguments <worked_hours> <price_hour> <premium>
All args is required and must have UnsignedInteger type.''')
if not err:
    print(worked_hours * price_hour + premium)
