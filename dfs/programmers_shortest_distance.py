from collections import deque


def solution(maps):
    dist = {(j, i): -1 for i in range(len(maps[0])) for j in range(len(maps))}
    cardies = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    que = deque()
    que.append((0, 0))
    dist[(0, 0)] = 1
    while que:
        cur_y, cur_x = que.popleft()
        maps[cur_y][cur_x] = 0
        for y, x in cardies:
            nxt_y, nxt_x = cur_y + y, cur_x + x
            if -1 < nxt_y < len(maps) and -1 < nxt_x < len(maps[0]):
                if maps[nxt_y][nxt_x] == 1:
                    maps[nxt_y][nxt_x] = 0
                    dist[(nxt_y, nxt_x)] = dist[(cur_y, cur_x)] + 1 if dist[(nxt_y, nxt_x)] == -1 else min(dist[(cur_y, cur_x)] + 1, dist[(nxt_y, nxt_x)])
                    que.append((nxt_y, nxt_x))
    return dist[(len(maps) - 1, len(maps[0]) - 1)]
