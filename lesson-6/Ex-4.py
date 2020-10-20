#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 6 Exercise 4

"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


from random import randint


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = 0

    def __init__(self, **kwargs):
        if 'color' in kwargs.keys():
            self.color = kwargs['color']
        if 'name' in kwargs.keys():
            self.name = kwargs['name']
        if 'is_police' in kwargs.keys():
            self.is_police = kwargs['is_police']

    def go(self):
        print(f'{self.name} is start going.')

    def stop(self):
        print(f'{self.name} stopped.')

    def turn(self, direction):
        """direction may be:
           0: north
           1: east
           2: south
           3: west"""
        if direction in range(4):
            print(f"{self.name} turn to the {('north', 'east', 'south', 'west')[direction]}.")

    def show_speed(self):
        print(f'Current speed: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60 and not self.is_police:
            print(f'Overspeed!!!\n60 is maximum!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40 and not self.is_police:
            print(f'Overspeed!!!\n40 is maximum!')


class PoliceCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._is_police = 1


cars = (TownCar(color='white', name='Opel'),
        SportCar(color='red', name='Ferrari'),
        WorkCar(color='black', name='Ford', is_police=True),
        PoliceCar(color='blue', name='Renault'))

for car in cars:
    car.go()
    car.turn(randint(0, 3))
    car.speed = randint(1, 100)
    car.show_speed()
    car.stop()
