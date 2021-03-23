import sys

t = int(sys.stdin.readline())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    r = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    r_set = [r1, r2, r]
    m = max(r_set)
    r_set.remove(m)
    if r == 0 and r1 == r2:
        print(-1)
    elif m > sum(r_set):
        print(0)
    elif r1 + r2 == r or m == sum(r_set):
        print(1)
    else:
        print(2)