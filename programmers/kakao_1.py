def solution(s):
    answer = ""
    a = ""
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for i in s:
        if '0' <= i <= '9':
            answer += i
        else:
            a += i
            if dic.get(a) is not None:
                answer += dic[a]
                a = ""
    return answer
