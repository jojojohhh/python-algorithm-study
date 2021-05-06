def solution(d, budget):
    d.sort()
    answer = 0
    for n in d:
        if n <= budget:
            answer += 1
            budget -= n
        else:
            break
    return answer
