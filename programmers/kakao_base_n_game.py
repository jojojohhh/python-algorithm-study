def solution(n, t, m, p):
    answer = '01'
    d = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    decimal = 2
    while len(answer) < t * m:
        num = decimal
        base = ''
        while num > 0:
            div = num // n
            mod = num % n
            num = div
            if mod >= 10:
                base += d[str(mod)]
            else:
                base += str(mod)
        answer += base[::-1]
        decimal += 1
    return ''.join([answer[i] for i in range(p-1, t * m, m)])
