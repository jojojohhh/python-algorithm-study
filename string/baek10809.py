import sys

s = list(sys.stdin.readline().rstrip('\n'))
for i in range(26):
    if chr(i + 97) not in s:
        print(-1, end=' ')
    else:
        print(s.index(chr(i + 97)), end=' ')