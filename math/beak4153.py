import math
import sys

while True:
    n_list = list(map(int, sys.stdin.readline().split()))
    if n_list[0] == 0 and n_list[1] == 0 and n_list[2] == 0:
        break
    y = max(n_list[0], n_list[1], n_list[2])
    n_list.remove(y)
    x = n_list.pop()
    z = n_list.pop()
    if y == math.sqrt(math.pow(x, 2) + math.pow(z, 2)):
        print('right')
    else:
        print("wrong")