from itertools import combinations


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1


def solution(nums):
    answer = 0
    for num in combinations(nums, 3):
        answer += is_prime(sum(num))
    return answer