import operator
from collections import Counter


def solution(s):
    answer = []
    a = sorted(dict(Counter(list(map(int, s.replace("{", "").replace("}", "").split(","))))).items(), key=operator.itemgetter(1), reverse=True)
    for key, _ in a:
        answer.append(key)
    return answer
