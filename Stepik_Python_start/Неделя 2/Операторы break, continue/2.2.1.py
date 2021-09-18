a = int(input())

while a <= 100:
    if a < 10:
        a = int(input())
        pass
    elif a >= 10:
        print(a)
        a = int(input())