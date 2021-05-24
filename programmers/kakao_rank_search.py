def solution(info, query):
    rel = [i.split(' ') for i in info]
    query = [list(filter(lambda x: x != "and", q.split(' '))) for q in query]
    answer = [len(list(filter(lambda x: ((x[0] == q[0] or q[0] == '-') and (x[1] == q[1] or q[1] == '-') and (x[2] == q[2] or q[2] == '-') and (x[3] == q[3] or q[3] == '-') and (int(x[4]) >= int(q[4]))), rel))) for q in query]
    return answer
