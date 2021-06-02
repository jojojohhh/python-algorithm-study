from itertools import chain


def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] > 0:
                board[i][j] = min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j]) + 1
    return max(list(chain.from_iterable(board))) ** 2
