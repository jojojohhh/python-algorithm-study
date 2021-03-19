import sys

l = []
for i in range(10):
    l.append(int(sys.stdin.readline()) % 42)
l = set(l)
print(len(l))