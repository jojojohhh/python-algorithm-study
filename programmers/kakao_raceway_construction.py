def solution(board):
    answer = 0
    coord = {(0, 0): 0}
    way = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    que = []
    if board[0][1] == 0:
        que.append((0, 1, 0, 100))
        coord[(0, 1)] = 100
    if board[1][0] == 0:
        que.append((1, 0, 2, 100))
        coord[(1, 0)] = 100
    while que:
        y, x, v, c = que.pop(0)
        for idx, data in enumerate(way):
            m_x, m_y = data[1] + x, data[0] + y
            if m_x < 0 or m_y < 0 or m_x >= len(board) or m_y >= len(board) or board[m_y][m_x] == 1:
                continue
            if v == idx:
                total_c = 100 + c
            else:
                total_c = 600 + c
            if coord.get((m_y, m_x)) is not None and total_c > coord.get((m_y, m_x)):
                continue

            coord[(m_y, m_x)] = total_c
            que.append((m_y, m_x, idx, total_c))
    answer = coord[(len(board) - 1, len(board) - 1)]
    print(coord)
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))