import sys

n = int(sys.stdin.readline())
cnt = 0

# s_list = []
# for i in range(n):
#     check = True
#     s = sys.stdin.readline().rstrip('\n')
#     bef = ''
#     for j in s:
#         if bef != j:
#             if s_list.count(j) == 0:
#                 s_list.append(bef)
#                 bef = j
#             else:
#                 check = False
#                 break
#     s_list.clear()
#     if check:
#         cnt += 1

for i in range(n):
    s = sys.stdin.readline().rstrip('\n')
    check = True
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            new_s = s[i + 1:]
            if new_s.count(s[i]) > 0:
                check = False
                break
    if check:
        cnt += 1
print(cnt)