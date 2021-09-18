a = str(input())
c = a.upper().count('c'.upper())
g = a.upper().count('g'.upper())
print((c+g)/len(a)*100)