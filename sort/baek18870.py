import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
xs = list(sorted(set(x)))
xs = {xs[i]: i for i in range(len(xs))}
print(*[xs[i] for i in x])