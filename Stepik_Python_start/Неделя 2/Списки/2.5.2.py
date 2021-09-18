a = [int(i) for i in input().split()]
b = []
for i in range(len(a)):
    if len(a) == 1:
        print(a[0])
    elif i == 0:
        b.append(a[i-1] + a[i+1])
    elif i == len(a) - 1:
        b.append(a[0] + a[i-1])
    else:
        b.append(a[i-1] + a[i+1])

for i in b:
    print(i, end=' ')