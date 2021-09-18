import math
type = input()

if type == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a * b))
elif type == 'круг':
    r = int(input())
    print(float(3.14 * pow(r, 2)))
elif type == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))