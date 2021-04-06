import sys

n = int(sys.stdin.readline())
a = 1
p = 6
cnt = 1
if n == 1:
    print(cnt)
else:
    while True:
        a += p
        cnt += 1
        if n <= a:
            print(cnt)
            break
        p += 6