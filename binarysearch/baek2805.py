from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    length = 0
    for i in arr:
        if i > mid:
            length += i - mid
    if length >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)