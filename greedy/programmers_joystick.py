def solution(name):
    answer = 0
    name = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    idx = 0
    while True:
        answer += name[idx]
        name[idx] = 0
        if sum(name) == 0:
            return answer
        l, r = 1, 1
        while name[idx - l] == 0:
            l += 1
        while name[idx + r] == 0:
            r += 1
        answer += l if l < r else r
        idx += -l if l < r else r
