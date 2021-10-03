N = list(map(int, input().split()))

def function(arr):
    cnt = 0
    for i in range(len(N)):
        if N[i]%2 == 0: cnt += 1
    return(cnt)

def decoration(func, N):
    n = function(N)
    if n == 0: print('Нет(')
    elif n > 10: print('Очень много')
    else: print(n)

function = decoration(function, N)
#print(function(N))
