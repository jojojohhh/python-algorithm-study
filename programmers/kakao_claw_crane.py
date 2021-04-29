def solution(board, moves):
    answer = 0
    st = []
    for i in moves:
        for line in board:
            if line[i - 1] != 0:
                if len(st) > 0 and st[len(st) - 1] == line[i - 1]:
                    st.pop()
                    answer += 2
                else:
                    st.append(line[i - 1])
                line[i - 1] = 0
                break
    return answer
