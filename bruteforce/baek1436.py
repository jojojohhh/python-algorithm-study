import sys

n = int(sys.stdin.readline())
t = 666
cnt = 0
while True:
    if '666' in str(t):
        cnt = cnt + 1
    if cnt == n:
        print(t)
        break
    t = t + 1