import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
visited = [False] * n
arr = []


def dfs(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            arr.append(i + 1)
            dfs(depth + 1, i + 1, n, m)
            visited[i] = False
            arr.pop()


dfs(0, 0, n, m)

# s = combinations(range(1, n + 1), m)
# for i in s:
#     print(' '.join(map(str, i)))