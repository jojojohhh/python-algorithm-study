import sys


n = int(sys.stdin.readline())
n_arr = []
for i in range(n):
    n_arr.append(int(sys.stdin.readline()))

for i in range(n - 1):
    for j in range(i + 1, n):
        if n_arr[i] > n_arr[j]:
            t = n_arr[i]
            n_arr[i] = n_arr[j]
            n_arr[j] = t

for i in n_arr:
    print(i)