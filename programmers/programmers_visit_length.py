def solution(dirs):
    v = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    road = {(0, 0): []}
    cur = [0, 0]
    bef = [0, 0]
    for d in dirs:
        cur = [x + y for x, y in zip(cur, v[d])]
        if not (-5 <= cur[0] <= 5 and -5 <= cur[1] <= 5):
            cur = bef
            continue
        if cur not in road.get(tuple(bef), []) and bef not in road.get(tuple(cur), []):
            road[tuple(bef)] = road.get(tuple(bef), []) + [cur]
            road[tuple(cur)] = road.get(tuple(cur), []) + [bef]
        bef = cur
    return sum([len(v) for k, v in road.items()]) // 2
