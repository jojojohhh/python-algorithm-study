import sys

n = int(sys.stdin.readline())

sol = 0
while n >= 0:
    if n % 5 == 0:
        sol += (n // 5)
        print(sol)
        break
    n -= 3
    sol += 1
else:
    print(-1)

# sol = []
# for i in range(n // 5 + 1):
#     sol.append(i)
#     if n % 3 == 0:
#         sol[i] += n // 3
#     else:
#         sol[i] = -1
#     n -= 5
# sol = [i for i in sol if i != -1]
# if not sol:
#     print(-1)
# else:
#     print(min(sol))

