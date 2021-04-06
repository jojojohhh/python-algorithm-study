import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

# s = permutations(range(1, n + 1), m)
# for i in s:
#     print(' '.join(map(str, i)))

visited = [False] * n
arr = []


def dfs(depth, n, m):
    if depth == m:
        print(*arr)
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            arr.append(i + 1)
            dfs(depth + 1, n, m)
            visited[i] = False
            arr.pop()


dfs(0, n, m)