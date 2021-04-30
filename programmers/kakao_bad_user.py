from itertools import permutations


def compare_to(user, ban):
    for i in range(len(user)):
        if len(user[i]) != len(ban[i]):
            return False
        for j in range(len(ban[i])):
            if ban[i][j] != "*" and user[i][j] != ban[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = list()
    for i in permutations(user_id, len(banned_id)):
        if compare_to(i, banned_id):
            i = set(i)
            if i not in answer:
                answer.append(i)
    return len(answer)
