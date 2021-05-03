def solution(numbers, hand):
    answer = ''
    phone = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    r = [3, 2]
    l = [3, 0]
    for number in numbers:
        if number % 3 == 1:
            answer += "L"
            l = phone[number]
        elif number % 3 == 0 and number != 0:
            answer += "R"
            r = phone[number]
        else:
            range_r = abs(r[0] - phone[number][0]) + abs(r[1] - phone[number][1])
            range_l = abs(l[0] - phone[number][0]) + abs(l[1] - phone[number][1])
            print(range_l, range_r)
            if range_r > range_l:
                answer += "L"
                l = phone[number]
            elif range_l > range_r:
                answer += "R"
                r = phone[number]
            else:
                if hand == "right":
                    answer += "R"
                    r = phone[number]
                else:
                    answer += "L"
                    l = phone[number]
        print(number, l, r)
    return answer
