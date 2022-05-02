# [1차] 추석 트래픽

from collections import deque


def solution(lines):

    q = deque()  # [start_time, end_time] 저장

    for i in range(len(lines)):
        line = lines[i]

        hh = int(line[11:13])
        mm = int(line[14:16])
        ss = float(line[17:23])
        T = float(line[24:-1])

        end_time = hh * (60 ** 2) + mm * 60 + ss
        start_time = end_time - T + 0.001

        q.append([start_time, end_time])

    count_q = deque()  # 각 로그에서 포함되는 처리 요청 개수
    for i in range(len(q)):
        curr_start, curr_end = q[i]

        curr_count = 0
        for j in range(i, len(q)):
            temp_start, temp_end = q[j]

            if temp_start < curr_end + 1:
                curr_count += 1

            # curr_end에서 닿을 수 있는 최대보다 넘어서서 temp_start가 있을 수 밖에 없는 경우
            if curr_end + 0.999 < temp_end - 3 + 0.001:  # 이 이후로는 겹칠 수가 없음 -> 다음 확인
                break
            # 위 과정을 안해도 정답이 되지만, 성능 향상에 큰 도움을 줄 때가 많음
            # 물론 조금 더 느려지는 경우도 있음(18번 테스트케이스)

        count_q.append(curr_count)

    # print(count_q)
    answer = max(count_q)

    return answer