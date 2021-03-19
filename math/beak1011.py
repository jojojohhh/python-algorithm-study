import sys

t = int(sys.stdin.readline())
for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    d = y - x
    cnt = 0
    m = 1
    m_sum = 0
    while m_sum < d:
        cnt += 1
        m_sum += m
        if cnt % 2 == 0:
            m += 1
    print(cnt)