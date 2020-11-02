a = list(map(int, input().split()))


def decorator(function):
    def priem2(a):
        n = function(a)
        if n > 10:
            print('Очень много')
        elif n == 0:
            print('Нет')
        else:
            print('Не достаточно много')
        return
    return priem2


@decorator
def priem(a):
    n = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            n += 1
        else:
            n = n
    return n

priem(a)
