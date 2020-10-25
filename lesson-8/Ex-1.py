#!/usr/bin/env/python
#
# Written by Teterin Roman
# for GeekBrains Python course
# Python base
# Lesson 8 Exercise 1

"""== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html"""


from random import randint
from copy import deepcopy

loser = ''


class LottoCard:
    used_cards = []  # Выданные карточки (для исключения повторений)

    def __init__(self, name):
        self.__name = name
        data = [list(' ' * 9) for x in range(3)]
        matrix = deepcopy(data)
        while matrix == data or matrix in LottoCard.used_cards:
            numbers = list(range(1, 91))
            for line in range(3):
                while len(list(filter(lambda x: type(x) == int, matrix[line]))) < 5:
                    ni = randint(0, len(numbers) - 1)
                    mi = (numbers[ni] - 1) // 10
                    if numbers[ni] not in matrix[0] and numbers[ni] not in matrix[1] and \
                            numbers[ni] not in matrix[2] and matrix[line][mi] == ' ':
                        matrix[line][mi] = numbers.pop(ni)
        self.__matrix = matrix
        self.__make_cell_list()
        LottoCard.used_cards.append(self.__matrix)

    def __make_cell_list(self):
        self.__cell_list = [self.__matrix[l][r] for l in range(len(self.__matrix))
                            for r in range(len(self.__matrix[0]))]

    def check(self, num):
        return num in self.__cell_list

    def cross_out(self, num):
        line = self.__cell_list.index(num) // 9
        row = self.__cell_list.index(num) % 9
        self.__matrix[line][row] = '-'
        self.__make_cell_list()

    def get_name(self):
        return self.__name

    def __str__(self):
        return self.__name + '\n' + \
               '\n'.join([' '.join('XX' if y == '-' else ('  ' if y == ' ' else (' ' + str(y) if y < 10 else str(y)))
                                   for y in x) for x in self.__matrix])


class LottoBarrelsBag:
    def __init__(self):
        self.__numbers = list(range(1, 91))

    @property
    def next(self):
        if len(self.__numbers) > 0:
            return self.__numbers.pop(randint(0, len(self.__numbers) - 1))

    @property
    def remains(self):
        return len(self.__numbers)


players = (LottoCard('Игрок'), LottoCard('Компьютер'))
barrels = LottoBarrelsBag()
while 'barrel_num' not in locals() or loser == '':
    barrel_num = barrels.next
    print(f'Из мешка достали бочонок: {barrel_num} (осталось {barrels.remains})')
    for i in range(len(players)):
        print(players[i])
    if randint(1, 50) == 1:
        loser = 1
        break
    elif players[1].check(barrel_num):
        players[1].cross_out(barrel_num)
    answer = ''
    while answer not in ('y', 'n'):
        answer = input(f'Зачеркнуть цифру? (y/n) ').lower()
    answer = True if answer == 'y' else False
    if players[0].check(barrel_num) != answer:
        loser = 0
        break
    elif answer:
        players[0].cross_out(barrel_num)
print(f'{players[loser].get_name()} проиграл!!!\nИгра окончена.')
