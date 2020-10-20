#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 6 Exercise 3

"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров)."""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = 0

    def __init__(self, name, surname, position='default', **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        if 'wage' and 'bonus' in kwargs.keys():
            self._income = {'wage': kwargs['wage'], 'bonus': kwargs['bonus']}


class Position(Worker):

    def __init__(self, name, surname, position='default', **kwargs):
        super().__init__(name, surname, position='default', **kwargs)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


workers = (Position('Василий', 'Петров', wage=123, bonus=345),
           Position('Сергей', 'Смирнов', 'заколачиватель гвоздей', wage=3000, bonus=1000),
           Position('Александр', 'Серышев', 'заворачиватель саморезов', wage=3050, bonus=1500))
for worker in workers:
    print(f'{worker.get_full_name()} полный доход: {worker.get_total_income()}')

