# 21608. 상어 초등학교
import operator
import sys
input = sys.stdin.readline

# k번 학생의 자리를 정하는 함수
def take_seat_student(k):
    wish_list = student_dic[k] # 좋아하는 학생 번호

    temp_dic = {} # 인접한 자리에 대해 표시
    for wish_student in wish_list:
        target_seat = seat_dic[wish_student]
        if target_seat == [-1, -1]: # 아직 자리에 앉지 않은 학생인 경우
            continue
        else:
            check_adjacent_seat(target_seat, temp_dic) # 각 학생들의 인접한 자리에 표시

    targets = []  # 가장 많이 인접한 칸의 위치들을 담음 -> 이후 이 위치에서 인접한 빈칸 수로 비교
    if temp_dic: # 인접한 칸이 존재하는 경우
        sorted_dic = sorted(temp_dic.items())
        sorted_dic = sorted(sorted_dic.items(), key=operator.itemgetter(1), reverse=True)

        max_adjacent_count = sorted_dic[0][1]


        for x in sorted_dic:
            if x[1] < max_adjacent_count:
                break
            else:
                targets.append(x[0])

    else:
        # 전체 빈칸에 대해 확인해야함



# wish_student 번호 학생의 인접한 칸을 temp_dic에 표시
def check_adjacent_seat(target_seat, temp_dic):
    curr_x, curr_y = target_seat

    for i in range(4):
        next_x = curr_x + dx[i]
        next_y = curr_y + dy[i]

        if 0 <= next_x < N and 0 <= next_y < N:
            if grid[next_x][next_y] == 0: # 인접한 칸이 빈칸일때 체크
                if [next_x, next_y] in temp_dic:
                    temp_dic[[next_x, next_y]] += 1
                else:
                    temp_dic[[next_x, next_y]] = 1

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if __name__ == "__main__":
    N = int(input())
    grid = [[0 for _ in range(N)] for _ in range(N)] # 자리에 앉은 상태

    seat_dic = {} # 각 학생들의 자리 위치를 담음
    student_dic = {} # 학생(key)들이 각자 좋아하는 학생들의 번호를 담음
    for i in range(N ** 2):
        seat_dic[i] = [-1, -1] # i번 학생의 자리 위치
        line = list(map(int, input().split()))
        student_dic[line.pop(0)] = line

    # student_dic에 들어간 순서대로 자리를 정함
    for
