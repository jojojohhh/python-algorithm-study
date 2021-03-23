import sys


def is_prime(num):
    if num == 0:
        return False
    else:
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True


n_list = list(range(2, 246912))
p_list = []
for i in n_list:
    if is_prime(i):
        p_list.append(i)


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cnt = 0
    for i in p_list:
        if n < i <= 2 * n:
            cnt += 1
    print(cnt)