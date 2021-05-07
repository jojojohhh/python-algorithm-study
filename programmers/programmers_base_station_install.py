def solution(n, s, w):
    answer = 0
    c = 1
    i = 0
    while c <= n:
        if i >= len(s) or c < s[i] - w:
            c += 2 * w + 1
            answer += 1
        else:
            c = s[i] + w + 1
            i += 1
    return answer