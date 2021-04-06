import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in m:
    check = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check or i == 2:
        cnt += 1

print(cnt)