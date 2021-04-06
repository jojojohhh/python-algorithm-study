import sys

s = sys.stdin.readline().rstrip('\n')
ca = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
ca_cnt = 0
for i in ca:
    if s.count(i) != 0:
        ca_cnt += s.count(i)
        s = s.replace(str(i), " ")

s = s.replace(" ", '')
ca_cnt += len(s)
print(ca_cnt)