def solution(s):
    answer = len(s)
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        bef = s[0:i]
        cnt = 1
        s1 = ""
        for j in range(i, len(s), i):
            s2 = s[j:j+i]
            if bef == s2:
                cnt += 1
            else:
                s1 += str(cnt) + bef if cnt > 1 else bef
                cnt = 1
                bef = s2
        s1 += str(cnt) + bef if cnt > 1 else bef
        answer = len(s1) if answer > len(s1) else answer
    return answer
