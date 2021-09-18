def modify_list(l):
    m = []
    b = l[::-1]
    for i in range(len(b) - 1, -1, -1):
        if b[i] % 2 == 0:
            m.append(b[i] // 2)
        else:
            b.pop(i)




lst = [1, 3, 5, 7]
print(modify_list(lst))
print(lst)