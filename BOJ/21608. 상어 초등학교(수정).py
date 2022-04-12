# 21608. 상어 초등학교
import operator
import sys
input = sys.stdin.readline

# 각 학생들의 위치를 어떻게 나타내지? -> student_dict 해당 학생번호에 위치를 추가
# 2차원 배열에 학생의 위치를 나타냄


# 해당 학생이 좋아하는 학생들과 가장 많이 인접한 칸을 구함
def find_most_adjacent(student_num):
    like_student_nums = student_dict[student_num]

    adjacent_dict = {} # 인접한 칸에 대한 카운트

    # 좋아하는 학생들이 이미 교실에 존재하는 경우, 인접한 칸들을 표시
    for like_student in like_student_nums:
        # print("여기!", like_student)
        if len(student_dict[like_student]) >= 5: # 좌표까지 포함하고 있는 경우 -> 교실에 존재
            # print("여기!", like_student)
            like_student_x = student_dict[like_student][-1][0]
            like_student_y = student_dict[like_student][-1][1]

            for i in range(4): # 상 하 좌 우 표시
                temp_x = like_student_x + dx[i]
                temp_y = like_student_y + dy[i]

                if 0 <= temp_x < N and 0 <= temp_y < N: # 교실 내
                    if classroom[temp_x][temp_y] == 0:
                        if (temp_x, temp_y) in adjacent_dict:
                            adjacent_dict[(temp_x, temp_y)] += 1
                        else:
                            adjacent_dict[(temp_x, temp_y)] = 1

    most_adjacent_list = []
    # print("adjacent_dict", adjacent_dict)
    # 인접한 칸 수가 많은 순서대로 정렬
    adjacent_list = sorted(adjacent_dict.items(), key=operator.itemgetter(1), reverse=True)
    max_count = 0
    for i in range(len(adjacent_list)):
        if max_count == adjacent_list[i][1]:
            most_adjacent_list.append(tuple(adjacent_list[i][0]))
        elif max_count < adjacent_list[i][1]:
            max_count = adjacent_list[i][1]
            most_adjacent_list = [tuple(adjacent_list[i][0])]

    # print("most_adjacent_list", most_adjacent_list)
    return most_adjacent_list


# 인접한 칸 중 비어있는 칸이 가장 많은 칸을 구함
def find_most_empty(most_adjacent_list):
    empty_dict = {}
    for x in most_adjacent_list:
        empty_dict[x] = 0 # 각 지점에서 인접한 칸 중 비어있는 칸의 수

    if not most_adjacent_list: # 인접한 칸이 없는 경우
        # 전체 빈칸에서 확인
        for x in range(N):
            for y in range(N):
                if classroom[x][y] == 0: # 빈 곳에서
                    empty_dict[(x, y)] = 0
                    for i in range(4): # 상 하 좌 우
                        adjacent_x = x + dx[i]
                        adjacent_y = y + dy[i]

                        if 0 <= adjacent_x < N and 0 <= adjacent_y < N:
                            if classroom[adjacent_x][adjacent_y] == 0:
                                empty_dict[(x, y)] += 1

    else:
        for (temp_x, temp_y) in most_adjacent_list:
            for i in range(4): # 상 하 좌 우
                adjacent_x = temp_x + dx[i]
                adjacent_y = temp_y + dy[i]

                if 0 <= adjacent_x < N and 0 <= adjacent_y < N:
                    if classroom[adjacent_x][adjacent_y] == 0:
                        empty_dict[(temp_x, temp_y)] += 1

    most_empty_list = []

    # 비어있는 칸 수가 많은 순서대로 정렬
    empty_list = sorted(empty_dict.items(), key=operator.itemgetter(1), reverse=True)
    max_count = 0

    for i in range(len(empty_list)):
        if max_count == empty_list[i][1]:
            most_empty_list.append(empty_list[i][0])
        elif max_count < empty_list[i][1]:
            max_count = empty_list[i][1]
            most_empty_list = [empty_list[i][0]]

    # print("most_empty_list", most_empty_list)
    return most_empty_list



# 행, 열이 가장 작은 칸을 구함
def find_smallest_x_y(most_empty_list):
    # print(sorted(most_empty_list)[0])
    return sorted(most_empty_list)[0]


# 만족도 총 합
def calc_total_satisfaction():
    total_satisfaction = 0
    for x in range(N):
        for y in range(N):
            student = classroom[x][y]
            count = 0

            for i in range(4):
                temp_x = x + dx[i]
                temp_y = y + dy[i]

                if 0 <= temp_x < N and 0 <= temp_y < N:
                    if classroom[temp_x][temp_y] in student_dict[student]:
                        count += 1

            if count == 0:
                satisfaction = 0
            else:
                satisfaction = 10 ** (count - 1)

            total_satisfaction += satisfaction

    return total_satisfaction

# def print_classroom():
#     print("==== classroom ====")
#     for i in range(N):
#         print(classroom[i])
#     print("===================")

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if __name__ == "__main__":
    N = int(input())
    classroom = [[0 for _ in range(N)] for _ in range(N)] # 각 위치에 있는 학생들을 나타냄

    student_dict = {} # 각 학생이 좋아하는 학생의 번호들을 담음
    for _ in range(N ** 2):
        line = list(map(int, input().split()))

        student_num = line.pop(0)
        like_student_nums = line

        student_dict[student_num] = like_student_nums

    # print(student_dict)

    for student in student_dict:
        # print(student, "번 학생의 자리를 정함")
        most_adjacent_list = find_most_adjacent(student)
        most_empty_list = find_most_empty(most_adjacent_list)
        (x_pick, y_pick) = find_smallest_x_y(most_empty_list)

        classroom[x_pick][y_pick] = student
        student_dict[student].append([x_pick, y_pick])
        # print(student, "번 학생의 자리 :", x_pick, ",", y_pick)
        # print(student_dict)

    # print_classroom() # 교실 상태 출력
    print(calc_total_satisfaction())
