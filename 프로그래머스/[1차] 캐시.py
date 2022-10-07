# [1차] 캐시

def solution(cacheSize, cities):
    answer = 0

    cache = [0] * cacheSize

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            idx = cache.index(city)  # index를 조정해줌 -> 가장 최근에 확인한 걸로
            cache.pop(idx)
        else:
            answer += 5
            cache.pop(0)  # 가장 오래된 곳을 빼냄

        cache.append(city)  # 가장 최근에 확인한 걸로 표시

    return answer