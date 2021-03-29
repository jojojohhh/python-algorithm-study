import sys

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()
sol = 0

for i in range(len(n_list) - 2):
    for j in range(i + 1, len(n_list) - 1):
        for k in range(j + 1, len(n_list)):
            if n_list[i] + n_list[j] + n_list[k] > m:
                continue
            else:
                sol = max(sol, n_list[i] + n_list[j] + n_list[k])

print(sol)