def solution(n):
    answer = ''
    if n <= 3:
        return '124'[n - 1]
    while n > 3:
        n, r = divmod(n - 1, 3)
        answer = '124'[r] + answer
    answer = '124'[n - 1] + answer
    return answer


print(solution(12))