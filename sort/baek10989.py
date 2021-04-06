import sys

n = int(sys.stdin.readline())
n_arr = [0] * 10001

for i in range(n):
    m = int(sys.stdin.readline())
    n_arr[m] = n_arr[m] + 1

for i in range(10001):
    if n_arr[i] != 0:
        for j in range(n_arr[i]):
            print(i)