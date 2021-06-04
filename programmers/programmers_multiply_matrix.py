def solution(arr1, arr2):
    return [[sum(r * c for r, c in zip(a1, a2)) for a2 in zip(*arr2)] for a1 in arr1]
