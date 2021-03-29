import sys


def hanoi(n, a, b, c):
    if n == 1:
        print(f'{a} {c}')
    else:
        hanoi(n - 1, a, c, b)
        print(f'{a} {c}')
        hanoi(n - 1, b, a, c)


n = int(sys.stdin.readline())
cnt = 1
for i in range(n - 1):
    cnt = cnt * 2 + 1
print(cnt)
hanoi(n, 1, 2, 3)