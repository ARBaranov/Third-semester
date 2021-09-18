m = list(input().split())
x = str(input())
for i in range(len(m)):
    if x == m[i]:
        print(i, end=' ')
    else:
        pass

if m.count(x) == 0:
    print('Отсутствует')

