def solution(s):
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if st:
                st.pop()
            else:
                return False
    return True if len(st) == 0 else False
