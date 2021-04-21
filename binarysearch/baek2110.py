from sys import stdin

n, c = map(int, stdin.readline().split())
arr = sorted([int(stdin.readline()) for _ in range(n)])
start, end = 1, arr[-1] - arr[0]

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    x = arr[0]
    for i in range(1, n):
        if x + mid <= arr[i]:
            cnt += 1
            x = arr[i]
    if cnt >= c:
        sol = mid
        start = mid + 1
    else:
        end = mid - 1
print(sol)