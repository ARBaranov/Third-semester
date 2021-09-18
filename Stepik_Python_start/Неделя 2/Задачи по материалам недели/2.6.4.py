a = []
while True:
    str = input()
    if str == 'end':
        break
    row = str.split()
    for i in range(len(row)):  # преобразование элементов в число
        row[i] = int(row[i])
    a.append(row)
for i in range(len(a)):  # старт вывода новой матрицы
    for j in range(len(a[i])):
        print(a[i - 1][j] + a[i - len(a) + 1][j] + a[i][j - 1] + a[i][j - len(a[i]) + 1], end=' ')
    print()
