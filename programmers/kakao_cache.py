from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.upper()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer
