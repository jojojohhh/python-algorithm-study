import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip('\n')
n_sum = 0
for i in range(len(s)):
    n_sum += int(s[i])
print(n_sum)