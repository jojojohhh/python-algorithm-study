def solution(answers):
    answer = []
    no_1 = [1, 2, 3, 4, 5]
    no_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    no_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if no_1[i % len(no_1)] == answers[i]:
            cnt[0] += 1
        if no_2[i % len(no_2)] == answers[i]:
            cnt[1] += 1
        if no_3[i % len(no_3)] == answers[i]:
            cnt[2] += 1
    for i, s in enumerate(cnt):
        if s == max(cnt):
            answer.append(i + 1)
    return answer


s = [1, 3, 2, 4, 2]
print(solution(s))