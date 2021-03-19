import sys

c = int(sys.stdin.readline())
for i in range(c):
    l = list(map(int, sys.stdin.readline().split()))
    n = l[0]
    del l[0]
    avg = sum(l) / len(l)
    r = 0
    for j in l:
        if j > avg:
            r += 1
    r = r / len(l) * 100
    print("%0.3f%%" % r)