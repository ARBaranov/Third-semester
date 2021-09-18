num1 = int(input())
num2 = int(input())

def gcd_subtraction(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1 or num2

print(num1 * num2 // gcd_subtraction(num1, num2))