import sys

n, m = map(int, sys.stdin.readline().split())
arr = []


def dfs(depth, n, m):
    if depth == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(i + 1)
        dfs(depth + 1, n, m)
        arr.pop()