def solution(numbers):
    return str(int(''.join(sorted(list(map(str, a)), key=lambda x: x*3, reverse=True))))


a = [6, 10, 2]
print(solution(a))