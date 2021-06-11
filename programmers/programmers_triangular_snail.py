from itertools import chain


def solution(n):
    s = [[0] * i for i in range(1, n + 1)]
    i, j, cnt = 0, 0, 1
    last = sum([len(i) for i in s])
    nxt_coord = {'RIGHT': [0, 1], 'DOWN': [1, 0], 'UP': [-1, -1]}
    state = 'DOWN'
    while True:
        if cnt > last:
            break
        if not s[i][j]:
            s[i][j] = cnt
            if i == n - 1 and j < len(s[i]) - 1:
                state = 'RIGHT'
            elif j == len(s[i]) - 1 and i != 0:
                state = 'UP'
            cnt += 1
        else:
            nxt_i, nxt_j = nxt_coord[state]
            i -= nxt_i
            j -= nxt_j
            if state == 'RIGHT':
                state = 'UP'
            elif state == 'UP':
                state = 'DOWN'
            else:
                state = 'RIGHT'
        nxt_i, nxt_j = nxt_coord[state]
        i += nxt_i
        j += nxt_j
    return list(chain.from_iterable(s))

