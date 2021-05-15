import re


def solution(str1, str2):
    str1, str2 = str.upper(str1), str.upper(str2)
    s1 = re.sub('[^A-Z]', "", str1)
    str1 = list(zip(str1, str1[1:]))
    s1 = list(set(zip(s1, s1[1:])) & set(str1))
    s2 = re.sub('[^A-Z]', "", str2)
    str2 = list(zip(str2, str2[1:]))
    s2 = list(set(zip(s2, s2[1:])) & set(str2))
    intersection = list(set(s1) & set(s2))
    union = list(set(s1) | set(s2))
    dup = []
    for i in intersection:
        m = min(str1.count(i), str2.count(i))
        for j in range(1, m):
            dup.append(i)
    intersection.extend(dup)
    dup = []
    for i in union:
        m = max(str1.count(i), str2.count(i))
        for j in range(1, m):
            dup.append(i)
    union.extend(dup)
    if len(union) == 0:
        return 65536
    return int(len(intersection) / len(union) * 65536)
