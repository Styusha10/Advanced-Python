def swap(func):
    def wrapped(*args, **kwargs):
        arr = args[::-1]
        return(func(*arr, **kwargs))
    return wrapped

@swap


def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

x, y = map(int, input().split())
div(x, y, show=True)
