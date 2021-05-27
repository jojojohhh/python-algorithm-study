from collections import deque


def solution(people, limit):
    answer = 0
    que = deque(sorted(people))
    while que:
        if len(que) > 1:
            if que[0] + que[-1] <= limit:
                que.pop(); que.popleft()
            else:
                que.pop()
            answer += 1
        else:
            if que[0] < limit:
                answer += 1
                break
    return answer
