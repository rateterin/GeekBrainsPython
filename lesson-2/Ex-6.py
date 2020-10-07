#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 2 Exercise 6

n = 1
d = {}
products = []
add_product_response = 'y'
while True:
    if add_product_response == 'n':
        break
    elif add_product_response == 'y':
        d['Название'] = input('Введите название товара: ')
        d['Цена'] = int(input('Введите цену товара: '))
        d['Количество'] = int(input('Введите количество товара: '))
        d['Ед'] = input('Введите единицу измерения товара: ')
        products.append((n, dict(d)))
        n += 1
    add_product_response = input('Добавить еще один товар (y/n): ')
p_name = []
p_price = []
p_count = []
p_unit = []
for i in range(len(products)):
    line = products[i]
    product = line[1]
    p_name.append(product['Название'])
    p_price.append(product['Цена'])
    p_count.append(product['Количество'])
    p_unit.append(product['Ед'])
print({'Название': list(p_name), 'Цена': list(p_price), 'Количество': list(p_count), 'Ед': list(p_unit)})
