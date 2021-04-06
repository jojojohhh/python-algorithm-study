import sys


def recursion(n):
    if n == 2:
        return n
    elif n == 0:
        return 1
    else:
        n = n * recursion(n-1)
        return n


n = int(sys.stdin.readline())

print(recursion(n))