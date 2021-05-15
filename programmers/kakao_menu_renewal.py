from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    a = []
    for c in course:
        b = []
        for order in orders:
            b.extend(list(combinations(order, c)))
        print(b)
        a.append(Counter(b))
    for i in a:
        if len(i) > 0:
            max_val = max(i.values())
            for k, v in i.items():
                if max_val == 1:
                    continue
                if max_val == v:
                    answer.append(''.join([j for j in k]))
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))