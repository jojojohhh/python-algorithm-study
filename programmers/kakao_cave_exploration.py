from collections import deque


def solution(n, path, order):
    answer = True
    adj = {n: [] for n in range(n)}
    for s, e in path:
        adj[s].append(e)
        adj[e].append(s)

    precedeA = {}
    precedeB = {}

    for a, b in order:
        precedeA[a] = b
        precedeB[b] = a
        if b == 0:
            return False
        if a == 0:
            precedeA[0] = 0

    visited = [0]*n
    visited[0] = 1

    q = deque()
    q.append(0)
    print(adj)
    print(precedeA, precedeB)
    while q:
        current = q.popleft()
        print(current, precedeA.get(precedeB.get(current)), precedeB.get(current))
        if current == precedeA.get(precedeB.get(current)):
            visited[current] = 2
        else:
            print(adj[current])
            for neighbor in adj[current]:
                print(visited)
                if visited[neighbor] == 0:
                    q.append(neighbor)
                    visited[neighbor] = 1

                    if precedeA.get(neighbor):
                        if visited[precedeA[neighbor]] == 2:
                            q.append(precedeA[neighbor])
                            visited[precedeA[neighbor]] = 1

                        precedeA[neighbor] = 0

    for i in visited:
        if i == 0:
            return False
    return answer


print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	, [[8,5],[6,7],[4,1]]	))
# print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]	, [[4,1],[5,2]]		))
# print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))