from itertools import permutations


def is_prime(num):
    cnt = 0
    for i in num:
        check = True
        if i <= 1:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                check = False
        if check:
            cnt += 1
    return cnt


def solution(numbers):
    s = []
    for i in range(1, len(numbers) + 1):
        tmp = permutations(numbers, i)
        for j in tmp:
            tmp_str = "".join(j)
            s.append(int(tmp_str))
    s =list(set(s))
    return is_prime(s)