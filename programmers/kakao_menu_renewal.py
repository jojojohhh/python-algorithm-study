from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        b = []
        for order in orders:
            b.extend([''.join(sorted(combi)) for combi in combinations(order, c)])
        counter = Counter(b).most_common()
        answer += [k for k, v in counter if 1 < v == counter[0][1]]
    return sorted(answer)
