import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1, n + 1):
    if i <= 99:
       cnt += 1
    else:
        l = list(map(int, str(i)))
        if l[1] - l[0] == l[2] - l[1]:
            cnt += 1
print(cnt)