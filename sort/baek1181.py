import sys

n = int(sys.stdin.readline())

s = []

for i in range(n):
    c = sys.stdin.readline().rstrip('\n')
    s.append((c, len(c)))

s = list(set(s))

s.sort(key=lambda w: (w[1], w[0]))

for i in s:
    print(i[0])