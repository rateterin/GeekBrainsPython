#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 6 Exercise 1

"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
(Далее следует какой-то бред. На лекции советовали его проигнорить.)
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт."""


from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self, green_slip=7):
        self.__green_slip = green_slip

    def running(self):
        for n, lt_color in cycle(enumerate(('Красный', 'Желтый', 'Зеленый'))):
            yield lt_color
            sleep((7, 2, self.__green_slip)[n])


tl = TrafficLight(3)
for color in tl.running():
    print(color)
