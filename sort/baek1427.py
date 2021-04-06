import sys

n = int(sys.stdin.readline())

arr = list(map(int, list(str(n))))
arr.sort(reverse=True)
for i in arr:
    print(i, end='')