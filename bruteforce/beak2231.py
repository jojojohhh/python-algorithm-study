import sys

n = int(sys.stdin.readline())
m = 0
for i in range(1, n + 1):
    k = list(map(int, str(i)))
    n_sum = i + sum(k)
    if n_sum == n:
        m = i
        break

print(m)