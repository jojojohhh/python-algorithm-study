import sys

n, m = map(int, sys.stdin.readline().split())
arr = []


def dfs(depth, idx, n, m):
    if depth == m:
        print(*arr)
        return
    for i in range(idx, n):
        arr.append(i + 1)
        dfs(depth + 1, i, n, m)
        arr.pop()


dfs(0, 0, n, m)