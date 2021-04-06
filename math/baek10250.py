import sys

t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    a = n % h
    b = n // h + 1
    if n % h == 0:
        a = h
        b = n // h
    print(a*100+b)