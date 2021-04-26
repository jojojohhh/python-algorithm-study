def dfs(numbers, target, idx, value):
    if idx == len(numbers):
        if target == value:
            return 1
        return 0
    return dfs(numbers, target, idx + 1, value + numbers[idx]) + dfs(numbers, target, idx + 1, value - numbers[idx])


def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer
