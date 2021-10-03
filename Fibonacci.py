import sys
import argparse

def createParser():
    prs = argparse.ArgumentParser()
    prs.add_argument('-n', default='n')
    return prs

if __name__ == '__main__':
    pr = createParser()
    namespace = pr.parse_args()
    n = namespace.n
    n = int(n)

    fib1 = 0
    fib2 = 1

    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1

    print(fib2)
