import sys

n1, n2 = sys.stdin.readline().rstrip('\n').split()
if int(n1[::-1]) > int(n2[::-1]):
    print(int(n1[::-1]))
else:
    print(int(n2[::-1]))

# n1, n2 = map(int, sys.stdin.readline().split())
# n1 = list(str(n1))
# n2 = list(str(n2))
# n1.reverse()
# n2.reverse()
# n1 = int(''.join(n1))
# n2 = int(''.join(n2))
# if n1 > n2:
#     print(n1)
# else:
#     print(n2)