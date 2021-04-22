from collections import Counter
from functools import reduce


def solution(clothes):
    c = Counter([i[1] for i in clothes])
    return reduce(lambda x, y: x * (y + 1), c.values(), 1) - 1


s = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(s))