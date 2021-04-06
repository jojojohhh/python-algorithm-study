import sys


def is_prime(num):
    if num == 0:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    m = n
    for j in range(n // 2, 1, -1):
        if is_prime(j) and is_prime(n - j):
            print(f'{j} {m - j}')
            break