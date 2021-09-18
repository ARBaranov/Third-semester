s = 0
m = []
while True:
    a = int(input())
    m.append(a)
    s += a
    if s == 0:
        print(sum([i*i for i in m]))
        break
