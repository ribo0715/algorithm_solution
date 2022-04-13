# 23291. 어항 정리
import copy
import sys
input = sys.stdin.readline


# 어항을 한 번 정리하는 과정
def change_fish_bowl():
    global fish

    # 물고기 수가 가장 적은 어항에 물고기를 추가
    put_fish_in_min()

    # 어항 쌓기 시작
    # 가장 왼쪽에 있는 어항을 그 오른쪽 위로 올림
    fish[1].append(fish.pop(0)[0])
    # print(fish)
    # 2개 이상 쌓여있는 어항을 계속 공중부양시켜가며 회전
    while True:
        if not rotate_more_two():
            break

    # 어항에 있는 물고기의 수 조절
    control_fish_num()

    # print(fish)
    make_floor_line()
    # print(fish)

    rotate_half()
    # print(fish)
    rotate_half()
    # print(fish)
    control_fish_num()
    make_floor_line()



# max, min 차이
def get_diff_max_min():
    return max(fish)[0] - min(fish)[0]

# 왼쪽 N/2개를 공중부양 -> 오른쪽 N/2개 위에 놓음
def rotate_half():
    global fish

    index_half = len(fish) // 2 - 1

    for i in range(index_half + 1):
        for j in reversed(range(len(fish[i]))):
            fish[len(fish) - 1 - i].append(fish[i][j])

    for _ in range(index_half + 1):
        fish.pop(0)


# 바닥에 일렬로 놓음
def make_floor_line():
    global fish

    temp = copy.deepcopy(fish)

    fish = []
    for x in temp:
        for y in x:
            fish.append([y])


def control_fish_num():
    global fish

    temp = copy.deepcopy(fish)

    for x in range(len(temp)):
        for y in range(len(temp[x])):

            for i in range(4): # 상 하 좌 우
                temp_x = x + dx[i]
                temp_y = y + dy[i]

                if 0 <= temp_x < len(temp) and 0 <= temp_y < len(temp[temp_x]):
                    diff = temp[x][y] - temp[temp_x][temp_y]
                    d = abs(diff) // 5
                    if d > 0 and diff > 0:
                        fish[x][y] -= d
                        fish[temp_x][temp_y] += d

# 상 하 좌 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


# 2개 이상 쌓여있는 어항 공중 부양시킨 이후 위로 올림
def rotate_more_two():
    global fish

    index_more_two = -1
    last_length = 1

    for i in range(len(fish)):
        if len(fish[i]) >= 2:
            if last_length > len(fish[i]): # 공중부양 시킬 수가 없는 경우
                return False
            else:
                last_length = len(fish[i])

            index_more_two += 1
        else:
            break


    if len(fish) - index_more_two - 1 < last_length: # 공중 부양시킬 수 없는 경우
        return False

    for i in reversed(range(index_more_two + 1)):
        for j in range(len(fish[i])):
            fish[index_more_two + 1 + j].append(fish[i][j])

    for _ in range(index_more_two + 1):
        fish.pop(0)

    return True


# 물고기가 가장 적게 있는 곳에 물고기 한 마리 추가
def put_fish_in_min():
    min_fish_num = 10001
    for x in fish:
        min_fish_num = min(min_fish_num, min(x))

    for x in fish:
        for i in range(len(x)):
            if x[i] == min_fish_num:
                x[i] += 1


# 어항들의 모습을 어떻게 저장하지? 각 위치에 대한 2차원 배열? -> 굳

if __name__ == "__main__":
    N, K = map(int, input().split())
    fish = [[] for _ in range(N)] # 각 위치에 아래서부터 위로 놓인 물고기들의 수를 담음
    line = list(map(int, input().split()))


    for i in range(N):
        fish[i].append(line[i])
    # print(fish)
    # put_fish_in_min()
    # print(fish)
    count = 0

    while True:
        if max(fish)[0] - min(fish)[0] <= K:
            break

        count += 1
        change_fish_bowl()


    # print(fish)
    # print("count :", count)
    print(count)