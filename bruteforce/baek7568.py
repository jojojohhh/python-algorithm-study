import sys

n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(list(map(int, sys.stdin.readline().split())))

for i in n_list:
    r = 1
    for j in n_list:
        if i[0] < j[0] and i[1] < j[1]:
            r = r + 1
    print(r, end=' ')