a = int(input())
if a == 0:
    print(' ')
if a == 1:
    print(1)
s = []
for i in range(a+1):
    b = str(i) * i
    s.append(b)

s.remove(s[0])
string = ''
for i in range(len(s) - 1):
    string += s[i]
for i in range(len(string[:a])):
    if i < 45:
        print(string[i], end=' ')
    else:
        if i % 2 == 0:
            pass
        else:
            print(string[i] + string[i + 1], end=' ')