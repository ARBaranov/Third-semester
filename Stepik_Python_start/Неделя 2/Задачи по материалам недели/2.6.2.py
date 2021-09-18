a = int(input())
m = list()
m.append(list(i+1 for i in range(a)))
m = [i for i in m[0]]
m = [[i] * i for i in m]
x = []
for i in range(len(m)):
    for j in range(len(m[i])):
        x.append(m[i][j])
for i in range(len(m)):
    print(x[i], end=' ')