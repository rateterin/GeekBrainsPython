#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 7 Exercise 3

"""Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к
клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****."""

CELLS1 = 17  # ячеек в первой клетке
CELLS2 = 7  # ячеек во второй клетке
CELLS_IN_ROW = 4  # на сколько ячеек разбивать клетку в методе make_order


class OrgCell:
    def __init__(self, num_cells=1):
        try:
            self.num_cells = int(num_cells)
        except ValueError:
            self.num_cells = 1

    def __add__(self, other):
        if isinstance(other, OrgCell):
            return OrgCell(self.num_cells + other.num_cells)

    def __sub__(self, other):
        if isinstance(other, OrgCell):
            if self.num_cells >= other.num_cells:
                return OrgCell(self.num_cells - other.num_cells)
            else:
                print('Вычитаемая клетка должна быть меньше!!')

    def __mul__(self, other):
        if isinstance(other, OrgCell):
            return OrgCell(self.num_cells * other.num_cells)

    def __truediv__(self, other):
        if isinstance(other, OrgCell):
            return OrgCell(round(self.num_cells / other.num_cells))

    def __str__(self):
        return str(self.num_cells)

    def make_order(self, num_in_row):
        if type(num_in_row) != int:
            return 'Ожидалось целое число'
        if self.num_cells >= num_in_row:
            return ('*' * num_in_row + '\n') * (self.num_cells // num_in_row) + '*' * (self.num_cells % num_in_row)
        else:
            return 'Общее количество ячеек меньше запрошенного'


cell1 = OrgCell(CELLS1)
cell2 = OrgCell(CELLS2)
print(f'cell1 = {cell1}, cell2 = {cell2}')
print(f'cell1 + cell2 = {cell1 + cell2}')
print(f'cell1 - cell2 = {cell1 - cell2}')
print(f'cell1 * cell2 = {cell1 * cell2}')
print(f'cell1 / cell2 = {cell1 / cell2}')
print(f'cell1 - 3 = {cell1 - 3}')
print(f'cell1 + qwe = {cell1 - "qwe"}')
print(f'cell1 * 3 = {cell1 * 3}')
print(f'Результат метода cell1.make_order({CELLS_IN_ROW}):')
print(cell1.make_order(CELLS_IN_ROW))
