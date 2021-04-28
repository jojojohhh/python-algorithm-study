def solution(lottos, win_nums):
    answer = []
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
    answer.append(rank.get(cnt + lottos.count(0)))
    answer.append(rank.get(cnt))
    return answer
