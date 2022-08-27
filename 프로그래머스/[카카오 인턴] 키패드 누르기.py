# [카카오 인턴] 키패드 누르기
"""
1,4,7 -> 왼손
3,6,9 -> 오른손
가운데(2,5,8,0) -> 양손에서 가까운 손가락 -> 거리가 같으면 오른손잡이면 오른손 사용

왼손, 오른손의 위치를 저장

A와 B사이의 거리를 구하는 함수
"""


def get_distance(A_x, A_y, B_x, B_y):
    return abs(A_x - B_x) + abs(A_y - B_y)


def solution(numbers, hand):
    answer = ''
    # 키패드 위치 -> "1"위치가 (0,0), "6"위치는 (1,2)
    L_x, L_y = 3, 0  # "*" 키패드 위치
    R_x, R_y = 3, 2  # "#" 키패드 위치

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            L_y = 0
            L_x = [1, 4, 7].index(number)

        elif number in [3, 6, 9]:
            answer += "R"
            R_y = 2
            R_x = [3, 6, 9].index(number)

        elif number in [2, 5, 8, 0]:
            target_x = [2, 5, 8, 0].index(number)
            target_y = 1

            L_distance = get_distance(target_x, target_y, L_x, L_y)
            R_distance = get_distance(target_x, target_y, R_x, R_y)

            if L_distance > R_distance:
                R_x = target_x
                R_y = target_y
                answer += "R"
            elif L_distance < R_distance:
                L_x = target_x
                L_y = target_y
                answer += "L"
            else:
                # 어느손잡이인지에 따라 이동
                if hand == "left":
                    L_x = target_x
                    L_y = target_y
                    answer += "L"
                else:
                    R_x = target_x
                    R_y = target_y
                    answer += "R"

    return answer