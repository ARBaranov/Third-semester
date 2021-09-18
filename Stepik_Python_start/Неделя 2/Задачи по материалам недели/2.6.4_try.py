import numpy as np

m = []
a = list(input().split())
while a != ['end']:
    m.append(a)
    a = input().split()

O = np.zeros((len(m), len(m[0])))  # len(m) - столбцы, len(m[0]) - строки

for i in range(len(m[0])):
    for j in range(len(m)):
        O[i][j] = int(m[i][j - 1]) + int(m[i][j + 1 - len(m)]) + int(m[i + 1 - len(m[0])][j]) + int(m[i - 1][j])

for i in range(len(O)):
    for j in range(len(O[i])):
        print(int(O[i][j]), end=' ')
    print()
