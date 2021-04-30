def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        if room.get(num) is None:
            room[num] = num + 1
            answer.append(num)
        else:
            l = [num]
            while True:
                num = room.get(num)
                if room.get(num) is None:
                    room[num] = num + 1
                    answer.append(num)
                    for i in l:
                        room[i] = num + 1
                    break
                l.append(num)
    return answer
