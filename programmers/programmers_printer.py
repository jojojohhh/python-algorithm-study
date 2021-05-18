from collections import deque


def solution(priorities, location):
    answer = 0
    new_prior = deque([[i, d] for i, d in enumerate(priorities)])
    while new_prior:
        prior = new_prior.popleft()
        max_prior = max(new_prior, key=lambda x: x[1])[1] if len(new_prior) > 0 else 0
        if prior[1] < max_prior:
            new_prior.append(prior)
        else:
            answer += 1
            if prior[0] == location:
                return answer
