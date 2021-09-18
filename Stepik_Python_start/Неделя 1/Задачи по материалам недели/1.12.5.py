m = []
n = 0

while n != 3:
    m.append(int(input()))
    n += 1

print(max(m[0], m[1], m[2]))
m.remove(max(m[0], m[1], m[2]))
print(min(m[0], m[1]))
m.remove(min(m[0], m[1]))
print(m[0])