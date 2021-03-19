import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

n = a * b * c
l = list(str(n))
for i in range(10):
    cnt = l.count(str(i))
    print(cnt)

# l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(str(n))):
#     l[int(str(n)[i])] += 1
# for i in range(len(l)):
#     print(l[i])