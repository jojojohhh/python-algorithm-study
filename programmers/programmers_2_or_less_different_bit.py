def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            num = list('0' + str(format(num, 'b')))
            for i in range(len(num) - 1, -1, -1):
                if num[i] == '0':
                    num[i] = '1'
                    num[i + 1] = '0'
                    break
            answer.append(int(''.join(num), 2))
    return answer
