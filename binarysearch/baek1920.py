import sys

sys.setrecursionlimit(10**9)
int(sys.stdin.readline())
arr_n = sorted(list(map(int, sys.stdin.readline().split())))
int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))


def binary_search(val, arr, s, e):
    if s > e or arr[e] < val:
        return 0
    index = (s + e) // 2
    if arr[index] == val:
        return 1
    elif arr[index] > val:
        return binary_search(val, arr, s, index - 1)
    else:
        return binary_search(val, arr, index + 1, e)


for m in arr_m:
    start = 0
    end = len(arr_n) - 1
    print(binary_search(m, arr_n, start, end))