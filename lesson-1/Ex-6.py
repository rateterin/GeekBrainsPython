a = float(input('Введите результат спортсмена в первый день: '))
b = float(input('Введите желаемый результат: '))
day = 1
a1 = ''
while a < b:
    a1, a2 = str(a).split('.')
    if int(a2[:2]) > 0:
        a1 += '.' + a2[:2].rstrip('0')
    print(f'{day}-й день: {a1}')
    a += a * .1
    day += 1
print(f'{day}-й день: {a1}')
print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')
