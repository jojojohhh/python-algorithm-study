def is_correct(s):
    st = []
    open_b = ['(', '{', '[']
    close_b = [')', '}', ']']
    pair = {')': '(', '}': '{', ']': '['}
    for b in s:
        if b in open_b:
            st.append(b)
        elif b in close_b:
            if len(st) == 0 or st[len(st) - 1] != pair[b]:
                return False
            st.pop()
    if len(st) > 0:
        return False
    return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        if is_correct(new_s):
            answer += 1
    return answer
