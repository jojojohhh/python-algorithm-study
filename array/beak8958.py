import sys

n = int(sys.stdin.readline())
for i in range(n):
    l = list(sys.stdin.readline().strip('\n'))
    sum = 0
    n = 1
    for c in l:
        if c == 'O':
            sum += n
            n += 1
        else:
            n = 1
    print(sum)
