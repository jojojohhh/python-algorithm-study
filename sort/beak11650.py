import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda n: (n[0], n[1]))
# arr = sorted(arr)
for i in arr:
    print(i[0], i[1])
