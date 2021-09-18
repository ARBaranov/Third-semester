def modify_list(l):
    a = len(l)
    l.extend([i // 2 for i in l if i % 2 == 0])
    del l[:a]


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)