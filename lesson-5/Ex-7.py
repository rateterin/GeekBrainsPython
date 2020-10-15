#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 5 Exercise 7

"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""


from json import dump as json_dump
profit = {}
avg_profit = []
with open('Ex-7.txt', 'r', encoding='utf-8') as src_file:
    firms = {el.split()[0]: [el.split()[1], int(el.split()[2]), int(el.split()[3])] for el in src_file.readlines()}
for firm in firms:
    profit[firm] = firms[firm][1] - firms[firm][2]
avg_profit = [el for el in profit.values() if el >= 0]
avg_profit = round(sum(avg_profit) / len(avg_profit), ndigits=2)
with open('Ex-7_1.json', 'w', encoding='utf-8') as json_file:
    json_dump([profit, {'average_profit': avg_profit}], json_file)
