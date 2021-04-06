import math
import sys


def star(n):
    n_list = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            n_list.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            n_list.append(n[i % len(n)] * 3)
    return n_list


n = int(sys.stdin.readline())

k = int(math.log(n, 3) - 1)

star_list = ["***", "* *", "***"]
for i in range(k):
    star_list = star(star_list)
for i in star_list:
    print(i)