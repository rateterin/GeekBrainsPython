n = ''
while not(n.isnumeric()):
    n = input('Введите целое положительное число: ')
n = int(n)
max_digit = 0
while n != (n % 10):
    if max_digit < (n % 10): max_digit = n % 10
    n //= 10
print(max_digit)
