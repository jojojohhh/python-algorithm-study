import math


def solution(arr):
    n = arr.pop()
    for a in arr:
        n = n * a // math.gcd(n, a)
    return n
