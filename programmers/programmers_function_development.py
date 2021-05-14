def solution(progresses, speeds):
    answer = []
    a = [(100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else (100 - progresses[i]) // speeds[i] + 1  for i in range(len(progresses)-1, -1, -1)]
    deploy = []
    deploy.append(a.pop())
    answer.append(1)
    while a:
        s = a.pop()
        if deploy[len(deploy) - 1] >= s:
            d = deploy[len(deploy) - 1]
            answer[len(answer) - 1] += 1
        else:
            d = s
            answer.append(1)
        deploy.append(d)
    return answer
