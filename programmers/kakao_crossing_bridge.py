def check(stone, k, m):
    cnt = 0
    for i in range(len(stone)):
        if stone[i] - m <= 0:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True


def solution(stones, k):
    r = max(stones)
    l = min(stones)
    while True:
        if l > r:
            break
        m = (r + l) // 2
        if check(stones, k, m):
            l = m + 1
        else:
            r = m - 1
    return l
