import sys

t = int(sys.stdin.readline())
for i in range(t):
    r, s = sys.stdin.readline().rstrip('\n').split()
    m = ''
    for i in s:
        m += int(r) * i
    print(m)