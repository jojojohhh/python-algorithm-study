def check(p):
    st = []
    for i in p:
        if i == '(':
            st.append(i)
        else:
            if len(st) == 0:
                return False
            st.pop()
    if len(st) == 0:
        return True


def recursion(p):
    if check(p):
        return p
    u = [p[0]]
    for i in range(1, len(p)):
        u.append(p[i])
        if u.count('(') == u.count(')'):
            v = list(p[i + 1:])
            break
    if not check(u):
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        new_u = ['(']
        new_u.extend(u[1:len(u) - 1])
        new_u.append(')')
        new_u.extend(recursion(v))
        return new_u
    else:
        u.extend(recursion(v))
        return u


def solution(p):
    if check(p) or len(p) == 0:
        return p
    return ''.join(recursion(list(p)))


print(solution("()))((()"))