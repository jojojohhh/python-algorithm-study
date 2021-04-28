def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board[i - 1].append((i - 1) * columns + j)

    for x1, y1, x2, y2 in queries:
        min_val = 10001
        tmp = board[x1 - 1][y2 - 1]
        min_val = min(min_val, min(board[x1 - 1][y1 - 1: y2 - 1]))
        board[x1 - 1][y1: y2] = board[x1 - 1][y1 - 1: y2 - 1]

        for i in range(x1, x2):
            min_val = min(min_val, board[i][y1 - 1])
            board[i - 1][y1 - 1] = board[i][y1 - 1]

        min_val = min(min_val, min(board[x2 - 1][y1: y2]))
        board[x2 - 1][y1 - 1: y2 - 1] = board[x2 - 1][y1: y2]

        for i in range(x2 - 2, x1 - 1, -1):
            min_val = min(min_val, board[i][y2 - 1])
            board[i + 1][y2 - 1] = board[i][y2 - 1]

        board[x1][y2 - 1] = tmp
        min_val = min(min_val, tmp)
        answer.append(min_val)
    return answer
