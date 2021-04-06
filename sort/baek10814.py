import sys

n = int(sys.stdin.readline())

s = []

for i in range(n):
    c = list(sys.stdin.readline().rstrip('\n').split())
    s.append(c)

s.sort(key=lambda w: int(w[0]))

for i in s:
    print(i[0], i[1])