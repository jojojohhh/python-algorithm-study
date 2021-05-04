def solution(gems):
    answer = [1, 100000]
    gem = set(gems)
    r = 0
    l = 0
    dic = {gems[0]: 1}
    while r < len(gems) and l < len(gems):
        if len(dic) == len(gem):
            if answer[1] - answer[0] > r - l:
                answer = [l + 1, r + 1]
            if dic[gems[l]] > 1:
                dic[gems[l]] -= 1
            else:
                del dic[gems[l]]
            l += 1
        else:
            if r == len(gems) - 1:
                break
            else:
                r += 1
                if dic.get(gems[r]) is None:
                    dic[gems[r]] = 1
                else:
                    dic[gems[r]] += 1
    return answer
