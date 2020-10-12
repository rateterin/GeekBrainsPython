#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 3 Exercise 2
#
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def get_user_info(first_name, second_name, born_year, city, email, phone_number):
    return f'Имя: {first_name}, Фамилия: {second_name}, год рождения: {born_year}, город проживания: {city}, ' \
           f'email: {email}, телефон: {phone_number}'
print(get_user_info(first_name='Павлик', second_name='Морозов', born_year=2000, city='Воронеж',
                    email='pmorozov@mail.ru', phone_number='+79029876543'))
