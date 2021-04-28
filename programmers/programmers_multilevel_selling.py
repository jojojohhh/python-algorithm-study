def recursion(ref_dict, enroll, money, seller, idx):
    remainder = int(money * 0.1)
    answer[idx[seller]] += money - remainder
    if ref_dict[seller] != "-":
        if remainder >= 1:
            recursion(ref_dict, enroll, remainder, ref_dict[seller], idx)


def solution(enroll, referral, seller, amount):
    global answer
    answer = [0] * len(enroll)
    enroll_idx = {}
    ref_dict = {}
    for i in range(len(enroll)):
        ref_dict[enroll[i]] = referral[i]
        enroll_idx[enroll[i]] = i
    for idx, n in enumerate(seller):
        recursion(ref_dict, enroll, amount[idx] * 100, n, enroll_idx)
    return answer