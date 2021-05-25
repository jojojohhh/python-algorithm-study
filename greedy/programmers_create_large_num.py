def solution(number, k):
    st = [number[0]]
    for num in number[1:]:
        while st and st[-1] < num and k > 0:
            k -= 1
            st.pop()
        st.append(num)
    return ''.join(st[:-k]) if k != 0 else ''.join(st)
