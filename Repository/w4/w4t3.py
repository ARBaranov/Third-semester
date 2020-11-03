def swap(function):
    def wrap(*args, **kwargs):
        args = args[::-1]
        function(*args, **kwargs)
        return
    return wrap

@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

print(div(2, 4, show=True))