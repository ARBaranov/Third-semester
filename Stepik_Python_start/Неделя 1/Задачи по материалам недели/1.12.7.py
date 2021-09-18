a = int(input())

first = a // 100000 % 10
second = a // 10000 % 10
third = a // 1000 % 10
fourth = a // 100 % 10
fifth = a // 10 % 10
six = a % 10

if first + second + third == fourth + fifth + six:
    print('Счастливый')
else:
    print('Обычный')