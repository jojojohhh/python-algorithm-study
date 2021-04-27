def solution(prices):
    answer = []
    prices.reverse()
    while prices:
        a = prices.pop()
        cnt = 1
        for i in range(len(prices) - 1, 0, -1):
            if a > prices[i]:
                break
            else:
                cnt += 1
        if prices:
            answer.append(cnt)
        else:
            answer.append(0)
    return answer
