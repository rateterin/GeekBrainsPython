#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 7 Exercise 2

"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod

all_cloth_cost = 0.0


class Cloth(ABC):
    def __init__(self, v=0.0, h=0.0):
        global all_cloth_cost
        self.v = v
        self.h = h
        all_cloth_cost += self.cloth_cost

    @abstractmethod
    def cloth_cost(self):
        pass


class Coat(Cloth):
    @property
    def cloth_cost(self):
        return self.v / 6.5 + 0.5


class Costume(Cloth):
    @property
    def cloth_cost(self):
        return self.h * 2 + 0.3


coat = Coat(v=30)
costume = Costume(h=1.2)

print(f'Расход ткани на пальто: {coat.cloth_cost}')
print(f'Расход ткани на костюм: {costume.cloth_cost}')
print(f'Общий расход ткани на пошив одежды: {all_cloth_cost}')
