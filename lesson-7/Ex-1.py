#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 7 Exercise 1

"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, lst_lst):
        self.lst_lst = lst_lst

    def __str__(self):
        out = ''
        for el in self.lst_lst:
            out += ',\t'.join((str(n) for n in el)) + '\n'
        return out

    def __add__(self, other):
        if len(self.lst_lst) == len(other.lst_lst):
            new_matrix = []
            for el1, el2 in zip(self.lst_lst, other.lst_lst):
                if len(el1) != len(el2):
                    return 'Размеры матриц не совпадают!!'
                else:
                    new_matrix.append([x + y for x, y in zip(el1, el2)])
            return new_matrix
        else:
            return 'Размеры матриц не совпадают!!'


m1 = Matrix([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

m2 = Matrix([[7, 8, 9],
             [1, 2, 3],
             [4, 5, 6]])

m3 = Matrix(m1 + m2)
print(f'{m1}+\n{m2}=\n{m3}')
