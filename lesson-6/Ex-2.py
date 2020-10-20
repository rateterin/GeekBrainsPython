#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 6 Exercise 2

"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины
полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т"""


class Road:
    def __init__(self, length=1, width=2):
        self._length = length
        self._width = width

    def need_mass(self):
        mass = self._width * self._length * 5
        if mass >= 1000:
            mass /= 1000
            ed = 'т'
        else:
            ed = 'кг'
        return f'{self._width}м * {self._length}м * 5см = {mass}{ed}'


road_1 = Road(width=13, length=10100)
road_2 = Road(length=53)
print(road_1.need_mass())
print(road_2.need_mass())
