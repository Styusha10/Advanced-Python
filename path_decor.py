import time

def decormk(path:str):
    def decor(sm):
        def wrapped(*args, **kwargs):
            with open(path, 'w') as file:
                tmp = time.ctime()
                time.clock()
                res = sm(*args, *kwargs)
                arr = args
                array = [str(tmp), arr, res, time.clock(), alltime]
                file.writeln("\n".join(array))
                file.close()
            return(sm(*arr, **kwargs))
        return(wrapped)
    return(decor)

@decormk('f.txt')

def sm(a, b): return a+b

a, b = map(int, input().split())
sm(a, b)
