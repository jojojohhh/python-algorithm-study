from sys import stdin

k, n = map(int, stdin.readline().split())
arr_k = [int(stdin.readline()) for _ in range(k)]
start, end = 1, max(arr_k)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in arr_k:
        lines += i // mid

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)