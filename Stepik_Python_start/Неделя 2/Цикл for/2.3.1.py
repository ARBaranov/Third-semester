a = int(input())
b = int(input())
c = int(input())
d = int(input())

vertical_vector = []
horizontal_vector = []
count = []

for i in range(c, d + 1):
    horizontal_vector.append(i)

for j in range(a, b + 1):
    vertical_vector.append(j)

for k in horizontal_vector:
    print(' \t', k, end='')
print()
for l in vertical_vector:
    print(l, end=''),
    for k in horizontal_vector:
        print('\t', l*k, end=''),
    print()

#for l in vertical_vector:
 #   'count.append(l)
  #  'for k in horizontal_vector:
   #  '   count.append(l*k)
    #'count.clear()'