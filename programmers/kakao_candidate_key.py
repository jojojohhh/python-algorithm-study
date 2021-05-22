from itertools import combinations


def dup_check(l):
    for s in l:
        if l.count(s) > 1:
            return False
    return True


def minimality(candi, combi):
    for c in candi:
        if c == c.intersection(combi):
            return False
    return True


def solution(relation):
    idx = [i for i in range(len(relation[0]))]
    candi = []
    for i in range(1, len(idx) + 1):
        combination = list(combinations(idx, i))
        for combi in combination:
            l = []
            for rel in relation:
                l.append([rel[i] for i in combi])
            if dup_check(l) and minimality(candi, set(combi)):
                candi.append(set(combi))
    return len(candi)
