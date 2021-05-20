from collections import deque


def check(p):
    st = []
    for i in p:
        if i == '(':
            st.append(i)
        elif st:
            st.pop()
    return not st


def solution(p):
    if check(p) or len(p) == 0:
        return p
    p_que = deque(p)
    u = ""
    while p_que:
        u += p_que.popleft()
        if u.count('(') == u.count(')'):
            break
    v = ''.join(list(p_que))
    if check(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + ''.join(['(' if u[i] == ')' else ')' for i in range(1, len(u) - 1)])


print(solution("()))((()"))