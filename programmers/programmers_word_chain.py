def solution(n, words):
    c = set([words[0]])
    for i in range(1, len(words)):
        if words[i] in c or words[i][0] != words[i - 1][-1]:
            return [i % n + 1, i // n + 1]
        else:
            c.add(words[i])
    return [0, 0]
