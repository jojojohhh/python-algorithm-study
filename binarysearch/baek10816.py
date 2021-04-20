import sys
from collections import Counter

int(sys.stdin.readline())
arr_n = map(int, sys.stdin.readline().split())
int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

cnt = Counter(arr_n)
print(' '.join(f'{cnt[m]}' if m in cnt else '0' for m in arr_m))

