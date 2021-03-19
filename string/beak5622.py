import sys

s = list(sys.stdin.readline().rstrip('\n'))
sol = 0
for i in s:
    if 'A' <= i <= 'C':
        sol += 3
    elif 'D' <= i <= 'F':
        sol += 4
    elif 'G' <= i <= 'I':
        sol += 5
    elif 'J' <= i <= 'L':
        sol += 6
    elif 'M' <= i <= 'O':
        sol += 7
    elif 'P' <= i <= 'S':
        sol += 8
    elif 'T' <= i <= 'V':
        sol += 9
    else:
        sol += 10

# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# s = sys.stdin.readline().rstrip('\n')
# sol = 0
# for j in range(len(s)):
#     for i in dial:
#         if s[j] in i:
#             sol += dial.index(i)+3
print(sol)