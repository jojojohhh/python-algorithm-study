import sys

n, m = map(int, sys.stdin.readline().split())
chess = []
for i in range(n):
    chess.append(sys.stdin.readline().rstrip('\n'))

new_chess = []
for i in range(n - 7):
    for j in range(m - 7):
        cnt_w = 0
        cnt_b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if chess[k][l] != 'W':
                        cnt_w = cnt_w + 1
                    elif chess[k][l] != 'B':
                        cnt_b = cnt_b + 1
                else:
                    if chess[k][l] != 'W':
                        cnt_b = cnt_b + 1
                    elif chess[k][l] != 'B':
                        cnt_w = cnt_w + 1
        new_chess.append(cnt_w)
        new_chess.append(cnt_b)

print(min(new_chess))