from collections import deque
from math import inf


def solution(N, road, K):
    dic = {}
    for n in road:
        dic[n[0]] = dic.get(n[0], []) + [[n[1], n[2]]]
        dic[n[1]] = dic.get(n[1], []) + [[n[0], n[2]]]
    dist = {i: inf if i != 1 else 0 for i in range(1, N + 1)}
    que = deque([1])
    while que:
        cur = que.popleft()
        for nxt in dic[cur]:
            if dist[nxt[0]] > dist[cur] + nxt[1]:
                dist[nxt[0]] = dist[cur] + nxt[1]
                que.append(nxt[0])
    answer = len([1 for _, a in dist.items() if a <= K])
    return answer
