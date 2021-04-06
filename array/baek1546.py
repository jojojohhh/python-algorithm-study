import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = max(l)
for i in range(len(l)):
    l[i] = l[i] / m * 100
print(sum(l)/len(l))