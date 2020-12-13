def my_fib(n):
    if n > 0:
        a = 1
        yield a
        if n > 1:
            b = 1
            yield b
            if n > 2:
                k = 2
                while k != n:
                    c = a + b
                    yield c
                    a, b = b, c
                    k += 1


for i in my_fib(0):
    print(i)