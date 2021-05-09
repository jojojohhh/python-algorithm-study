def check(coords, place):
    distance = [(1, 0), (-1, 0), (2, 0), (-2, 0), (0, 1), (0, -1), (0, 2), (0, -2), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    print(coords)
    for coord in coords:
        for d in distance:
            a = ((coord[0] + d[0]), (coord[1] + d[1]))
            if a in coords:
                if a[0] == coord[0] or a[1] == coord[1]:
                    if place[(coord[0] + a[0]) // 2][(coord[1] + a[1]) // 2] != "X":
                        return False
                else:
                    print(coord, a)
                    print(place[coord[0]][a[1]], place[a[0]][coord[1]])
                    if place[coord[0]][a[1]] != "X" or place[a[0]][coord[1]] != "X":
                        return False
    return True


def solution(places):
    answer = []
    coords = list()
    for place in places:
        for i, p in enumerate(place):
            for j in range(len(p)):
                if p[j] == "P":
                    coords.append((i, j))
        if check(coords, place):
            answer.append(1)
        else:
            answer.append(0)
        coords = []
    return answer
