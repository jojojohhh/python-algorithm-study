import sys

t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    sol = [j for j in range(1, n + 1)]
    for j in range(k):
        for m in range(1, n):
            sol[m] += sol[m - 1]
    print(sol[n-1])