def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    while True:
        coord = set()
        for i in range(1, n):
            for j in range(1, m):
                if board[i][j] == board[i - 1][j] == board[i][j - 1] == board[i - 1][j - 1] != '-1':
                    coord |= {(i, j), (i - 1, j), (i, j - 1), (i - 1, j - 1)}
        for i, j in coord:
            board[i][j] = '-1'
        for i in range(len(board)):
            mov_block = ['-1'] * board[i].count('-1')
            board[i] = mov_block + [b for b in board[i] if b != '-1']
        if len(coord) == 0:
            return answer
        answer += len(coord)
