i = 3
with open('text.txt', 'w') as file:
    while i != 0:
        file.write('We can do this, lets go\n')
        i -= 1
with open('text.txt', 'r') as file:
    for line in file:
        print(line)