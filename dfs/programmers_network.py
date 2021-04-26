def dfs(computers, idx, visited):
    st = [idx]
    while st:
        cur = st.pop()
        visited[cur] = True
        for i in range(len(computers)):
            if not visited[i] and computers[cur][i]:
                st.append(i)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    return answer