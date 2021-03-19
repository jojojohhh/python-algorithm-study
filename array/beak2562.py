import sys

n_max = int(sys.stdin.readline())
i_max = 1

for i in range(8):
    n = int(sys.stdin.readline())
    if n_max < n:
        n_max = n
        i_max = i + 2
print(n_max)
print(i_max)