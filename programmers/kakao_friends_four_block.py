from collections import deque


def check_block(m, n, x, y, board, cur):
    que = deque([[y, x]])
    new_board = [list(b) for b in board]
    cardies = [[0, 1], [1, 0], [1, 1]]
    coord = {(y, x)}
    cnt = 0
    while que:
        qy, qx = que.popleft()
        if qy == m - 1 or qx == n - 1:
            continue
        new_que = deque()
        for dy, dx in cardies:
            nxt_x, nxt_y = dx + qx, dy + qy
            if board[nxt_y][nxt_x] != cur:
                break
            new_que.append([nxt_y, nxt_x])
        if len(new_que) == len(cardies):
            new_board[y][x] = '0'
            cnt += 1
            for dy, dx in new_que:
                if new_board[dy][dx] != '0':
                    new_board[dy][dx] = '0'
                    coord.add((dy, dx))
                    cnt += 1
            que.extend(new_que)
    print(coord)
    return new_board


def solution(m, n, board):
    answer = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] != '0':
                board = check_block(m, n, j, i, board, board[i][j])
    print(board)
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))