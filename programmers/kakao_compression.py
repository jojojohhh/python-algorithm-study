def solution(msg):
    answer = []
    idx = {chr(n): i + 1 for i, n in enumerate(range(ord('A'), ord('Z') + 1))}
    i = 0
    while i < len(msg):
        s = msg[i]
        j = i
        while j < len(msg):
            if s not in idx:
                answer.append(idx[s[:len(s) - 1]])
                idx[s] = len(idx) + 1
                i = j
                break
            else:
                if j != len(msg) - 1:
                    j += 1
                    s += msg[j]
                else:
                    i = j + 1
                    break
    answer.append(idx[s])
    return answer
