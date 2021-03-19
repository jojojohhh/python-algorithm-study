def d(n: int):
    s = n
    for i in list(str(n)):
        s += int(i)
    return  s

l = []
for i in range(1, 10001):
    l.append(d(i))
    if i not in l:
        print(i)