gain = float(input('Какова выручка: '))
expenses = float(input('Каковы издержки: '))
if gain > expenses:
    fin_res = 'Прибыль'
elif expenses > gain:
    fin_res = 'Убыток'
else:
    fin_res = '0'
print(f'Финансовый результат фирмы: {fin_res}')
if fin_res == 'Прибыль':
    print(f'Рентабельность фирмы: {(gain - expenses) / gain}')
workers = int(input('Сколько сотрудников работает в фирме: '))
print(f'Прибыль на одного сотрудника: {(gain - expenses) / workers}')
