a = [int(i) for i in input().split()]
for x in set(a):
    if a.count(x) > 1:
        print(x, end=' ')
