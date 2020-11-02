import sys

def fib(n):
    f1 = 0
    f2 = 1
    for __ in range(n):
        f1, f2 = f2, f1+f2
    return f1

if __name__ == '__main__':

    if len(sys.argv) >= 1:
        if sys.argv[1] == '-n':
            print(sys.argv[2])
            print(str(fib(int(sys.argv[2]))))
        else:
            print(str(fib(int(sys.argv[0]))))
