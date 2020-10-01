n = ''
while not(n.isnumeric()):
    n = input('Введите число: ')
n = int(n)
nn = int(str(n) * 2)
nnn = int(str(n) * 3)
print(n + nn + nnn)
