# 15686. 치킨 배달


"""
 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나
 도시의 칸은 (r, c)와 같은 형태
 r과 c는 1부터 시작

치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리는 모든 집의 치킨 거리의 합

(r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|

0은 빈 칸, 1은 집, 2는 치킨집

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업

도시의 치킨 거리가 가장 작게 
"""

def get_distance(x1, y1, x2, y2): # 두 점 사이의 거리 구하기
    return abs(x1 - x2) + abs(y1 - y2)
    

# 치킨집 위치들을 저장
# 그중 M개를 뽑았을 때, 거리를 계산
# 거리의 최소값을 저장

def get_shortest_distance(i, j, chicken_places):
    distance_min = 1e9
    
    for chicken_place in chicken_places:
        distance_temp = get_distance(i, j, chicken_place[0], chicken_place[1])
        distance_min = min(distance_min, distance_temp)

    return distance_min
        



import sys
input = sys.stdin.readline

from itertools import combinations

if __name__ == "__main__":
    n, m = map(int, input().split()) # 도시크기 n x n, 최대 치킨집 개수 m개

    city = [] # 도시의 상태를 담을 배열
    houses = []
    chicken_places = []
    
    for i in range(n): # 도시의 정보 n줄
        city.append(list(map(int, input().split())))

        for j in range(n):
            if city[i][j] == 1: # 집 위치 저장
                houses.append((i,j))
            elif city[i][j] == 2: # 치킨집 위치 저장
                chicken_places.append((i, j))

    # 치킨집 총 개수가 M보다 작거나 같은 경우, 그대로 두면 됨
    if len(chicken_places) <= m:
        picked_places_list = [chicken_places]
    else:
        # M개보다 많은 경우, 그중 M개를 뽑는 경우의 수만큼 수행
        picked_places_list = list(combinations(chicken_places, m))

##    print(picked_places_list)
    
    total_min = 1e9
    for picked_places in picked_places_list: #  m개를 뽑은 경우들에 대하여 진행
        total_temp = 0
        # 모든 집들에 대해 치킨거리를 구해 더함
        for house in houses:
##            print(house[0])
##            print(house[1])
##            print(picked_places)
            total_temp += get_shortest_distance(house[0], house[1], picked_places)

        total_min = min(total_min, total_temp)

    print(total_min)

    
