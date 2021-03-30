import sys
from collections import Counter

n = int(sys.stdin.readline())
n_arr = []
for i in range(n):
    n_arr.append(int(sys.stdin.readline()))

print("%.f"%(sum(n_arr) / n))

n_arr.sort()
print(n_arr[n // 2])

m_arr = Counter(n_arr).most_common()

if len(m_arr) > 1:
    if m_arr[0][1] == m_arr[1][1]:
        print(m_arr[1][0])
    else:
        print(m_arr[0][0])
else:
    print(m_arr[0][0])

print(n_arr[-1]  - n_arr[0])