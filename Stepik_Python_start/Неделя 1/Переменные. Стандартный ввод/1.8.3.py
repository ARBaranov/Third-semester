X = int(input())
H = int(input())
M = int(input())

common = X + H*60 + M

print(common//60)
print(common-common//60*60)