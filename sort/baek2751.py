import sys

n = int(sys.stdin.readline())
n_arr = []
for i in range(n):
    n_arr.append(int(sys.stdin.readline()))

n_arr.sort()
for i in n_arr:
    print(i)