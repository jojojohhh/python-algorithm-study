import sys

s = sys.stdin.readline().rstrip('\n').upper()

uni_s = list(set(s))
cnt_s = []
for i in uni_s:
    cnt = s.count(i)
    cnt_s.append(cnt)

if cnt_s.count(max(cnt_s)) > 1:
    print('?')
else:
    max_index = cnt_s.index(max(cnt_s))
    print(uni_s[max_index])

# s_dic = dict()

# for i in s :
#     if i not in s_dic.keys() :
#         s_dic[i] = 1
#     else:
#         s_dic[i] += 1
#
# max_key = [k for k, v in s_dic.items() if v == max(s_dic.values())]
# if len(max_key) >= 2 :
#     print('?')
# else :
#     print(max_key[0])